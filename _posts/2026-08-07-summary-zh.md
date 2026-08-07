---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 84 条内容中筛选出 5 条重要资讯。

---

1. [超级力量：268k 星的开源代理技能框架与软件开发方法论](#item-1) ⭐️ 8.0/10
2. [Anthropic 的智能体技能仓库在 GitHub 上获 16.6 万星](#item-2) ⭐️ 8.0/10
3. [Graphify：将代码库转为可查询知识图谱，无需向量存储](#item-3) ⭐️ 8.0/10
4. [Agent Skills 仓库：为 AI 编码代理提供生产级技能集](#item-4) ⭐️ 8.0/10
5. [Datasette 1.0a38 修复混合权限表的 SQL 注入漏洞](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [超级力量：268k 星的开源代理技能框架与软件开发方法论](https://github.com/obra/superpowers) ⭐️ 8.0/10

开源仓库 obra/superpowers 在 GitHub 上获得了 268,111 颗星，提供了一个用于 AI 辅助编码的代理技能框架和软件开发方法论。它引入了一种名为“子代理驱动开发”的结构化方法，通过自动化的审查循环将任务分派给新的子代理。 如此大规模的采用表明社区对一种实用的、代理式的软件开发方法给予了强有力的认可。该框架可能重塑开发者将 AI 代理集成到其软件开发生命周期中的方式，通过模块化技能和自主子代理来提升速度和质量。 该仓库主要使用 Shell 编写，拥有 23,964 个分支和 322 个开放问题，最近一次推送是在 2026 年 8 月 7 日。它涵盖的主题包括 AI、编码、SDLC 和子代理驱动开发，并且设计为与多种 AI 编码代理兼容。

github · obra · 8月7日 00:29

**背景**: 代理技能是轻量级的模块化包（通常是一个包含指令的 SKILL.md 文件），用于扩展 AI 代理在特定任务上的能力。子代理驱动开发是一种结构化执行框架，它将复杂任务分解为独立的子单元，每个子单元由一个新的子代理处理，并带有自动化的规格和质量审查循环。该仓库将这些概念整合成一个连贯的 AI 辅助软件工程方法论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://myclaw.ai/skills/subagent-driven-development">Subagent - Driven Development on MyClaw</a></li>
<li><a href="https://techcommunity.microsoft.com/blog/appsonazureblog/an-ai-led-sdlc-building-an-end-to-end-agentic-software-development-lifecycle-wit/4491896">An AI led SDLC: Building an End-to-End Agentic Software Development Lifecycle with Azure and GitHub. | Microsoft Community Hub</a></li>

</ul>
</details>

**标签**: `#agentic-framework`, `#AI-development`, `#SDLC`, `#open-source`, `#GitHub`

---

<a id="item-2"></a>
## [Anthropic 的智能体技能仓库在 GitHub 上获 16.6 万星](https://github.com/anthropics/skills) ⭐️ 8.0/10

Anthropic 的智能体技能（Agent Skills）公开仓库在 GitHub 上获得了 166,720 颗星，成为该平台上最受关注的 AI 项目之一。该仓库提供了一种轻量级、开放的格式，用于通过专业知识和工作流扩展 AI 智能体的能力。 如此大规模的社区认可表明，对标准化、可复用的智能体技能有着强烈需求，这些技能能将通用 AI 智能体转变为领域专家。这为新兴的智能体生态设定了事实标准，影响了开发者构建和共享智能体能力的方式。 该仓库使用 Python 编写，截至最新推送已累计 19,855 个 fork 和 1,067 个未解决问题。一个技能被定义为包含 SKILL.md 文件的文件夹，遵循渐进式披露模式，使智能体仅加载所需上下文。

github · anthropics · 7月24日 20:12

**背景**: 智能体技能（Agent Skills）是指令、脚本和资源的结构化包，赋予 AI 智能体特定能力和领域知识。它们遵循开放规范并实现渐进式披露模式，让智能体在需要时仅加载所需上下文。这个概念类似于 AI 智能体的可插拔模块，使开发者能够创建和共享可复用的技能包。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/skills">GitHub - anthropics/skills: Public repository for Agent Skills · GitHub</a></li>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://learn.microsoft.com/en-us/agent-framework/agents/skills">Agent Skills | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#Anthropic`, `#AI agents`, `#developer tools`, `#GitHub`

---

<a id="item-3"></a>
## [Graphify：将代码库转为可查询知识图谱，无需向量存储](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

Graphify-Labs/graphify 是一个新开源项目（已获 103,535 颗星），它通过 Tree-sitter 进行确定性 AST 解析，将任意代码库及其文档、SQL 模式、配置和 PDF 文件转换为可查询的知识图谱，并可作为 Claude Code、Cursor、Codex 和 Gemini CLI 的技能使用，无需向量存储。 这种方法为基于嵌入的代码理解提供了一种确定性和可解释的替代方案，后者通常不透明且资源密集。通过与流行的 AI 编码助手直接集成，Graphify 能显著改善开发者搜索、调试和理解大型代码库的方式。 Graphify 使用 Tree-sitter 进行本地 AST 解析，并采用 Leiden 算法进行社区检测，支持 GraphRAG 风格的检索，同时保持确定性边。它没有向量存储，确保代码元素之间的每个连接都是可解释且可重现的。

github · Graphify-Labs · 8月6日 16:45

**背景**: Tree-sitter 是一个开源解析器生成器，可为源代码生成具体的语法树（AST），实现快速增量解析。Leiden 算法是一种社区检测算法，用于优化网络中的模块化度，常被用来识别知识图谱中的聚类。GraphRAG 是一种检索增强生成方法，它使用知识图谱而非向量嵌入来为大语言模型提供上下文。Graphify 结合了这些技术，在不依赖不透明的向量嵌入的情况下，为代码库创建了一个结构化的、可查询的表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tree-sitter_%28parser_generator%29">Tree-sitter (parser generator) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leiden_algorithm">Leiden algorithm - Wikipedia</a></li>
<li><a href="https://neo4j.com/blog/genai/what-is-graphrag/">What is GraphRAG? - Neo4j Graph Intelligence Platform</a></li>

</ul>
</details>

**标签**: `#knowledge-graph`, `#code-analysis`, `#ai-agents`, `#developer-tools`, `#ast`

---

<a id="item-4"></a>
## [Agent Skills 仓库：为 AI 编码代理提供生产级技能集](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

GitHub 上的 addyosmani/agent-skills 仓库已获得超过 82,000 个星标，为 Claude Code、Codex 和 Cursor 等 AI 编码代理提供了一套生产级工程技能集合。 高星标数量反映了社区的强烈认可和实用价值，表明标准化的代理技能能够显著提升 AI 编程工具生态中开发者的生产力和代码质量。 该仓库主要使用 JavaScript 编写，拥有 8,896 个复刻和 100 个开放问题，话题标签包括 antigravity、claude-code、codex、cursor 和 skills。最近一次推送是在 2026 年 8 月 6 日。

github · addyosmani · 8月6日 22:45

**背景**: Claude Code、Codex 和 Cursor 等 AI 编码代理通过理解代码库、编辑文件、运行命令以及根据自然语言指令完成多步编程任务来帮助开发者。“Agent Skills”概念是一种轻量级、开放格式，通过专业知识和工作流扩展代理能力，通常在一个文件夹中通过 SKILL.md 文件定义。此仓库收集了这些用于生产环境的技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_%28code_editor%29">Cursor (code editor)</a></li>
<li><a href="https://agentskills.io/">Agent Skills Overview - Agent Skills</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#AI coding agents`, `#claude-code`, `#codex`, `#cursor`

---

<a id="item-5"></a>
## [Datasette 1.0a38 修复混合权限表的 SQL 注入漏洞](https://simonwillison.net/2026/Aug/6/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a38 修复了一个 SQL 注入漏洞，该漏洞允许拥有任意公共表访问权限的用户，即使在禁用 execute-sql 权限的情况下，也能读取同一数据库中的私有表。此修复同样适用于 Datasette 0.65.3。 此安全修复对于在同一 Datasette 实例中同时暴露公共表和私有表的管理员至关重要，因为它堵住了未授权数据访问的路径。尽管这种混合配置较为罕见，但若不及时修补，漏洞可能导致数据泄露。 该漏洞要求 Datasette 实例在同一数据库中同时提供公共表和私有表，并通过 Datasette 权限系统配置访问。修复的漏洞允许在数据库上限制 execute-sql 权限的情况下仍能发起 SQL 注入攻击。

rss · Simon Willison · 8月6日 18:24

**背景**: Datasette 是一个开源工具，用于将数据探索和发布为交互式网站和 API。它包含一个权限系统，用于控制对数据库、表和查询的访问。execute-sql 权限专门控制用户是否可以运行任意 SQL 查询。该漏洞存在于当同一数据库中存在不同访问级别的多个表时，权限与 SQL 执行引擎之间的交互中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and ...</a></li>
<li><a href="https://docs.datasette.io/en/stable/authentication.html">Authentication and permissions - Datasette documentation</a></li>
<li><a href="https://simonwillison.net/2025/Nov/4/datasette-10a20/">A new SQL-powered permissions system in Datasette 1.0a20</a></li>

</ul>
</details>

**标签**: `#datasette`, `#security`, `#sql injection`, `#release`

---