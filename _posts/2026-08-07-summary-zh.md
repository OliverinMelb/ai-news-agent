---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 98 条内容中筛选出 8 条重要资讯。

---

1. [Codex rust-v0.147.0 发布：新增便携插件与 MCP 2026-07-28 支持](#item-1) ⭐️ 8.0/10
2. [Superpowers：26.8 万星标的子代理驱动开发技能框架](#item-2) ⭐️ 8.0/10
3. [ECC：238K 星 AI 编码代理性能优化工具](#item-3) ⭐️ 8.0/10
4. [Graphify 用 AST 解析把任意代码库变成可查询的知识图谱](#item-4) ⭐️ 8.0/10
5. [DeerFlow：字节跳动开源 SuperAgent 编排框架，可完成数小时长时程任务](#item-5) ⭐️ 8.0/10
6. [用 Rust 重写 Postgres，借助批处理、算子融合与 SIMD 实现 300 倍分析加速](#item-6) ⭐️ 8.0/10
7. [Claude Code 2.1.224 新增自托管 Runner 并强化沙箱安全](#item-7) ⭐️ 7.0/10
8. [DeepSeek V4 Flash 0731 发布：本地推理极快、成本几乎可忽略](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Codex rust-v0.147.0 发布：新增便携插件与 MCP 2026-07-28 支持](https://github.com/openai/codex/releases/tag/rust-v0.147.0) ⭐️ 8.0/10

OpenAI 发布了 Codex rust-v0.147.0，新增了支持目录搜索的便携式 Agent 插件、持久化会话分区、--approve-for-me 标志、Cursor 技能导入，以及对 MCP 2026-07-28 协议的可选支持。该版本还修复了命令展示和回放日志中的密钥脱敏问题。 该版本为开发者提供了扩展和控制这一广泛使用的编码 Agent 的新方式，顺应了便携式插件与 MCP 标准的行业趋势。密钥脱敏修复则解决了分享或回放终端输出时的安全隐患。 在技术层面，Codex 将 MCP SDK 升级到 3.0.0、Ratatui 升级到 0.30.2、V8 升级到 150.4.0，并移除已弃用的 `--full-auto` 标志，改用 `--sandbox workspace-write`。此外还为 Amazon Bedrock 增加了缓存的网络搜索和远程会话压缩，并强化了信任与认证检查。

github · github-actions\[bot\] · 8月7日 01:41

**背景**: Codex 是 OpenAI 的命令行编码 Agent，可以在沙盒中读取和修改代码仓库。MCP（Model Context Protocol）是一个开放标准，用于将 AI 应用连接到外部工具和数据源，2026-07-28 修订版加入了分页发现和多轮请求能力。Cursor 技能是将知识打包给 AI 编码 Agent 的可复用 SKILL.md 指令文件，此次更新可让用户直接导入这些技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://cursor.com/docs/skills">Agent Skills | Cursor Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#codex`, `#coding agent`, `#MCP`, `#plugins`, `#release`

---

<a id="item-2"></a>
## [Superpowers：26.8 万星标的子代理驱动开发技能框架](https://github.com/obra/superpowers) ⭐️ 8.0/10

obra/superpowers 在 GitHub 上已获得 268,709 颗星，最近一次更新于 2026-08-07，成为采用最广泛的代理技能框架之一。该项目提供了可组合的技能库，以及一套完整的子代理驱动开发（SDD）方法论，供 AI 编码代理使用。 凭借 26.8 万颗星和活跃的开发状态，该框架代表了一种可信且有重大影响的方式来编排 AI 编码代理，直接回应了日益增长的结构化代理技能和多代理协调需求。它支持 Claude Code、Cursor、Codex、OpenCode 和 Gemini CLI 等主流 AI 编码工具，可能影响开发者构建和共享代理工作流的方式。 该仓库主要使用 Shell 编写，目前有 23,997 个复刻（fork）和 323 个未关闭的 issue，表明社区规模庞大且维护活跃。子代理驱动开发工作流会为每个任务分派全新的实现子代理，随后进行任务审查和整个分支的审查，通过隔离的代理上下文强制执行质量门禁。

github · obra · 8月7日 20:42

**背景**: Agent Skills 是一种轻量级、开放的格式，用于扩展 AI 代理的能力，每个技能是一个包含 SKILL.md 文件的文件夹，该文件包含元数据和指令。Superpowers 正是基于这一概念构建，提供可根据代理需求触发的可组合技能，并包含一套详细的 SDD 方法论，通过使用具有隔离上下文的专业子代理来提高代码质量并减少冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra/superpowers: An agentic skills framework ...</a></li>
<li><a href="https://deepwiki.com/obra/superpowers/6.6-subagent-driven-development">Subagent-Driven Development | obra/superpowers | DeepWiki</a></li>
<li><a href="https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md">superpowers/skills/subagent-driven-development/SKILL.md at ...</a></li>

</ul>
</details>

**标签**: `#ai`, `#coding-agents`, `#skills`, `#subagent-driven-development`, `#open-source`

---

<a id="item-3"></a>
## [ECC：238K 星 AI 编码代理性能优化工具](https://github.com/affaan-m/ECC) ⭐️ 8.0/10

GitHub 仓库 affaan-m/ECC 已获得 238,562 颗星，它是一个针对 AI 编码代理运行环境的性能优化系统，支持 Claude Code、Codex、Opencode、Cursor 等工具。该系统提供了包含技能、本能、记忆和安全功能的结构化框架，旨在提升代理的效率和可靠性。 该仓库获得的大量星标验证了社区对标准化代理运行环境的需求——这种环境能优化性能并为 AI 编码代理添加安全护栏。该项目可能成为开发者构建或扩展基于代理的开发工具的首选参考，影响 AI 代理在生产环境中与代码库交互的方式。 该仓库主要使用 JavaScript 编写，最近一次推送时间为 2026-08-07，目前有 125 个开放问题。其标签包括 ai-agents、claude-code、mcp 和 productivity，表明它与模型上下文协议 \(MCP\) 及现代 AI 编码工具链进行了集成。

github · affaan-m · 8月7日 21:22

**背景**: 代理运行环境 \(agent harness\) 是围绕大语言模型 \(LLM\) 的软件基础设施，负责管理工具使用、记忆、状态持久化和执行环境，将静态模型转变为有能力的代理。模型上下文协议 \(MCP\) 由 Anthropic 于 2024 年 11 月推出，标准化了 AI 系统连接外部工具和数据源的方式。代理系统中的本能 \(instincts\) 是一种前认知反射，能在任何代码变更或工具调用前执行自动安全检查，保护代码库免受意外损害。ECC 将这些概念整合到一个针对主流编码代理平台的性能优化运行环境中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://skillsmp.com/creators/itallstartedwithaidea/agent-skills/skills-claude-mythos-agent-instinct-system">agent-instinct-system Agent Skill | SkillsMP</a></li>

</ul>
</details>

**标签**: `#ai-agents`, `#claude-code`, `#mcp`, `#developer-tools`, `#performance-optimization`

---

<a id="item-4"></a>
## [Graphify 用 AST 解析把任意代码库变成可查询的知识图谱](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

Graphify 是一个新的开源工具，能把任意代码库（包括其中的文档、SQL 模式、配置文件和 PDF）通过本地确定性的 AST 解析转换成一个可查询的知识图谱。它以 /graphify 技能的形式提供给 Claude Code、Cursor、Codex 和 Gemini CLI，且无需向量存储。 Graphify 拥有超过 10.4 万个星标和约 1 万个分支，显示出社区对 AI 编码代理背后确定性、可解释代码分析工具的强烈需求。它采用“每条边都有解释、无需向量存储”的设计，为把 LLM 锚定在真实代码库上提供了一种透明、可替代基于嵌入检索的方案。 该项目用 Python 编写，并借助 tree-sitter 进行确定性的 AST 解析，其主题标签还涉及 GraphRAG、RAG 和 Leiden 社区发现算法。它以技能（skill）形式分发，兼容基于 MCP 的编码工具；仓库目前有 853 个未关闭的 issue，说明项目仍在积极开发和维护中。

github · Graphify-Labs · 8月7日 21:58

**背景**: 抽象语法树（AST）是源代码的一种结构化、确定性表示，编译器和静态分析器可以可靠地处理它，这与模糊的基于嵌入的方法形成对比。模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，用于标准化 AI 系统连接外部工具和数据源的方式。GraphRAG 是一种混合技术，利用知识图谱增强检索增强生成（RAG），与朴素的纯向量检索相比，能更好地检索实体和关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GraphRAG">GraphRAG</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tree-sitter_%28parser_generator%29">Tree-sitter (parser generator)</a></li>

</ul>
</details>

**标签**: `#code-analysis`, `#knowledge-graph`, `#developer-tools`, `#ai-agents`, `#mcp`

---

<a id="item-5"></a>
## [DeerFlow：字节跳动开源 SuperAgent 编排框架，可完成数小时长时程任务](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

字节跳动开源了 DeerFlow，这是一个 SuperAgent 编排框架，通过协调子代理、记忆、沙箱、工具、技能和消息网关，可处理从几分钟到数小时的长时程任务。该 GitHub 仓库已获得超过 7.9 万颗星标和 1 万余次 fork，且仍在持续活跃开发中。 DeerFlow 的意义在于它代表了从简单代理框架向“编排框架（harness）”的转变——即能够支撑长时间、多步骤自主工作流的运行时脚手架。对于构建 agentic 应用的 AI 开发者来说，它提供了来自大型科技公司的、面向生产且可扩展的参考实现，回应了多代理系统中常见的编排与治理难题。 DeerFlow（Deep Exploration and Efficient Research Flow 的缩写）主要以 Python 构建，支持深度研究、编码和内容创作等场景。其消息网关支持模块化的多代理协调，沙箱为安全执行提供隔离环境，并且该框架可与 LangChain、LangGraph 等生态集成。

github · bytedance · 8月7日 13:38

**背景**: 代理编排框架（agent harness）是 LLM 代理周围的运行时脚手架，通常执行 ReAct 循环：模型进行推理、通过工具调用采取行动、观察结果并重复该过程。与单纯框架不同，harness 提供了维持长时程任务所需的基础设施——记忆、沙箱、工具逻辑和子代理编排。多代理系统通常使用中央编排器进行意图路由和代理生命周期管理，DeerFlow 的消息网关也体现了这一模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bytedance/deer-flow">GitHub - bytedance/deer-flow: An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours. · GitHub</a></li>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness</a></li>
<li><a href="https://arize.com/blog/what-is-an-agent-harness/">What Is an Agent Harness? Definition &amp; How It Works</a></li>
<li><a href="https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html">Reference architecture - Multi-agent Reference Architecture</a></li>

</ul>
</details>

**标签**: `#agent-framework`, `#open-source`, `#ai-agents`, `#multi-agent`, `#python`

---

<a id="item-6"></a>
## [用 Rust 重写 Postgres，借助批处理、算子融合与 SIMD 实现 300 倍分析加速](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 8.0/10

pgrust——一个从头用 Rust 重写 PostgreSQL 的项目——的作者发布了一篇详细的技术文章，解释查询引擎如何借助批处理、算子融合和 SIMD 向量化，在分析型工作负载上实现 300 倍加速。该项目通过了 Postgres 回归测试套件中的全部 46,066 项测试。 这表明，一个从零构建的现代查询引擎可以在保持线协议和 SQL 方言兼容的同时，在 OLAP 工作负载上大幅超越成熟的 PostgreSQL 代码库。这是一项对后端及数据密集型开发具有高参考价值的工程成就，也再次引发了关于受信任的 Postgres 核心团队是否应采纳自适应规划等现代技术的讨论。 加速主要通过三种技术实现：按批处理行（向量化执行）而非逐行处理、融合算子以减少物化开销，以及使用 SIMD 指令利用数据级并行。该项目由八个并行 AI 编码代理构建，与 Postgres 保持线协议和 SQL 方言兼容，并以正确性为最高优先级，通过形式化验证和差分模糊测试覆盖 1,000 多个用户可见函数来保障。

hackernews · poly2it · 8月7日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**背景**: PostgreSQL 是一个用 C 语言编写的成熟、久经考验的关系型数据库，但它经典的逐行（Volcano 风格）查询执行模型对分析型工作负载效率不高。ClickHouse、QuestDB 等分析型数据库采用向量化执行，即每次调用让算子按列批量处理值，从而最大化 CPU 缓存效率并支持 SIMD。&#x27;松耦合算子融合&#x27;（relaxed operator fusion）是一项相关研究技术，允许数据库管理系统在查询计划中暂存中间结果，以结合编译、向量化和预取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now ...</a></li>
<li><a href="https://betterstack.com/community/guides/databases/pgrust-postgres/">PGRust: A Rust Rewrite of PostgreSQL That Passes All ...</a></li>
<li><a href="https://clickhouse.com/resources/engineering/vectorized-query-execution">What is vectorized query execution?</a></li>

</ul>
</details>

**社区讨论**: 作者强调正确性是最高优先级，并提到通过形式化验证和差分模糊测试证明了 1,000 多个用户可见函数与 Postgres 逻辑一致。评论者担心由官方 Postgres 团队之外的机构构建的重写版本在可信度、长期维护与连续性方面的问题；一位用户对自适应规划终于被证明可行感到兴奋，另一位则询问将 pgrust 嵌入二进制能否让它成为 SQLite/Turso 的替代品。

**标签**: `#postgres`, `#rust`, `#query-engine`, `#performance`, `#analytics`

---

<a id="item-7"></a>
## [Claude Code 2.1.224 新增自托管 Runner 并强化沙箱安全](https://github.com/anthropics/claude-code/releases/tag/v2.1.224) ⭐️ 7.0/10

Claude Code v2.1.224 引入了 `claude self-hosted-runner` 命令，让 Team 和 Enterprise 用户可以在自己的机器或容器上运行云端会话。该版本还增加了 `archive` 插件来源，支持通过 HTTPS 托管的 zip 文件安装插件并可选 SHA-256 固定，同时新增了沙箱凭据掩码选项。 自托管 Runner 让组织能够更灵活地控制编码代理的运行位置，解决了团队扩大 Claude Code 使用规模时的数据驻留和合规性问题。archive 插件来源和更严格的凭据掩码也提升了供应链安全，降低了代理运行期间机密泄露的风险。 新的凭据掩码功能需要启用 `network.tlsTerminate`，并且仅从用户、托管或 `--settings` 设置中生效；这些选项包括通过 `decode: &quot;jwt&quot;` 配合 `maskClaims` 进行 JWT 感知掩码，以及用于 AWS SigV4 重新签名的 `awsPairs`/`sigv4`。此版本还修复了 Linux 和 macOS 上以尾部斜杠结尾的 deny 条目可被静默绕过的沙箱漏洞，并取消了每个会话 200 个子代理的生成上限。

github · ashwin-ant · 8月7日 04:00

**背景**: Claude Code 是 Anthropic 推出的命令行编码代理，可以编辑代码、运行命令并自动执行开发任务。通过 `claude self-hosted-runner` 启动的自托管环境，让组织可以在自己运营的基础设施上运行来自 Web、移动端、桌面或计划任务的 Claude Code 云端会话，而不是在 Anthropic 的云上运行；但这并非完全自托管的 Claude 技术栈。archive 插件来源为 git 或 npm 安装提供了另一种选择，使受限环境中的插件分发更加容易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/ahab_indieseek/claude-code-21224-self-hosted-environments-checklist-2ck9">Claude Code 2.1.224 Self - Hosted Environments... - DEV Community</a></li>
<li><a href="https://claudcod.com/blog/claude-code-self-hosted-runner/">Claude Code Self - Hosted Runner : Own Infra Guide | Claude Code Blog</a></li>
<li><a href="https://dev.classmethod.jp/en/articles/20260807-cc-updates-v2-1-224/">Claude Code v2.1.224 Major Updates - Self - Hosted Environments and...</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#coding agents`, `#release notes`, `#developer tools`, `#enterprise`

---

<a id="item-8"></a>
## [DeepSeek V4 Flash 0731 发布：本地推理极快、成本几乎可忽略](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 7.0/10

DeepSeek 正式发布了 DeepSeek-V4-Flash-0731，取代了此前的预览版，显著增强了智能体（agentic）能力。社区实测报告显示其本地推理速度很快（在 2x RTX Pro 6000 Blackwell 上预填充约 8k tok/s、解码 250+ tok/s），且运营成本几乎可忽略（重度使用下每天约 $5）。 这一发布意义重大，因为它将广泛的智能体能力与异常快速的本地推理和近乎为零的成本结合，使个人开发者和小团队也能切实使用强大的推理能力。它还带有 ARC-AGI 基准评测链接，使其处于关于推理能力和 AGI 进展的持续讨论之中。 该模型采用稀疏混合专家（MoE）架构，总参数 284B，其中激活参数仅 13B，API 定价为每百万输入 token $0.09、每百万输出 token $0.18。社区报告指出，高峰时段价格会翻倍，且高峰时段按中国时区定义；部分用户还遇到模型陷入死循环或工具调用失败的问题。

hackernews · tosh · 8月7日 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

**背景**: DeepSeek V4 Flash 是 DeepSeek 推出的快速、高性价比模型档位，在预览版之后迎来了 0731 正式版。ARC-AGI 基准通过视觉网格谜题衡量模型的流体智力和新颖抽象推理能力，其下一代版本 ARC-AGI-2 旨在对当前最先进的推理系统进行压力测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek-ai/DeepSeek-V4-Flash-0731 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash-0731">DeepSeek V4 Flash 0731 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/deepseek-v4-flash">DeepSeek V4 Flash 0731 (max) - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://arcprize.org/arc-agi/2">ARC-AGI-2</a></li>

</ul>
</details>

**社区讨论**: 社区整体评价较为正面，用户称赞该模型的速度、低成本以及在调试和文档/数据分析方面的强大能力。但也有用户反映一些问题，包括模型陷入死循环、自言自语而不执行工具调用，以及高峰时段定价按中国时区定义等。

**标签**: `#DeepSeek V4`, `#model-release`, `#ARC-AGI`, `#local-inference`, `#benchmark`

---