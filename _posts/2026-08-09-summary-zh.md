---
layout: default
title: "Horizon Summary: 2026-08-09 (ZH)"
date: 2026-08-09
lang: zh
---

> 从 61 条内容中筛选出 4 条重要资讯。

---

1. [Graphify 把任意代码库变成编码代理可查询的知识图谱](#item-1) ⭐️ 8.0/10
2. [Agent Skills 仓库获 85k 星，为 AI 编码代理提供生产级技能](#item-2) ⭐️ 8.0/10
3. [一个 AI 技能，可跨 Reddit、X、YouTube、HN、Polymarket 研究任意主题](#item-3) ⭐️ 8.0/10
4. [PrivateGPT 提供完整 API 层，在本地模型上构建支持 RAG 和 MCP 的私有 AI 应用](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Graphify 把任意代码库变成编码代理可查询的知识图谱](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

Graphify 是一个最近仍在维护的开源 Python 项目，拥有超过 10.4 万 GitHub star，可将任意代码库（包括文档、SQL schema、配置和 PDF）转换为确定性的、可查询的知识图谱。它以 /graphify 技能的形式提供给 Claude Code、Cursor、Codex 和 Gemini CLI，使用本地 AST 解析且无需向量存储。 这件事意义重大，因为它为基于大模型的编码代理提供了代码库的结构化图谱表示，在不依赖向量嵌入的情况下改善代码搜索与推理能力。该项目获得 10.4 万 star，说明开发者社区对 AI 开发工具中确定性、可解释的代码分析有强烈需求。 该工具使用 Tree-sitter 进行增量解析以构建具体语法树，支持基于图谱的 RAG（GraphRAG），并结合 Leiden 算法对生成的图进行社区检测。它主要以 Python 编写，以 skill/MCP 集成的形式提供。

github · Graphify-Labs · 8月9日 22:25

**背景**: Tree-sitter 是一个开源解析器生成器，能够生成具体语法树并支持增量解析，广泛用于文本编辑器和代码分析。GraphRAG 是一种检索增强生成技术，它将文档组织为知识图谱而非向量嵌入，帮助大语言模型理解复杂关系。Leiden 算法是一种社区检测方法，通过优化模块度来识别网络中连接紧密的节点群组。Graphify 将这三者结合起来，让 AI 编码代理能够查询代码库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tree-sitter_%28parser_generator%29">Tree-sitter (parser generator)</a></li>
<li><a href="https://www.datacamp.com/tutorial/graphrag">GraphRAG: Graph-Based Retrieval-Augmented Generation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leiden_algorithm">Leiden algorithm</a></li>

</ul>
</details>

**标签**: `#ai-agents`, `#knowledge-graph`, `#code-analysis`, `#mcp`, `#developer-tools`

---

<a id="item-2"></a>
## [Agent Skills 仓库获 85k 星，为 AI 编码代理提供生产级技能](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani 的 agent-skills 仓库在 GitHub 上获得超过 85,000 颗星，成为 Claude Code、Codex、Cursor 等 AI 编码代理最受欢迎的生产级技能集合之一。 这些技能封装了高级工程师使用的工作流、质量门控和最佳实践，使 AI 代理能够在开发各阶段一致地遵循高质量流程，从而显著提升开发效率和代码质量。 该仓库主要使用 JavaScript 编写，拥有 9,155 个 fork 和 105 个未解决问题，主题包括 antigravity（Google 的代理开发平台）。技能是可复用的指令包，涵盖代码审查、重构、文档、安全分析等。

github · addyosmani · 8月8日 21:05

**背景**: Agent skills 是可复用的指令包，用于教导 AI 编码代理如何执行特定任务，如代码审查、重构或浏览器自动化。在 Claude Code、Codex CLI、Cursor 等环境中，技能指导代理遵循结构化工作流。Google Antigravity 与 Gemini 3 一同发布，是一个基于 VS Code 分支的代理开发平台，允许代理自主规划和执行复杂软件任务。agent-skills 仓库提供了生产级技能，可与这些平台配合使用，以强制执行工程最佳实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">GitHub - addyosmani/agent-skills: Production-grade ...</a></li>
<li><a href="https://pinggy.io/blog/ai_agent_skills/">What Are Skills in AI Agents? Top 14 Skills You Must Know in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#AI coding agents`, `#Claude Code`, `#Codex`, `#developer tools`

---

<a id="item-3"></a>
## [一个 AI 技能，可跨 Reddit、X、YouTube、HN、Polymarket 研究任意主题](https://github.com/mvanhorn/last30days-skill) ⭐️ 8.0/10

GitHub 仓库 mvanhorn/last30days-skill 已获得 57,752 颗星和 5,017 次 fork，它是一个开源 AI 技能，可跨 Reddit、X、YouTube、Hacker News、Polymarket 和网络研究任意主题，并生成有依据的总结。该仓库最近一次推送时间为 2026-08-09，表明项目仍在积极维护中。 对于构建智能体研究流程的 AI 开发者来说，这个技能将多个平台上的社交媒体和市场数据收集整合到一个可复用的包中，减少了编写自定义爬虫或 API 集成的需求。其庞大的星标数量表明，在 Claude Code 和 OpenClaw 生态中，对现成且可溯源的研究技能有着强烈需求。 该仓库使用 Python 编写，带有 ai-prompts、deep-research、openclaw、clawhub、claude-code、recency 以及众多平台相关标签，目前有 118 个未关闭的问题。它对 ClawHub/OpenClaw 的适配表明，它可以作为 AgentSkills 包分发，并通过智能体平台调用。

github · mvanhorn · 8月9日 18:44

**背景**: AI 技能是可复用的提示词、工具和指令集合，用于扩展 AI 智能体。Claude Code 是 Anthropic 推出的 AI 编程助手，可以在开发工作流中使用这类技能；而 OpenClaw 是一个开源自主 AI 智能体，在本地运行并通过消息平台进行交互。ClawHub 是 OpenClaw 智能体的技能注册表和市场。名称中的“last 30 days”表明该技能强调近期帖子和实时趋势发现，而不是长期的通用网页搜索结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw</a></li>
<li><a href="https://clawhub.ai/">ClawHub — a fast skill registry for agents, with vector search.</a></li>

</ul>
</details>

**标签**: `#AI skill`, `#Claude Code`, `#research`, `#agent`, `#Python`

---

<a id="item-4"></a>
## [PrivateGPT 提供完整 API 层，在本地模型上构建支持 RAG 和 MCP 的私有 AI 应用](https://github.com/zylon-ai/private-gpt) ⭐️ 8.0/10

PrivateGPT 是一个拥有超过 57,000 个 GitHub 星标的 Python 开源项目，目前提供完整的 API 层，用于在本地模型上构建私有 AI 应用，支持 RAG、技能、工具、MCP 以及 text-to-sql。它兼容任何 OpenAI 兼容的推理服务器，为自托管 AI 提供了灵活的底座。 这一项目意义重大，因为它让开发者能够构建自托管、保护隐私的 AI 应用，无需将敏感数据发送到外部云服务商，这对企业和受监管行业至关重要。其高关注度与活跃维护表明，市场对本地部署、本地模型 AI 工具有着强劲而持续的需求。 该仓库拥有 7,608 个 fork 且仅有 3 个未关闭的 issue，说明代码库健康且维护活跃。它支持任何 OpenAI 兼容的服务器，使开发者可以灵活地对本地模型或第三方推理后端运行 PrivateGPT。

github · zylon-ai · 8月6日 13:41

**背景**: PrivateGPT 是本地优先 AI 这一大趋势的一部分。RAG（检索增强生成）通过连接外部知识库来改进大语言模型的回答；而 MCP（模型上下文协议）由 Anthropic 于 2024 年 11 月提出，旨在标准化 AI 系统与外部工具和数据源的集成方式。PrivateGPT 所提供的功能正建立在这些技术之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#private-gpt`, `#rag`, `#mcp`, `#local-models`, `#open-source`

---