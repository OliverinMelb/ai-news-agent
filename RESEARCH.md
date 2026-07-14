# 调研原始结果汇总（2026-07-14）

三个方向：① GitHub 同类开源项目 ② Reddit/HN 社区讨论 ③ 可复用 MCP/插件生态。
另附 ④ 用户提到的三个项目的核实结果。

---

# ① GitHub 同类开源项目

## 一、与目标定位最接近的综合型项目

### 1. finaldie/auto-news — 个人多源资讯聚合 + LLM 过滤
- URL: https://github.com/finaldie/auto-news （~900★）
- 技术栈: Python + LangChain，Docker/K8s/Helm 部署
- 架构: 多源抓取（RSS、Reddit、Twitter/X、YouTube 转写、网页文章）→ 基于个人兴趣的 LLM 过滤（宣称降噪 80%+）→ 排序 → 推送到 Notion，另有周报/TODO 生成
- LLM: 是（ChatGPT / Gemini / Ollama via LangChain，摘要 + 相关性过滤 + insight 提取）
- 点评: 与需求（多渠道→过滤去重→推送）架构几乎一一对应

### 2. Thysrael/Horizon — AI 新闻雷达（管线设计最清晰）
- URL: https://github.com/Thysrael/Horizon （~8.1k★）
- 技术栈: Python（uv）、Docker，多 LLM 提供商（Claude/GPT/Gemini/DeepSeek/Ollama 等）
- 架构: 配置定义 → 抓取（HN、RSS/Atom、Reddit、Telegram 频道、Twitter/X 用户、GitHub releases）→ 去重 → **LLM 0-10 打分**（阈值过滤）→ 上下文/社区评论富化 → 摘要 → 交付（GitHub Pages、邮件、Feishu/DingTalk/Slack/Discord webhook、MCP 接口），中英双语
- 点评: "score → threshold → enrich → deliver" 评分管线是可直接借鉴的核心模式

### 3. sansan0/TrendRadar — 多平台热点监控 + AI 筛选（国内生态最全）
- URL: https://github.com/sansan0/TrendRadar （~60k★）
- 技术栈: Python + SQLite（可选 S3/R2）+ Docker / GitHub Actions 无服务器部署 + LiteLLM（100+ provider）
- 架构: 35 个平台热榜 + RSS 抓取 → 关键词精筛 + `filter_pipeline` AI 筛选 → 翻译/情感分析/简报 → 9 种推送渠道（企业微信/飞书/钉钉/Telegram/邮件/ntfy/Bark/Slack/Webhook）
- 特色: **自带 MCP server**，可在 Claude Desktop/Cursor 里自然语言分析热点；GitHub Actions fork 即用

### 4. iliane5/meridian — "总统级"每日情报简报
- URL: https://github.com/iliane5/meridian （~2.4k★）
- 技术栈: TypeScript（Turborepo、Cloudflare Workers/Workflows、Hono、PostgreSQL + Drizzle、Nuxt 3）
- 架构: 数百 RSS → 正文提取 → LLM 逐篇分析 → **embedding 聚类（multilingual-e5 + UMAP + HDBSCAN）**→ 簇审查 → 深度分析 → Markdown 简报
- LLM: Gemini 2.0 Flash 低成本处理 2000+ 篇/天，2.5 Pro 做长上下文对比
- 点评: "embedding 聚类去重"是比纯 URL 去重更高级的方案

### 5. smol-ai AINews（swyx）— AI 工程师日报的事实标准
- URL: https://github.com/smol-ai/ainews-web-2025 （站点 https://news.smol.ai/ ）
- 架构: 监控头部 AI Discord + Reddit + X → LLM 汇总 → 每工作日 newsletter（15 万+ 订阅）
- 点评: 产品形态标杆；管线核心未完全开源，输出格式（url + 一句话摘要分区）值得模仿

## 二、用 LLM 做"相关性判断 + 摘要"的项目

