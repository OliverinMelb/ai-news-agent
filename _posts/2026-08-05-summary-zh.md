---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 88 条内容中筛选出 6 条重要资讯。

---

1. [Matt Pocock 的 Skills 仓库：超 20 万星，为工程师打造的实用 AI 技能](#item-1) ⭐️ 8.0/10
2. [Graphify 将代码库转为可查询知识图谱](#item-2) ⭐️ 8.0/10
3. [Agent Skills：为 AI 编码代理提供生产级工程技能](#item-3) ⭐️ 8.0/10
4. [Deer Flow：79k 星开源超级代理，专攻长周期任务](#item-4) ⭐️ 8.0/10
5. [Cloudflare OS：AI 智能体与应用的开源平台](#item-5) ⭐️ 8.0/10
6. [LLM 0.32 新增推理轨迹、服务端工具和 OpenAI Responses API 支持](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Matt Pocock 的 Skills 仓库：超 20 万星，为工程师打造的实用 AI 技能](https://github.com/mattpocock/skills) ⭐️ 8.0/10

Matt Pocock 的 skills 仓库在 GitHub 上获得了 204,894 颗星，提供了一套可复用的代理技能，专为实际工程任务设计。这些技能可以直接通过 Claude Code 的市场或使用 npx 命令一键安装。 该仓库展示了工程师对标准化、实用型代理技能日益增长的需求，填补了 AI 代理能力与日常开发者工作流之间的空白，有望加速 AI 编码助手的普及。 该仓库主要使用 Shell 语言编写，拥有 17,681 个 fork 和 281 个未解决问题。它已列入 Claude Code 的官方市场，支持自动更新。

github · mattpocock · 8月5日 18:10

**背景**: 代理技能（Agent Skills）是一种轻量级、可移植的指令、脚本和资源包，用于扩展 AI 代理的能力。这种开放格式通过一个 SKILL.md 文件定义，允许 Claude Code 和 Codex 等代理按需发现和加载技能。该仓库实现了这一格式，包含由 Matt Pocock 为实际工程任务精选的技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mattpocock/skills">mattpocock /skills: Skills for Real Engineers. Straight from my . agents ...</a></li>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://www.skills.sh/">Discover and install skills for AI agents .</a></li>

</ul>
</details>

**标签**: `#agents`, `#skills`, `#developer-tools`, `#ai`, `#github`

---

<a id="item-2"></a>
## [Graphify 将代码库转为可查询知识图谱](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

Graphify 是一个新的开源工具，它利用确定性 AST 解析将任意代码库转换为可查询的知识图谱，并集成了 Claude Code、Cursor、Codex 和 Gemini CLI。截至 2026 年 8 月，该项目在 GitHub 上已获得超过 10.3 万颗星。 该工具为基于向量的代码搜索提供了一种确定性替代方案，使 AI 智能体能够更准确地理解代码结构和关系。它有望显著改善代码分析、自动调试和 AI 辅助的软件开发工作流程。 Graphify 使用 tree-sitter 进行 AST 解析，采用 Leiden 算法进行知识图谱中的社区检测，并支持模型上下文协议（MCP）以便与 AI 智能体集成。它不仅能处理源代码，还能导入文档、SQL 模式、配置文件和 PDF。

github · Graphify-Labs · 8月5日 21:12

**背景**: 知识图谱是捕获实体及其关系的结构化表示，能够比纯文本实现更精确的查询。AST 解析分析代码的语法结构，提供了一种不依赖嵌入的确定性代码理解方式。Leiden 算法是一种广泛应用于大型网络的社区检测方法，而 GraphRAG 是将知识图谱与检索增强生成相结合的混合方法。由 Anthropic 引入的模型上下文协议（MCP）标准化了 AI 模型连接外部工具和数据源的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Leiden_algorithm">Leiden algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/GraphRAG">GraphRAG</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#knowledge-graph`, `#code-analysis`, `#AI-agents`, `#developer-tools`, `#AST-parsing`

---

<a id="item-3"></a>
## [Agent Skills：为 AI 编码代理提供生产级工程技能](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani 的 GitHub 仓库 &#x27;agent-skills&#x27; 已获得超过 81,900 颗星，为 Claude Code、Codex、Cursor 等 AI 编码代理提供了一套生产级工程技能集合。 这个开源项目将资深工程师使用的工作流和最佳实践标准化，使 AI 编码代理能够在开发各阶段遵循一致、高质量的工程模式。其大规模采用表明，AI 编码生态系统中对可检查、可复用的技能库的需求正在增长。 该仓库使用 JavaScript 编写，最近更新于 2026 年 8 月 5 日，目前有 148 个未解决问题。它支持多种工具，包括 Claude Code、Codex、Cursor 和 Antigravity，并明确为 AI 代理编码了质量门禁和最佳实践。

github · addyosmani · 8月5日 19:09

**背景**: 像 Claude Code 和 Cursor 这样的 AI 编码代理可以自主编辑代码、运行命令和管理项目。然而，如果没有明确的指导，它们可能会产生不一致或低质量的结果。此处的“技能”是打包的工作流，编码了资深开发者的工程实践，确保 AI 代理遵循经过验证的模式，如测试、代码审查和安全重构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">Production-grade engineering skills for AI coding agents.</a></li>
<li><a href="https://pinggy.io/blog/ai_agent_skills/">What Are Skills in AI Agents? Top 14 Skills You Must Know in 2026</a></li>
<li><a href="https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051">10 Must-Have Skills for Claude (and Any Coding Agent) in 2026</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#AI coding agents`, `#GitHub`, `#Claude Code`, `#Codex`

---

<a id="item-4"></a>
## [Deer Flow：79k 星开源超级代理，专攻长周期任务](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

字节跳动的 Deer Flow 是一个开源的长周期超级代理框架，已在 GitHub 上获得超过 79,000 颗星。它通过沙箱、记忆、工具、技能、子代理和消息网关，为代理提供研究、编码和创作的能力。 凭借庞大的采用量和可信组织的支持，Deer Flow 表明行业对能够处理复杂多步骤任务的长周期 AI 代理的需求日益增长。它为开发者构建自主研究和编码工作流提供了一个实用、可审查的基础。 该框架支持 Python 和 TypeScript，并与 LangGraph、LangChain 和 LangManus 集成。它旨在处理需要数分钟到数小时的任务，使用子代理执行专门的子任务，并通过消息网关实现代理间通信。

github · bytedance · 8月5日 09:57

**背景**: 长周期任务是指需要许多连续步骤、决策和动作（通常数十到数百个）才能达到最终结果的目标。子代理是专门的辅助 AI，主代理可将任务委派给它们，在单独的上下文中进行专注工作。LangGraph 是一个基于图的编排框架，用于构建可靠的多代理 AI 工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/langgraph">What is LangGraph ? | IBM</a></li>
<li><a href="https://www.altexsoft.com/blog/subagents/">What Are Subagents ? When to Use Them and Why</a></li>
<li><a href="https://www.ai21.com/glossary/ai-agent/what-are-long-horizon-tasks/">What are Long-Horizon Tasks? | AI21</a></li>

</ul>
</details>

**标签**: `#agentic-framework`, `#multi-agent`, `#open-source`, `#AI`, `#superagent`

---

<a id="item-5"></a>
## [Cloudflare OS：AI 智能体与应用的开源平台](https://blog.cloudflare.com/cloudflare-os/) ⭐️ 8.0/10

Cloudflare 发布了 Cloudflare OS，这是一个基于 Workers 构建的开源平台，允许开发者创建 AI 智能体和应用程序。该平台复兴了十年前 Sandstorm 的概念，并深度融合了 AI 技术。 这标志着 Cloudflare 在将其边缘计算平台定位为 AI 智能体开发基础方面迈出了重要一步。它可能降低构建自定义 AI 驱动工作流和工具的门槛，直接与其他智能体平台竞争。 Cloudflare OS 是开源的，已在 GitHub 上发布。它直接使用 pi-agent 而非 Cloudflare 自家的 Agents SDK，这引发了开发者社区对设计选择的疑问。

hackernews · speckx · 8月5日 13:58 · [社区讨论](https://news.ycombinator.com/item?id=49182996)

**背景**: Cloudflare Workers 是一个无服务器计算平台，可在 Cloudflare 的全球边缘网络上运行代码。Sandstorm 是一个开创性的开源项目，用于自托管 Web 应用程序，由 Kenton Varda 领导，他现在是 Cloudflare Workers 的首席开发者。Cloudflare OS 旨在将 Sandstorm 的简洁性带入 AI 智能体时代，允许用户在边缘运行和管理 AI 驱动的应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://os.cloudflare.app/">Cloudflare OS</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-os">GitHub - cloudflare / cloudflare - os : Agent workspace built on...</a></li>
<li><a href="https://sandstorm.io/">Sandstorm</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论既有兴趣也有怀疑。一些开发者质疑为何使用 pi-agent 而非 Cloudflare 自家的 Agents SDK。另一些人表达了对供应商锁定的担忧，还有少数人批评“OS”这个品牌名称具有误导性。

**标签**: `#Cloudflare`, `#agents`, `#open platform`, `#developer tools`, `#AI`

---

<a id="item-6"></a>
## [LLM 0.32 新增推理轨迹、服务端工具和 OpenAI Responses API 支持](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32 于 2026 年 8 月 4 日发布，新增了推理模型的可见推理轨迹显示、服务端工具（如 CodeInterpreter 和 WebSearch）集成，以及 OpenAI Responses API 支持，并将 GPT-5.6 Luna 设为默认模型。 此次更新大幅提升了 LLM 命令行工具对开发者的能力，允许直接观察推理过程并在提示中执行代码或网络搜索，从而简化了 AI 驱动的自动化和分析工作流程。 新增的 -R/--hide-reasoning 标志可抑制标准错误中的推理轨迹，而 llm openai endpoint 命令允许对任何兼容 OpenAI 的端点执行一次性提示且不记录日志。

rss · Simon Willison · 8月4日 23:58

**背景**: LLM 是一个开源命令行工具，用于与各种提供商的 LLM 进行交互。推理轨迹是模型在解决复杂问题时产生的中间步骤，现在通过 stderr 单独显示。服务端工具是由模型 API 提供的内置功能，如代码执行或网络搜索，模型可在生成过程中调用这些工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/aug/4/new-release-of-llm/">New release of LLM adds support for reasoning traces, OpenAI...</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://www.oflight.co.jp/en/columns/llm-cli-032-release-guide-2026-08">LLM 0 . 32 : New CLI Reasoning Traces &amp; Server-Side Tools | Oflight Inc.</a></li>

</ul>
</details>

**标签**: `#LLM`, `#CLI`, `#OpenAI Responses API`, `#reasoning traces`, `#developer tools`

---