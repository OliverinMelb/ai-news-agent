---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 91 条内容中筛选出 12 条重要资讯。

---

1. [Superpowers 框架为 AI 编码代理带来子代理驱动开发](#item-1) ⭐️ 9.0/10
2. [把代码库变成 AI 智能体可查询的知识图谱，无需向量库](#item-2) ⭐️ 8.0/10
3. [agent-skills 仓库为 AI 编程代理提供 19 个生产级技能](#item-3) ⭐️ 8.0/10
4. [Agent 优先控制平面发布 2,005+ Skills，支持 CLI、MCP 与插件](#item-4) ⭐️ 8.0/10
5. [Gemini 3.7 Flash：可调思考级别与增强视觉能力](#item-5) ⭐️ 8.0/10
6. [Spaghettifying DRAM 攻击解锁 AMD Jaguar 处理器隐藏功能](#item-6) ⭐️ 8.0/10
7. [DeepSeek 开源 Harness 智能体框架，支持全量可追踪会话日志](#item-7) ⭐️ 8.0/10
8. [GPT-5.6 新增 Responses API 能力，助力构建高性价比 AI 智能体](#item-8) ⭐️ 8.0/10
9. [OpenAI 预览 Ultrafast 服务层：GPT-5.6 Sol 速度提升 14 倍](#item-9) ⭐️ 8.0/10
10. [Hugging Face 重现 2200 篇 ICML 论文，发现可重复性差距](#item-10) ⭐️ 8.0/10
11. [DeepSeek V4 Pro 0813（在 OpenRouter 上）](#item-11) ⭐️ 8.0/10
12. [JetBrains 基准测试暴露输入浪费，Caveman 重构为本地代理](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Superpowers 框架为 AI 编码代理带来子代理驱动开发](https://github.com/obra/superpowers) ⭐️ 9.0/10

obra/superpowers 仓库已获得超过 27.1 万星标，成为广受欢迎的开源智能体技能框架与软件开发方法论。它通过一组可组合的技能和初始指令，让 Claude Code、Cursor、Codex、OpenCode、Gemini CLI 等 AI 编码代理遵循这套方法论工作。 这代表了从临时提示词转向结构化、方法论驱动的智能体开发的重要趋势。超过 27.1 万的星标表明社区对可重复工作流的强烈需求，这类工作流能显著提升 AI 编码代理的速度、质量和一致性。 该框架的核心是子代理驱动开发（SDD），即为每个任务派发全新的实现子代理，随后进行任务审查（规格符合性 + 代码质量），最后进行全分支审查。该仓库主要使用 Shell 编写，最近一次推送时间为 2026-08-13，目前有 328 个未关闭问题。

github · obra · 8月13日 00:36

**背景**: 智能体软件开发（Agentic software development）指使用 AI 代理（又称 TuringBots）在软件开发生命周期的多个阶段进行规划、生成、修改、测试和解释软件制品。Agent Skills 是可移植的指令、脚本和资源包，代理可按需发现并加载，从而在简单提示之外扩展代理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra/superpowers: An agentic skills framework ...</a></li>
<li><a href="https://grokipedia.com/page/Superpowers_agentic_skills_framework">Superpowers (agentic skills framework)</a></li>
<li><a href="https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development">superpowers/skills/subagent-driven-development at main · obra ...</a></li>

</ul>
</details>

**标签**: `#agentic-ai`, `#skills-framework`, `#sdlc`, `#ai-agents`, `#github`

---

<a id="item-2"></a>
## [把代码库变成 AI 智能体可查询的知识图谱，无需向量库](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

Graphify 是一个开源的 Python 工具，能把整个代码库（包括文档、SQL 模式、配置和 PDF）转换成 AI 编码智能体可查询的知识图谱。它采用确定性的 AST 解析，每条边都有解释，并以 /graphify 技能的形式提供给 Claude Code、Cursor、Codex 和 Gemini CLI，且无需向量库。 这很重要，因为它为代码理解提供了一种确定性、可解释的替代方案，取代基于向量的检索——而后者正日益成为 AI 编码智能体的瓶颈。凭借 10.6 万星标以及对主流编码智能体的集成，它反映出开发者对精确、可感知依赖关系的代码上下文的强烈需求。 该工具利用 tree-sitter 进行 AST 解析，并使用 Leiden 算法进行社区检测，同时集成了 MCP（模型上下文协议）和类 GraphRAG 的工作流。目前它有 920 个未关闭的 issue 和 10,329 个 fork，截至 2026 年 8 月仍在积极开发中。

github · Graphify-Labs · 8月13日 14:15

**背景**: 知识图谱把实体及其关系表示为节点和边，从而实现结构化、可解释的查询。GraphRAG 通过从文本中提取知识图谱来改进检索增强生成，而 Leiden 算法则用于在图中发现社区结构。MCP 是 Anthropic 于 2024 年 11 月推出的开放标准，用于规范 AI 助手连接外部工具和数据源的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Leiden_algorithm">Leiden algorithm - Wikipedia</a></li>
<li><a href="https://microsoft.github.io/graphrag/">Welcome - GraphRAG</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#ai-agents`, `#knowledge-graph`, `#code-analysis`, `#developer-tools`, `#mcp`

---

<a id="item-3"></a>
## [agent-skills 仓库为 AI 编程代理提供 19 个生产级技能](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

addyosmani/agent-skills 仓库已获得超过 86,900 颗星，为 Claude Code、Codex 和 Cursor 等 AI 编程代理提供精选的生产级工程技能。这些技能旨在让代理像资深工程师一样工作，而不是默认采用最短的解决方案。 该仓库解决了 AI 编程代理的一个关键局限——它们往往默认采用最短或最不稳健的解决方案。通过将领域知识和最佳实践打包成可复用的技能，它帮助开发者从 Claude Code、Codex 和 Cursor 等工具中获得更可靠、更接近资深工程师水准的输出。 该仓库主要使用 JavaScript 编写，拥有 9,338 个 fork，最近一次推送时间为 2026-08-11，表明维护活跃。它涵盖 agent-skills、antigravity、claude-code、codex、cursor 和 skills 等主题，初始版本包含 19 个生产级技能。

github · addyosmani · 8月11日 19:48

**背景**: AI 编程代理是能够理解代码库、编辑文件、运行命令并帮助开发者更快交付软件的工具。代理技能（agent skills）是这些助手可以加载以执行开发任务的任务特定指令文件，将领域知识、最佳实践和工作流打包成可复用格式。该仓库由知名开发者 Addy Osmani 创建，已成为这一新兴领域最受欢迎的资源之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents. · GitHub</a></li>
<li><a href="https://dev.to/_46ea277e677b888e0cd13/agent-skills-19-production-grade-skills-that-make-ai-coding-agents-work-like-senior-engineers-5bi9">agent-skills: 19 Production-Grade Skills That Make AI Coding Agents Work Like Senior Engineers - DEV Community</a></li>
<li><a href="https://docs.databricks.com/aws/en/agent-skills/">Agent skills for AI coding assistants | Databricks on AWS</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#ai-coding-agents`, `#prompt-engineering`, `#developer-tools`, `#github-repository`

---

<a id="item-4"></a>
## [Agent 优先控制平面发布 2,005+ Skills，支持 CLI、MCP 与插件](https://github.com/sickn33/agentic-awesome-skills) ⭐️ 8.0/10

AAS Core 是一个本地、Agent 优先的控制平面，提供完整的技能目录发现、Agent 自主选择、技术栈验证与规划能力，并内置 2,005+ 个 agentic skills。该项目附带 CLI、本地 MCP、插件和 Workbench，在 GitHub 上已获得 44,910 颗星。 该项目反映了行业向“agent skills”标准化的转变，使 AI Agent 更实用、可测试且可治理。由于支持主流 Agent 生态（Claude Code、Codex CLI、Cursor、Gemini CLI、Antigravity），它为开发者提供了一种跨工具发现和复用 agentic skills 的统一方式。 该仓库主要使用 Python 编写，拥有 6,567 个 fork，且报告零个未解决问题。项目维护活跃，最近一次推送时间为 2026-08-13，并支持包括 Claude Code、Codex CLI、Cursor、Gemini CLI、Kiro 和 Antigravity 在内的多种 Agent 平台。

github · sickn33 · 8月13日 17:56

**背景**: Agentic skills 是打包好的指令、代码和资源集合，AI Agent 可以在需要时发现并使用它们——就像交给通用 AI 模型的“专业认证”。Model Context Protocol \(MCP\) 由 Anthropic 于 2024 年 11 月推出，是一个开放标准，用于规范 AI 系统如何连接外部工具和数据源。Google Antigravity 是一个 Agent 优先的开发平台，用于编排自主 AI Agent 进行代码生成、执行和测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://medium.com/@jcpineda/agentic-skills-and-tools-1551e3e08f1d">Agentic Skills and Tools. The concept of AI agents is shifting | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#MCP`, `#developer-tools`, `#AI-agents`, `#skill-library`

---

<a id="item-5"></a>
## [Gemini 3.7 Flash：可调思考级别与增强视觉能力](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.7 Flash，这是一款新的基础模型，具备增强的视觉能力和可定制的思考级别（低、中、高），可通过 Gemini API 使用。 此次发布使开发者能够控制模型的推理深度，平衡成本、延迟和输出质量。这代表了谷歌在 Flash 系列中的持续快速迭代，与 GPT-5.6 Luna 和 Terra 等模型竞争。 该模型支持 LOW、MEDIUM（默认）和 HIGH 思考级别，但不支持 MINIMAL。入门定价计划于 2026 年 12 月 31 日翻倍，该模型在视觉任务和 DeepSWE 1.1 等基准测试中表现强劲。

hackernews · thisisauserid · 8月13日 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49289112)

**背景**: 思考级别允许 AI 模型在回答前生成内部推理步骤，以提高准确性但增加延迟。可调思考让用户根据使用场景选择合适的平衡。Gemini 3.7 Flash 是谷歌 Flash 系列的最新版本，该系列传统上专注于低成本、高容量的任务，但现在包含了增强的推理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-7-flash/">Gemini 3 . 7 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash">Gemini 3 . 7 Flash | Gemini Enterprise Agent Platform | Google Cloud...</a></li>
<li><a href="https://artificialanalysis.ai/articles/gemini-3-7-time-frontier">Gemini 3 . 7 Flash : On the Intelligence vs. Time per Task Pareto frontier</a></li>

</ul>
</details>

**社区讨论**: 社区成员测试了该模型的视觉能力，一位用户将其图像转 HTML 的输出与 Opus 进行了有利比较。其他人指出，像 Luna 这样的竞争对手提供了更好的性价比，而定价计划因模型迭代速度快而被批评为不切实际。

**标签**: `#Gemini 3.7 Flash`, `#Google AI`, `#large language model`, `#vision`, `#model release`

---

<a id="item-6"></a>
## [Spaghettifying DRAM 攻击解锁 AMD Jaguar 处理器隐藏功能](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 8.0/10

安全研究员 Christopher Domas 在 GitHub 仓库 skitter-creek-bath-salts 中发布了一种名为“Spaghettifying DRAM”的新硬件攻击，并将在 Black Hat 2026 上展示。该攻击利用 DRAM 加扰机制解锁通常隐藏在 ring 0 之下的 CPU 功能，已在 AMD Family 16h（Jaguar）CPU 上完成开发和测试。 这一研究意义重大，因为 DRAM 地址加扰原本被视为一种保护机制，但该工作将其变成攻击面，可能向 ring-0 软件暴露更深的 CPU 特权。它会影响系统安全研究、虚拟化与游戏主机破解，并可能促使厂商明确或修复内存控制器的锁定行为。 该攻击已在 AMD Family 16h 上完成开发和测试，这是公开资料中最后一个记载 DRAM 控制器转换寄存器、且显示这些寄存器无法加锁的 CPU 家族。README 提到 Zen 3 的内存控制器寄存器基地址不同，但其他受影响处理器家族的具体范围尚不明确。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: DRAM 加扰是内存控制器在数据到达 DRAM 芯片前对物理地址进行重排的一种技术，最初用于降低电气噪声、改善信号完整性。将物理地址转换到 DRAM 需要专用的控制器寄存器；如果软件能操纵这些寄存器，攻击者就可能重新映射内存并触达隐藏的高特权 CPU 功能。Christopher Domas 是 Battelle Memorial Institute 的知名安全研究员，以《The MoVfuscator》和 x86 硬件后门等演讲著称。skitter-creek-bath-salts 是他在 Black Hat 2026 演讲《Spaghettifying DRAM》的公开仓库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49286341">Spaghettifying DRAM | Hacker News</a></li>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/skitter-creek-bath-salts: Unlocking _everything_ on the CPU with DRAM scrambling · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Christopher Domas 即将在 Black Hat 上的演讲十分期待，并称赞他过往关于逆向工程和硬件后门的演讲。还有人指出 DRAM 日益复杂、攻击面巨大，ring-0 权限可能暴露“负环”领域，并追问除 AMD Family 16h 外还有哪些较新的 CPU 受影响；也有评论者表示，一旦拿到 ring-0，Xbox 和 PlayStation 的安全团队就该紧张了。

**标签**: `#security`, `#hardware`, `#DRAM`, `#exploit`, `#research`

---

<a id="item-7"></a>
## [DeepSeek 开源 Harness 智能体框架，支持全量可追踪会话日志](https://deepseek.com/harness/en/) ⭐️ 8.0/10

DeepSeek 发布了 Harness 的早期开发者预览版，这是一个采用 MIT 许可证的开源智能体框架（agent harness）。它提供仅追加（append-only）的会话日志来记录模型看到的所有内容，并支持动态插件系统。 这为 AI 开发者提供了一种开放、可追踪的方式来检查和调试智能体的运行过程，与一些闭源模型中加密或混淆的追踪记录形成对比。它可能推动开源生态中透明多智能体工具的采用。 Trajectory 视图允许用户按来源检查记录，而恢复（resume）、分支（fork）、搜索和回放（replay）都基于同一事件流运作。作者提醒，这只是一个早期预览版，存在不少粗糙之处，并预计会有破坏兼容性的变更。

hackernews · bjin · 8月13日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49285244)

**背景**: Agent harness（智能体框架）是围绕大语言模型的软件基础设施，负责管理工具调用、记忆、状态持久化、执行环境和反馈回路，从而把模型变成真正的 AI 智能体。DeepSeek 的 Harness 把所有上下文注入都记录在仅追加的会话日志中，让智能体运行过程更可观测、更容易调试。社区评论将其插件系统与 Cordis 相比较，Cordis 是一个已被 Koishi 项目使用的热重载插件框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://www.databricks.com/blog/ai-harness">What is an AI Agent Harness? | Databricks Blog</a></li>
<li><a href="https://harness-engineering.ai/blog/agent-harness-complete-guide/">The Complete Guide to Agent Harness: What It Is and Why It ...</a></li>

</ul>
</details>

**社区讨论**: 有评论者称赞仅追加的会话日志是“杀手级功能”，并指出一些美国模型的追踪记录会被混淆或加密。一位作者回应说这只是一个早期的 MIT 许可预览版，欢迎反馈；另一位评论者则强调了底层的 Cordis v4 插件系统，以及它在卸载时还原副作用的能力。

**标签**: `#deepseek`, `#agent-harness`, `#open-source`, `#developer-tools`, `#traceability`

---

<a id="item-8"></a>
## [GPT-5.6 新增 Responses API 能力，助力构建高性价比 AI 智能体](https://openai.com/index/builders-guide-to-gpt-5-6) ⭐️ 8.0/10

OpenAI 推出了新的大版本模型 GPT-5.6，并增强了 Responses API 的能力，旨在帮助初创公司更快、更经济地构建 AI 智能体。该公告强调更智能的模型选择是开发者的关键主题。 这对构建智能体的 AI 开发者有直接影响，提供了能够降低成本和开发时间的新工具。通过改进 Responses API 和模型选择，OpenAI 降低了初创公司交付生产级智能体应用的门槛。 Responses API 最初于 2025 年 3 月 11 日发布，结合了 Chat Completions API 的易用性和面向智能体应用的高级工具调用能力。GPT-5.6 在此基础上增加了专注于模型选择和成本效益的新能力，但公告中未详细说明具体的技术参数。

rss · OpenAI News · 8月13日 11:00

**背景**: OpenAI Responses API 是一个开发者工具，旨在通过结合 Chat Completions API 的易用性和高级工具调用能力，简化智能体应用的创建。模型选择是 AI 开发者的关键策略，因为为工作负载选择合适的模型需要在成本、性能和能力之间进行权衡。GPT-5.6 似乎是 OpenAI 模型系列演进的延续，重点是帮助开发者更高效地构建智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Responses_API">OpenAI Responses API</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/choose-ai-model">Choose the Right AI Model for Your Workload - Azure ...</a></li>

</ul>
</details>

**标签**: `#GPT-5.6`, `#OpenAI`, `#AI agents`, `#Responses API`, `#model selection`

---

<a id="item-9"></a>
## [OpenAI 预览 Ultrafast 服务层：GPT-5.6 Sol 速度提升 14 倍](https://openai.com/index/previewing-ultrafast) ⭐️ 8.0/10

OpenAI 预览了 Ultrafast，这是一个由 Cerebras 驱动的新 API 服务层，可将 GPT-5.6 Sol 的运行速度提升至原来的 14 倍，每秒最多输出 750 个 token。 这大幅降低了开发者的推理延迟，使更交互、更实时的 AI 应用成为可能。同时表明 OpenAI 正在将硬件多元化，不再局限于 NVIDIA GPU，以在速度上获得竞争优势。 Ultrafast 服务层利用了 Cerebras 的晶圆级引擎（Wafer Scale Engine），该引擎以超快推理著称。14 倍加速是相对于标准 GPU 推理而言，预览针对的是 GPT-5.6 Sol，这是能力最强的模型变体。

rss · OpenAI News · 8月13日 10:00

**背景**: Cerebras 使用专有的晶圆级引擎，推理速度比 NVIDIA GPU 快达 15 倍。GPT-5.6 是 OpenAI 于 2026 年 7 月发布的模型系列，包含 Luna、Terra 和 Sol 三个变体。Sol 是能力最强的，专注于网络安全和长周期任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cerebras.ai/inference">Inference - Cerebras</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#API`, `#inference`, `#performance`

---

<a id="item-10"></a>
## [Hugging Face 重现 2200 篇 ICML 论文，发现可重复性差距](https://huggingface.co/blog/icml-2026-open-reproductions) ⭐️ 8.0/10

Hugging Face 发布了一篇博客文章，详细介绍了他们从大规模重现 2200 篇 ICML 会议论文中获得的经验教训，突出了常见的可重复性挑战，并为机器学习社区提供了实用见解。 这项工作为机器学习研究中的可重复性危机提供了数据驱动的评估，帮助研究人员和实践者了解哪些做法有效、哪些失败，并鼓励采用更严谨的科学方法。 这项努力涉及在强化学习、计算机视觉和自然语言处理等不同子领域重现结果，团队记录了他们遇到的具体障碍，包括缺失代码、不完整的超参数设置和环境依赖。

rss · Hugging Face Blog · 8月13日 00:00

**背景**: 可重复性是科学进步的基石，但在机器学习中，由于代码、数据或详细实验设置的缺失，许多已发表的结果很难或无法独立验证。ICML（国际机器学习大会）是机器学习研究的顶级会议之一，其论文的可重复性对该领域的可信度尤为重要。

**标签**: `#reproducibility`, `#machine learning research`, `#ICML`, `#open science`, `#Hugging Face`

---

<a id="item-11"></a>
## [DeepSeek V4 Pro 0813（在 OpenRouter 上）](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek 发布了 V4 Pro 0813，该模型参数规模达 1.7T，可通过 API 使用，并已在 Hugging Face 上开放权重。

rss · Simon Willison · 8月12日 23:59

**标签**: `#deepseek`, `#large language model`, `#open weights`, `#API`, `#model release`

---

<a id="item-12"></a>
## [JetBrains 基准测试暴露输入浪费，Caveman 重构为本地代理](https://www.reddit.com/r/ClaudeCode/comments/1vn9xyo/jetbrains_called_bullshit_on_cavemans_65_they/) ⭐️ 7.0/10

在 JetBrains 独立基准测试仅测得 8.5% 的输出 token 节省（作者此前声称 65%）之后，Caveman 作者将该工具重构为本地代理，为 Claude Code、Codex 及其他编码代理压缩输入上下文。重构版在 54 次运行中报告输入 token 减少 33.2%，且全部 18 项精确答案检查均通过。 这凸显了编码代理工作流中的一个真实低效问题：输入上下文（文件、日志、工具输出、MCP 响应）被反复喂给模型，成为成本的主要来源。重构版为开发者提供了一种实用方式，在保留可恢复内容的同时减少输入 token 消耗，也展示了独立基准测试如何推动更好的工具诞生。 该代理在每次调用提供商前压缩输入，同时保持原始内容可逐字节恢复。作者还声称，通过 `caveman claude` 命令自动以图片形式加载，所有已安装的技能可以以 70% 更少的 token 运行，且保持 99% 的准确率，而常规的 Claude Code 配置保持不变。

reddit · r/ClaudeCode · /u/VeryVexxy · 8月13日 12:55

**背景**: Claude Skills 是 Anthropic 的 Claude AI 的一项功能，提供灵活的能力，包括对可执行脚本的支持。像 Claude Code 和 Codex 这样的编码代理通过反复将上下文——文件、日志、工具输出和 MCP（模型上下文协议）响应——发送给模型来工作，这会推高 token 成本。模型上下文协议是 Anthropic 于 2024 年 11 月推出的开放标准，用于规范 AI 系统与外部工具和数据源的集成方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://grokipedia.com/page/Claude_Skills">Claude Skills</a></li>
<li><a href="https://claude.com/skills">Skills | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#coding agents`, `#context compression`, `#proxy`, `#JetBrains`

---