| 项目 | URL | Stars | 要点 |
|---|---|---|---|
| Horizon | https://github.com/Thysrael/Horizon | ~8.1k | LLM 0-10 打分过滤 |
| auto-news | https://github.com/finaldie/auto-news | ~900 | LangChain 兴趣过滤 |
| meridian | https://github.com/iliane5/meridian | ~2.4k | LLM 分析 + embedding 聚类 |
| reddit-ai-trends | https://github.com/liyedanpdx/reddit-ai-trends | ~850 | Reddit 官方 API 抓 11 个 AI subreddit → DeepSeek R1 分析排名 → 每日中英双语 markdown |
| hacker-news-digest | https://github.com/polyrabbit/hacker-news-digest | ~750 | HN → ML 正文提取 → GPT 摘要（回退本地 T5）→ GitHub Pages + RSS |
| hn_summary | https://github.com/jiggy-ai/hn_summary | ~250 | 轮询 HN topstories → GPT 摘要 → Telegram 频道，支持 👎 反馈 |
| teledigest | https://github.com/igoropaniuk/teledigest | ~20 | 双 Telegram 客户端，SQLite FTS5，LLM 可配 OpenAI/Ollama |
| daily-ai-news-digest | https://github.com/viochris/daily-ai-news-digest | 小型 | Gemini + DuckDuckGo，Prefect 编排，Telegram 日推 |
| llm-daily-review | https://github.com/vfalbor/llm-daily-review | 小型 | 抓 HN 的 LLM 应用 → Docker 隔离实测 → 11 项打分 → 周榜 |

## 三、纯规则 / RSS 聚合（不用 LLM）

| 项目 | URL | Stars | 要点 |
|---|---|---|---|
| newsnow | https://github.com/ourongxing/newsnow | ~21k | TS 多平台实时热点聚合，30min 缓存，提供 MCP server；`server/sources` 适配器目录结构值得参考 |
| AI-News-Aggregator-Bot | https://github.com/hrnrxb/AI-News-Aggregator-Bot | ~20 | feedparser + SQLite 去重 + GitHub Actions 每 5h → Telegram；纯规则版最小可行架构 |
| awesome-trending-repos | https://dev.to/furkankoykiran/awesome-trending-repos-auto-tracking-github-trending-1afj | 小型 | Octokit + Actions 每日抓 trending 回写 README |
| awesome-ai-news | https://github.com/taielab/awesome-ai-news | 列表 | AI 新闻聚合工具 curated list，二次挖掘索引 |

## 四、基于 Agent 框架的示例

- **Claude Agent SDK**: https://github.com/anthropics/claude-agent-sdk-demos （~2.6k★）Research Agent demo：拆子主题 → 并行 spawn 子代理 WebSearch → 汇总；cookbook: https://platform.claude.com/cookbook/claude-agent-sdk-00-the-one-liner-research-agent
- **LangGraph**: https://github.com/nickhawn/news-agent ；多代理新闻引擎实践 https://medium.com/@shubham.shardul2019/how-i-built-an-autonomous-multi-agentic-news-engine-full-implementation-ef09a2f00f33
- **CrewAI**: https://github.com/topics/ai-news-agent ；https://github.com/aleph2136/newsfloor-agent
- 生态索引: https://github.com/githubnext/awesome-continuous-ai （"Continuous AI"：Actions 定时跑 LLM 任务的模式集合）

## 五、架构共识

1. 主流管线: 源适配器 → URL/hash 去重（SQLite 最常见，进阶 embedding 聚类）→ LLM 打分过滤 → LLM 摘要（批量省 token）→ 多渠道推送（Telegram 最普遍）
2. 零成本运行: GitHub Actions cron + 仓库内 SQLite/markdown 持久化（TrendRadar、reddit-ai-trends 等都是）
3. 趋势: 头部项目都在加 MCP server，让聚合结果可被 Claude/Cursor 对话式查询

---

# ② Reddit / HN 社区讨论

## 讨论帖清单

