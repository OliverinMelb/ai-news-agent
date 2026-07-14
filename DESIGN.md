# AI 开发资讯拉取 Agent — 设计文档（v0.1，只设计不开发）

> 目标：一个**主动拉取**（而非被算法推送）的 agent，定期从 GitHub / Reddit / HN / YouTube 等渠道
> 抓取与"AI 辅助开发"强相关的最新资讯 —— 好用的 skills、MCP server、Claude Code / Cursor 插件、
> agent 工具链、前后端开发新工具 —— 过滤去重后，以 **`url + 一句话描述`** 的清单形式推送给我。
> 不做视频流、不做全文阅读器，输出就是一份可扫读的 digest。

---

## 0. 调研结论速览（设计依据）

调研覆盖 GitHub 开源项目、Reddit/HN 社区讨论、MCP/插件生态三个方向，核心结论：

1. **这个轮子有人造过，架构已收敛。** 最接近的参考：
   - [Thysrael/Horizon](https://github.com/Thysrael/Horizon)（~8k★）：抓取 → 去重 → **LLM 0-10 打分过滤** → 富化 → 摘要 → 多渠道交付，管线最干净；
   - [finaldie/auto-news](https://github.com/finaldie/auto-news)（~900★）：RSS/Reddit/Twitter/YouTube 多源 + 个人兴趣 LLM 过滤，宣称降噪 80%+；
   - [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar)（~60k★）：GitHub Actions 免服务器 + 9 种推送渠道 + 自带 MCP server；
   - [iliane5/meridian](https://github.com/iliane5/meridian)（~2.4k★）：embedding 聚类去重的进阶方案；
   - 产品形态标杆：[smol.ai AI News](https://news.smol.ai/)（url+一句话摘要分区，HN 上"先订这个再考虑自建"的默认答案）。
2. **抓取层不需要写爬虫**，现成 MCP / 官方 API 全覆盖（详见 §3 工具层）。
3. **社区公认的坑**（详见 §6 设计红线）：去重是第一难题；LLM 打分要用便宜模型只看标题控制成本；
   embedding 兴趣过滤会杀死偶遇性（serendipity）；TikTok 无可行公开接口，直接放弃。

---

## 1. 定位与边界

| 维度 | 决定 | 理由 |
|---|---|---|
| 形态 | 定时批处理 agent（每日 1 次为主节奏），不是常驻服务 | HN 多帖共识：always-on 信息流会变成另一种刷手机；每周主动查 2-3 次胜过持续监控 |
| 输出 | `url + 中文一句话描述`，按类别分区的 markdown digest | 用户明确要求；smol.ai 已验证该形态可扫读性最好 |
| 视频 | **只取元数据（标题/描述），必要时取字幕，不碰视频流** | 字幕→LLM 摘要是社区收敛路线；画面/代码演示信息注定丢失，接受此损失 |
| TikTok | v1 放弃 | 官方 Research API 仅限欧美学术机构；无可靠免费 MCP；只有付费抓取服务且有封禁风险 |
| 主题 | 聚焦"AI 辅助开发工具链"：MCP server、Claude Code skills/plugins、agent 框架、前后端 AI 工具；**不做**泛 AI 新闻/融资/政策 | 砍源砍主题是社区第一条降噪经验 |

## 2. 总体架构

```
┌─ 调度层 ─────────────────────────────────────────────┐
│  GitHub Actions cron（免服务器，主推荐）             │
│  或 本机任务计划 / Claude Code scheduled agent       │
└──────────────────────┬────────────────────────────────┘
                       ▼
┌─ 抓取层（全部用现成 MCP / 官方 API，每源一个适配器）─┐
│ GitHub搜索 │ HN Algolia │ Reddit │ YouTube │ RSS │ Web搜索 │
└──────────────────────┬────────────────────────────────┘
                       ▼
┌─ 处理管线（两级漏斗，Horizon 模式）──────────────────┐
│ ① 规范化：统一为 {url, title, source, ts, meta}      │
│ ② 去重：URL 规范化哈希 + SQLite seen 表（v2: embedding 聚类）│
│ ③ 粗筛：便宜模型只看 标题+描述 按兴趣画像打 0-10 分  │
│    阈值（如 ≥7）以下丢弃 —— 这里消耗 90% 的候选      │
│ ④ 富化：仅对过线条目拉详情（README / 字幕 / 正文）    │
│ ⑤ 精摘要：生成一句话中文描述 + 分类标签               │
│ ⑥ 偶遇配额：保留 1-2 条"低分但新奇"的条目防过滤气泡  │
└──────────────────────┬────────────────────────────────┘
                       ▼
┌─ 送达层 ─────────────────────────────────────────────┐
│ 主：markdown digest 落盘（digests/2026-07-14.md）    │
│ 副：Telegram Bot API 或 ntfy.sh 一个 HTTP POST 推手机 │
└───────────────────────────────────────────────────────┘
```

## 3. 工具层选型（不写爬虫，全用现成件）

| 源/功能 | 选型 | 官方性 | 成本/限制 |
|---|---|---|---|
| GitHub 新项目 | [GitHub 官方 MCP](https://github.com/github/github-mcp-server) 的 `search_repositories`，query 形如 `mcp OR "claude code" created:>N天前 sort:stars` | 官方 | 免费 PAT；search 30 req/min |
| GitHub trending | 官方无 API。用上面 Search API 近似（稳定）；备选社区 [mcp-github-trending](https://github.com/hetaoBackend/mcp-github-trending)（爬页面，有失效风险） | 近似官方 | 免费 |
| **代码级验证（grep）** | [Grep MCP（mcp.grep.app，Vercel 官方）](https://vercel.com/blog/grep-a-million-github-repositories-via-mcp)：对 100 万公开仓库正则搜索 | 官方 | **免 key、免账号** |
| Hacker News | [HN Algolia API](https://hn.algolia.com/api)：`search_by_date + numericFilters=points>50` 直接拿"近 24h 高分帖" | 官方认可 | **免 key**，~10000 req/h，curl 即可 |
| Reddit | 社区 [reddit-mcp](https://github.com/GeLi2001/reddit-mcp) 或官方 API；盯 r/ClaudeAI、r/mcp、r/LocalLLaMA、r/ChatGPTCoding | API 官方 | 免费 app 凭证；60 req/min |
| YouTube 搜索/元数据 | YouTube Data API v3（MCP 封装如 [kirbah/mcp-youtube](https://github.com/kirbah/mcp-youtube)） | 官方 | 免费 key；**10000 units/天，search 一次 100 units → 省着用，优先盯固定频道的 uploads（1 unit）** |
| YouTube 字幕 | [jkawamoto/mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript) | 社区 | 免 key、不占配额；云 IP 偶被封 |
| 通用 Web 搜索 | Tavily 或 Brave Search MCP（二选一） | 官方 MCP | 免费档 1000-2000 次/月 |
| 正文提取 | Firecrawl MCP（url → 干净 markdown，给 ⑤ 精摘要用） | 官方 MCP | 免费 1000 credits/月 |
| RSS 底座 | PulseMCP 上多款 RSS MCP；hnrss.org 可按关键词/分数出定制 feed | — | 免费，最稳的兜底 |
| 推送 | Telegram Bot API 一个 `sendMessage`，或 `POST https://ntfy.sh/<topic>` | 官方 | 免费 |

**grep.app MCP 在设计中的角色**（回答"插件能不能参与设计"）：它不是资讯源，而是**验证器**——
digest 里出现一个新 MCP server / 插件时，用 grep.app 搜真实代码库里的引用量（如 `"@xxx/mcp-server"` 出现在多少仓库的
`package.json` / `.mcp.json` 里），把"营销热度"和"真实采用"区分开，作为打分的一个加权信号。这是同类开源项目都没做的差异化点。

## 4. 关键设计决策

### 4.1 两级漏斗控制 LLM 成本（社区通行做法）
- **粗筛**用 Haiku 级便宜模型，输入只有 `标题 + 描述 + 来源 + 热度指标`，按固定兴趣画像 prompt 打 0-10 分；
  实测参考（HN Show HN 帖）：只判标题的成本可忽略，<7 分丢弃能砍掉 90% 候选。
- **精摘要**才用强模型，且只处理过线的 10-30 条。
- 兴趣画像是一个受版本管理的 prompt 文件（`profile.md`），写明：高兴趣 = MCP/skills/agent 工具链/前后端 AI 工具；
  低兴趣 = 融资新闻、政策、泛 AGI 讨论、营销软文。调口味只改这个文件。

### 4.2 去重
- v1：URL 规范化（去 utm、统一 http(s)、GitHub url 取 owner/repo）→ 哈希 → SQLite `seen(url_hash, first_seen, score)` 表。
  同一条目再次出现只更新热度，不重复推送；**但热度跨阈值跃升（如 HN 上榜后又爆了）允许二次推送并标注**。
- v2（可选）：标题 embedding + 聚类，解决"同一事件不同 URL"（meridian 的方案），先不做。

### 4.3 防过滤气泡（serendipity 配额）
每期 digest 固定保留 1-2 条"分数不高但来源新/类型新"的条目，单独放"🎲 意外发现"区。
这是 HN 上对 embedding 过滤类产品最集中的批评，用配额制廉价对冲。

### 4.4 YouTube 策略（v0.2 修订：只用标题+描述，走频道 RSS）
- **不用 Data API、不用字幕**。每个频道天然有 RSS feed：
  `https://www.youtube.com/feeds/videos.xml?channel_id=<ID>`，内含标题+描述+链接，
  免 key、无配额、零封锁风险 —— YouTube 退化为普通 RSS 源，任何 RSS 底座原生支持。
- 维护固定频道清单（如 Matt Wolfe、Matthew Berman、AICodeKing、Fireship 等），标题+描述直接进粗筛。
- 代价：无法验证内容质量（标题党/营销描述）。可接受——输出本来就是 url+desc 让人自己点。
- v2 兜底：过线但描述空洞的**单条**视频才按需拉字幕富化（jkawamoto/mcp-youtube-transcript），
  且 prompt 中声明"这是视频字幕"（Summary Cat 实测坑）。

### 4.5 digest 格式（输出契约）
```markdown
# AI Dev Digest — 2026-07-14

## 🔧 MCP / 插件（3）
- [xxx-mcp](url) — 一句话：它是什么、解决什么、为什么值得看。⭐️新增 800/周 · 已被 40+ 仓库引用(grep)
## 🤖 Agent / 框架（2）
- ...
## 🎬 视频（2）
- [标题](url) — 频道 · 时长 · 字幕摘要一句话
## 💬 讨论（2）
- [Ask HN: ...](url) — 结论一句话
## 🎲 意外发现（1）
- ...
```

## 5. 运行形态候选（二选一，倾向 A）

| | A. GitHub Actions cron（推荐） | B. 本机 Claude Code 定时 agent |
|---|---|---|
| 成本 | 免服务器、免开机 | 需本机在线 |
| 持久化 | SQLite/digest 直接 commit 回仓库 | 本地文件 |
| LLM 调用 | 走 API key（Haiku 粗筛 + Sonnet 摘要） | 可复用本机 Claude Code 会话与 MCP 配置 |
| 参考先例 | TrendRadar、reddit-ai-trends、AI-News-Aggregator-Bot 全走此路 | Claude Code `/schedule` 云端 routine 亦可 |

## 6. 设计红线（来自社区踩坑汇总）

1. **先砍源再谈自动化**：v1 源不超过 6 路（GitHub 搜索、HN、2-3 个 subreddit、固定 YouTube 频道单、1 个通用搜索兜底）。
2. **不追实时**：每日一跑；HN 按分数过滤而非刷 new。
3. **Reddit 官方 API 有风控**，无认证 `.json` 端点约 10 req/min，一定走 OAuth 凭证。
4. **YouTube 字幕库是非官方通道**，云服务器 IP 可能被拒——Actions 里失败要静默降级为"只有标题+描述"。
5. **自建的对照组**：先订阅 smol.ai AI News 一周，digest 质量以"是否稳定给出它没有的、更贴前后端开发的条目"为验收标准。

## 7. v1 范围与里程碑（供未来开发参考，本文档不含实现）

- M1：GitHub + HN 两路 → 粗筛 → digest 落盘（跑通漏斗）
- M2：+ Reddit、YouTube 频道单、grep 验证信号、Telegram 推送
- M3：+ serendipity 配额、二次推送逻辑、兴趣画像调优
- 未决问题：① 推送频率日报 vs 周报二档？② 兴趣画像初版由谁写（建议先由 agent 访谈式生成）？③ 是否要中英双语描述？

## 8. 基座选型（v0.2 增补：直接基于开源改，不从零写）

| | Horizon (8.1k★) | TrendRadar (60k★) | auto-news (900★) | openclaw-newsroom (172★) |
|---|---|---|---|---|
| 源模型 | 配置化（HN/RSS/Reddit/X/GitHub releases），加源=改配置 | 35 平台**热榜**+RSS，偏大众热点 | RSS/Reddit/X/YouTube | 5 源，关键词/prompt 偏硬编码 |
| 过滤 | LLM 0-10 打分+阈值 ✅ | 关键词精筛+AI 筛选 | LangChain 兴趣过滤 | 关键词预过滤+LLM 策展 |
| 输出 | Pages/邮件/webhook + MCP 接口 | 9 推送渠道 + MCP server | Notion（K8s/Airflow，部署重） | OpenClaw 频道 |
| 改造成本 | **最低** | 中（源模型与需求错位） | 高 | 低但需动代码、社区小 |

**决定：Horizon 当基座**，openclaw-newsroom 当参考实现（SQLite 去重、3 层 LLM 故障转移值得读）。
说明：各项目自带的 MCP server 是**输出侧**能力（在 Claude/Cursor 里对话查询聚合结果），
是加分项而非选型核心；选型核心是源模型与过滤管线的贴合度。

**基于 Horizon 的改造清单（全部在配置/prompt 层）：**
1. 源配置：HN 关键词（mcp/claude code/cursor/agent）、r/ClaudeAI + r/mcp + r/ChatGPTCoding、
   重点仓库 GitHub releases、YouTube 频道 RSS 清单（§4.4）、smol.ai RSS 兜底对照；
2. 打分 prompt 换成兴趣画像（§4.1 profile.md）；
3. 交付通道配 Telegram/邮件，digest 模板按 §4.5；
4. 唯一可选代码：grep.app 采用量验证，管线外独立小脚本，后置不阻塞。

## 附：完整调研来源

- 开源同类：[Horizon](https://github.com/Thysrael/Horizon) · [auto-news](https://github.com/finaldie/auto-news) · [TrendRadar](https://github.com/sansan0/TrendRadar) · [meridian](https://github.com/iliane5/meridian) · [newsnow](https://github.com/ourongxing/newsnow) · [reddit-ai-trends](https://github.com/liyedanpdx/reddit-ai-trends) · [hacker-news-digest](https://github.com/polyrabbit/hacker-news-digest) · [hn_summary](https://github.com/jiggy-ai/hn_summary) · [AI-News-Aggregator-Bot](https://github.com/hrnrxb/AI-News-Aggregator-Bot) · [RSSbrew](https://github.com/yinan-c/RSSbrew) · [claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos) · [awesome-continuous-ai](https://github.com/githubnext/awesome-continuous-ai)
- 讨论帖：[Ask HN: keep up with AI as full stack dev](https://news.ycombinator.com/item?id=41226035) · [What do you read to keep up with AI](https://news.ycombinator.com/item?id=42799142) · [without drowning in noise](https://news.ycombinator.com/item?id=46157688) · [bleeding edge of AI tooling](https://news.ycombinator.com/item?id=48565601) · [Show HN: AI-sorted RSS](https://news.ycombinator.com/item?id=44974884) · [Show HN: personal AI news curator (n8n)](https://news.ycombinator.com/item?id=46492685) · [Show HN: Summary Cat](https://news.ycombinator.com/item?id=37617288) · [r/LocalLLaMA: how do you stay up to date](https://www.reddit.com/r/LocalLLaMA/comments/1h1hiku/)
- 工具层：[Grep MCP](https://vercel.com/blog/grep-a-million-github-repositories-via-mcp) · [GitHub MCP](https://github.com/github/github-mcp-server) · [HN Algolia](https://hn.algolia.com/api) · [reddit-mcp](https://github.com/GeLi2001/reddit-mcp) · [mcp-youtube](https://github.com/kirbah/mcp-youtube) · [mcp-youtube-transcript](https://github.com/jkawamoto/mcp-youtube-transcript) · [PulseMCP](https://www.pulsemcp.com/servers) · [官方 MCP Registry](https://registry.modelcontextprotocol.io)