### "如何跟上 AI 资讯"类（HN）
1. **Ask HN: How to keep up with AI/ML as a full stack dev?**（79 分/77 评论）https://news.ycombinator.com/item?id=41226035
   - 推荐源：Latent Space、Ben's Bites、Ethan Mollick、Zvi Mowshowitz、X（"比 HN 领先约 4 个月"）、YouTube 的 Yannic Kilcher / Matt Wolfe / Matthew Berman、r/LocalLLaMA
   - 心态："让时间替你降噪"——不追每条新闻，定期回看沉淀下来的东西
2. **Ask HN: What do you read to keep up with AI?** https://news.ycombinator.com/item?id=42799142
   - Simon Willison 博客、Gary Marcus、Stratechery、官方博客直订
   - 反面清单：**避开"AI 摘要 arxiv 再转卖"的量产 newsletter**
3. **Ask HN: keep up without drowning in noise?** https://news.ycombinator.com/item?id=46157688
   - HN 按周热度看而非实时刷；"always-on 信息流会变成另一种刷手机"——每周主动查 2-3 次胜过持续监控
4. **Ask HN: stay on top of AI tech?** https://news.ycombinator.com/item?id=44585887 及 **bleeding edge of AI tooling?** https://news.ycombinator.com/item?id=48565601
   - 高赞共同答案：**smol.ai AI News**——"别自己造轮子先订这个"

### "自己造 AI 新闻 agent"类（Show HN）
5. **AI fetches RSS feeds based on your prompt** https://news.ycombinator.com/item?id=44447866 — 每小时轮询 ~2000 RSS → embedding → 与自然语言 prompt 语义匹配；被指出的坑：embedding 成本、去重、准确率未说明
6. **Graph – AI-sorted RSS feeds** https://news.ycombinator.com/item?id=44974884 — 1600+ 源日拉 ~3000 条 → 兴趣画像 embedding 匹配打分；高赞质疑：**杀死偶遇性（serendipity）**，此类系统的结构性缺陷
7. **Where to put AI summary in custom RSS** https://news.ycombinator.com/item?id=40082096 — 自定义 XML namespace 会被阅读器忽略，摘要直接塞 `description` 字段
8. **personal AI news curator (n8n + OpenAI)** https://news.ycombinator.com/item?id=46492685 — **只把标题喂 GPT-4o-mini 按兴趣打 0-10 分，<7 丢弃**，过线才 Tavily 抓全文摘要 → 邮件；便宜模型只判标题是控制成本的通行做法
9. **Show HN: RSS Filter** https://news.ycombinator.com/item?id=39887678 — 自托管，从已读文章学习兴趣；同类：RSSbrew https://github.com/yinan-c/RSSbrew

### Reddit
10. **r/LocalLLaMA: how do you stay up to date?** https://www.reddit.com/r/LocalLLaMA/comments/1h1hiku/
    - 推荐 AI News（smol.ai）+ AlphaSignal、X 研究者 List、HF 直接 follow 机构、AI Timeline https://nhlocal.github.io/AiTimeline/ 、YouTube Matt Wolfe / Matthew Berman / AICodeKing
    - 有人明确提出"让 LLM 把梗图筛掉只留相关信息"；反方："找一个模型用熟，深度优于广度"
11. **r/SideProject 一批同类项目帖**：https://www.reddit.com/r/SideProject/comments/1k0uzja/ （ainews.email）、https://www.reddit.com/r/SideProject/comments/1kiv0je/ （AI 时间线日更）、https://www.reddit.com/r/SideProject/comments/1k57n4c/ （每 6h 聚类去重）、https://www.reddit.com/r/SideProject/comments/1keucey/ （caveman.press 复盘）——共同难题：**去重/聚类** 和 **摘要可信度**
12. **r/ChatGPTCoding: GPT Weekly** https://www.reddit.com/r/ChatGPTCoding/comments/13v1hr9/ — 人挑选 + GPT 辅助摘要的早期形态

## 公认信噪比高的源
- Newsletter：smol.ai AI News（日）、AlphaSignal、TLDR AI、Ben's Bites；周更深度：Interconnects、Ahead of AI、Import AI、The Batch。**共识：日更 1 份 + 周更 1-2 份，超过 3 份必然大量重复**
- 博客：Simon Willison（工程实践第一推荐）、Ethan Mollick、Zvi、Gary Marcus（反炒作制衡）、官方博客直订
- 社区：r/LocalLLaMA、r/MachineLearning、HN（按周热度；hnrss.org 可按分数/关键词出定制 RSS）、HF、GitHub Trending、X List（最快但最吵）

## YouTube/TikTok：只取元数据/字幕喂 LLM（路线已收敛）
- 标准管线：① `youtube-transcript-api` 拉现成字幕（零下载最便宜）② 无字幕回退 yt-dlp → Whisper ③ 摘要用便宜模型或本地 Ollama
- **Show HN: Summary Cat** https://news.ycombinator.com/item?id=37617288 — 实测：GPT-4 摘要质量只好 20% 但贵 10 倍；10 分钟视频约 $0.03；坑：超长视频爆上下文只超时不报错；prompt 里要声明"这是视频"
- 极简做法 https://www.danielcorin.com/til/yt-dlp/summarizing-video-transcript/ ；全本地 https://blog.stephenturner.us/p/video-to-audio-transcript-to-summary-whisperfile-llama ；定时盯频道 https://www.mindstudio.ai/blog/ai-news-digest-agent-claude-code-trigger-dev
- 局限：只覆盖"说出来的内容"，演示画面/代码屏录全丢；transcript 库是非官方通道，云 IP 常被拒；**TikTok 侧几乎无讨论，社区默认放弃**

## 跨帖踩坑汇总
1. 信息过载的解法是先砍源，不是更多自动化
2. 去重是所有 digest 项目的第一难题（embedding 聚类或 LLM 判重，每 6h 一次是常见节奏）
3. LLM 成本控制：便宜模型只看标题打分 + 阈值 + 两级漏斗
4. Reddit API 收费后大家走 OAuth 凭证或归档 API；RSS 因无门槛成最稳底座
5. embedding 兴趣匹配消灭 serendipity —— 一些项目开始留"随机探索"配额
6. 自建 vs 订阅：先订 smol.ai，确认满足不了再自建

---

# ③ 可复用 MCP / 插件生态

## 代码/仓库搜索
| 名称 | URL | 能力 | 限制 |
|---|---|---|---|
| **Grep MCP（Vercel 官方）** | https://mcp.grep.app / https://vercel.com/blog/grep-a-million-github-repositories-via-mcp | 约 100 万公开仓库正则/字面量代码搜索，按语言/repo/路径过滤 | **免 key 免账号**；只搜代码内容 |
| GitHub 官方 MCP | https://github.com/github/github-mcp-server | search_repositories（`created:>date stars:>n` 找新项目）、issue/PR、releases | 需 PAT；search 30 req/min |
| mcp-github-trending | https://github.com/hetaoBackend/mcp-github-trending | 抓 trending 页面，daily/weekly/monthly 按语言过滤 | 非官方，页面改版会失效；官方替代 = Search API 近似 |

## 社区内容
| 名称 | URL | 能力 | 限制 |
|---|---|---|---|
| HN Algolia API | https://hn.algolia.com/api | `search_by_date` + `numericFilters=points>100`，"近 24h 高分帖"的完美原语 | **免 key**，~10000 req/h，curl 即可 |
| hackernews-mcp | https://github.com/devrelopers/hackernews-mcp | 封装 Firebase + Algolia | 免 key 只读 |
| reddit-mcp | https://github.com/GeLi2001/reddit-mcp | 官方 API 搜帖/subreddit 热帖 | 需免费 app 凭证；OAuth 后 60 req/min |

## 视频
| 名称 | URL | 能力 | 限制 |
|---|---|---|---|
| kirbah/mcp-youtube | https://github.com/kirbah/mcp-youtube | YouTube Data API 搜索/元数据 | 免费 key；**10000 units/天，search 一次 100 units** |
| mcp-youtube-transcript | https://github.com/jkawamoto/mcp-youtube-transcript | 按 URL 拉字幕，多语言分页 | 免 key 不占配额；云 IP 偶被封 |
| claude-code-youtube-mcp | https://github.com/wynandw87/claude-code-youtube-mcp | 搜索+元数据+字幕+trending 一体 | 社区，混用官方 API 与抓取 |
| TikTok | https://developers.tiktok.com/products/research-api/ | 官方 Research API 仅限欧美学术/非营利 | **无可行公开通道**；只有付费抓取（有封禁风险）→ v1 放弃 |

## 通用检索
| 名称 | URL | 免费额度 |
|---|---|---|
| Brave Search MCP | https://github.com/brave/brave-search-mcp-server | 2000 次/月，支持 freshness |
| Tavily MCP | https://github.com/tavily-ai/tavily-mcp | 1000 credits/月，LLM 优化返回 |
| Exa MCP | https://github.com/exa-labs/exa-mcp-server | ~$10 额度，语义搜索"找类似 X 的新项目" |
| Firecrawl MCP | https://github.com/firecrawl/firecrawl-mcp-server | 1000 credits/月，url → 干净 markdown |

## 推送
| 名称 | URL | 说明 |
|---|---|---|
| Telegram Bot API | https://core.telegram.org/bots/api | 一个 sendMessage POST；MCP 封装 https://github.com/kstonekuan/telegram-notification-mcp |
| ntfy | https://ntfy.sh | `POST https://ntfy.sh/<topic>` 一行推手机；MCP https://github.com/cyanheads/ntfy-mcp-server |
| Slack Webhook | https://api.slack.com/messaging/webhooks | 官方免费 |
| Resend MCP | https://github.com/resend/mcp-send-email | 邮件 digest，免费 100 封/天 |

## MCP 目录
- 官方 Registry https://registry.modelcontextprotocol.io ；PulseMCP https://www.pulsemcp.com/servers （搜 rss/news 命中多款现成 server）；Smithery https://smithery.ai/servers ；mcp.so https://mcp.so

## 最省事组合
HN Algolia（免 key）+ GitHub 官方 MCP search（PAT 免费）+ Tavily/Brave 之一 + YouTube transcript MCP（免 key）配少量 Data API search，推送用 Telegram Bot API 或 ntfy.sh —— 全链路零爬虫零付费，只需 2 个免费 key，TikTok 放弃。

---

# ④ 用户提到的三个项目核实（2026-07-14）

| 项目 | 核实结果 |
|---|---|
| **openclaw-newsroom** | ✅ 存在且高度相关：https://github.com/jacob-bd/openclaw-newsroom （172★）。5 数据源（25 个 RSS + 13 个 subreddit + X + GitHub trending/releases + Tavily 搜索）→ 关键词预过滤 → SQLite 评分去重 → 前 8 篇富化全文 → 3 层 LLM 故障转移链（Gemini Flash Lite → Grok → Gemini Flash）策展 3-7 篇。纯 Python 标准库 + Shell，~$5/月。设计为 OpenClaw cron 任务，但**脚本可脱离 OpenClaw 独立运行** |
| **ai-news-intelligence** | ❌ 未找到同名知名仓库。同名搜索命中的是 [koala73/worldmonitor](https://github.com/koala73/worldmonitor)（61.8k★，实时全球情报仪表盘，偏地缘/基建监控，不是开发工具资讯）和一批小型聚合器，如 [hoangsonww/AI-News-Briefing](https://github.com/hoangsonww/AI-News-Briefing)（多代理日报管线，推 Notion/Obsidian/Slack） |
| **accio-ai** | ❌ 无对应新闻聚合知名项目。GitHub 上同名的是几个 0-3★ 小仓库（语音听写、RAG demo），其中 krxthx/accio-ai 自称"终端 AI 新闻摘要器"但 0★ 无活跃度 |
