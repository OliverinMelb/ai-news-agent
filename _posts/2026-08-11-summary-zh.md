---
layout: default
title: "Horizon Summary: 2026-08-11 (ZH)"
date: 2026-08-11
lang: zh
---

> 从 91 条内容中筛选出 12 条重要资讯。

---

1. [Graphify 通过 AST 解析将代码库转为可查询的知识图谱](#item-1) ⭐️ 8.0/10
2. [穴居人技能让 Claude 省 65% token，星标飙至 9.75 万](#item-2) ⭐️ 8.0/10
3. [86,193 星 GitHub 仓库精选生产级 AI 编程代理技能](#item-3) ⭐️ 8.0/10
4. [158 个科学代理技能让任何 AI 变成 AI 科学家](#item-4) ⭐️ 8.0/10
5. [将 LLM 输出重放到弱模型中可暴露隐藏的推理过程](#item-5) ⭐️ 8.0/10
6. [Meta 发布 Muse Glimmer：30B 开源权重智能体模型](#item-6) ⭐️ 8.0/10
7. [OpenAI Agents SDK v0.20.0：新默认模型与 MCP v1/v2 支持](#item-7) ⭐️ 7.0/10
8. [OpenAI Agents JS SDK v0.15.0：新默认模型、MCP v2 与持久化状态](#item-8) ⭐️ 7.0/10
9. [llama.cpp 新增多输出后端采样，支持推测解码加速](#item-9) ⭐️ 7.0/10
10. [Mojo 1.0 Beta 发布，宣称 AI 高性能，但闭源编译器引发争议](#item-10) ⭐️ 7.0/10
11. [H3-metal 让 Apple Silicon 原生运行 MiniMax-H3 推理](#item-11) ⭐️ 7.0/10
12. [IBM 研究用更少 Token 达到 ACE 级别效果](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Graphify 通过 AST 解析将代码库转为可查询的知识图谱](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

Graphify 提供了一种确定性、可解释的替代方案，取代了基于嵌入的代码分析，使开发者和 AI 代理能够更轻松地理解、导航和调试复杂代码库。它通过模型上下文协议（MCP）与多个 AI 助手集成，有望显著提升 AI 辅助软件开发的工作流程。 该工具使用 Tree-sitter 进行 AST 解析，支持 Leiden 算法对生成的图谱进行社区检测，并通过 MCP 以技能形式运行，无需向量数据库。它不仅能解析源代码，还能解析文档、SQL 模式、配置文件和 PDF，且图谱中的每条边都有解释。

github · Graphify-Labs · 8月11日 14:30

**背景**: Tree-sitter 是一个开源解析器生成器和增量解析库，用于构建源代码的具体语法树，广泛应用于文本编辑器和静态分析工具。Leiden 算法是一种社区检测方法，改进了 Louvain 算法，能产生连接更紧密的社区；这里用于聚类相关代码实体。模型上下文协议（MCP）是 Anthropic 于 2024 年引入的开放标准，用于规范 AI 系统连接外部工具和数据源的方式。Graphify 的方法避免了常见的向量嵌入依赖——后者可能不透明且资源密集——而是采用确定性 AST 解析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Leiden_algorithm">Leiden algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tree-sitter_%28parser_generator%29">Tree-sitter (parser generator)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#knowledge-graph`, `#code-analysis`, `#developer-tools`, `#AST`, `#AI-agents`

---

<a id="item-2"></a>
## [穴居人技能让 Claude 省 65% token，星标飙至 9.75 万](https://github.com/JuliusBrussee/caveman) ⭐️ 8.0/10

JuliusBrussee/caveman 是一个让 Claude Code 以简短穴居人风格回复的技能，目前已获得 97,508 个 GitHub 星标并走红。仓库声称这种方法相比标准提示可将 token 用量减少 65%。 如果减少 token 的说法属实，开发者将能大幅降低 Claude Code 的使用成本并减少响应延迟。这也凸显了提示工程中一个更广泛的趋势：在 AI 编码代理里优先追求效率，而不是对话式啰嗦。 该仓库用 Go 编写，拥有 5,622 个 fork 和 470 个未关闭 issue，是 GitHub 上增长最快的提示工程技术项目之一。搜索结果引用的独立测试显示，在某些场景下可节省 63%–71% 的 token，但实际减少幅度因任务和输出类型而异。

github · JuliusBrussee · 8月11日 16:02

**背景**: Claude Code 是 Anthropic 推出的命令行 AI 编程代理，而“技能（skills）”是可复用的提示工程包，用于定制其行为。穴居人技术是一种系统提示技巧，它迫使模型去掉填充词、用简短片段回复，从而减少输出 token，在按量计费模型上降低费用。项目口号“why use many token when few token do trick”是一个网络梗，现已成为该项目的非官方标语。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stork.ai/blog/this-ai-trick-cuts-claude-costs-by-45">Caveman Claude Skill: Cut Your AI Token Costs In Half | Stork.AI</a></li>
<li><a href="https://www.linkedin.com/pulse/prompt-engineering-trick-sounds-like-joke-saves-real-money-malamud-hyhde">The Prompt Engineering Trick That Sounds Like a Joke (And Saves...)</a></li>
<li><a href="https://code.claude.com/docs/en/skills">Extend Claude with skills - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#ai`, `#claude-code`, `#prompt-engineering`, `#token-optimization`, `#github`

---

<a id="item-3"></a>
## [86,193 星 GitHub 仓库精选生产级 AI 编程代理技能](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

addyosmani/agent-skills 仓库已飙升至 86,000 多颗星，为 Claude Code、Codex 和 Cursor 等 AI 编程代理提供了一个精选的生产级工程技能集合。这些技能是可复用的能力，能增强代理执行复杂软件工程任务的能力。 该仓库提供了一个经过社区验证的资源，使开发者更容易提升 AI 编程代理的效果，降低了利用高级代理能力的门槛。极高的星标数表明它在开发者社区中获得了强烈的信任和实用性认可。 该仓库主要使用 JavaScript 编写，拥有 9,263 个分支、105 个未解决问题，并于 2026 年 8 月最近更新。其技能以可检查的 .md 文件形式存储，可跨多个 AI 编程代理使用，该仓库是更广泛的开源代理技能生态系统的一部分。

github · addyosmani · 8月11日 19:48

**背景**: AI 编程代理（如 Claude Code 和 OpenAI Codex）是能够自主规划并执行多步骤编码任务的工具，它们可以读取代码库、编辑文件、运行命令并迭代直至任务完成。“技能”是可复用、可共享的能力（通常以 .md 文件定义），用于教导代理如何执行特定领域的任务，类似于插件或工具。开放代理技能规范允许这些技能在市场中索引，并通过一条命令安装，从而轻松增强代理的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://skillsmp.com/">Agent Skills Marketplace | Codex &amp; Claude Skills | SkillsMP</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_%28AI_agent%29">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#ai-coding`, `#claude-code`, `#cursor`, `#codex`

---

<a id="item-4"></a>
## [158 个科学代理技能让任何 AI 变成 AI 科学家](https://github.com/K-Dense-AI/scientific-agent-skills) ⭐️ 8.0/10

GitHub 上的 K-Dense-AI/scientific-agent-skills 仓库发布了热门开源库，提供 158 个即用型科学代理技能和 100 多个科学数据库，让任何 AI 代理都能执行科学任务。它兼容 Cursor、Claude Code、Codex 等工具，已有超过 33,000 颗星和 170,000+科学家使用。 该库通过提供全面的即用技能集，大幅降低了创建 AI 科学家的门槛，使研究人员无需从头构建即可自动化复杂的科学工作流。其开源特性及与主流编码代理的广泛兼容性，可能加速生物学、化学、医学和药物发现等领域的研究。 该库包含 158 个技能，覆盖生物信息学、化学信息学、药物发现、基因组学、蛋白质组学和材料科学。它遵循开放的 Agent Skills 标准，每个技能是一个包含 SKILL.md 文件的文件夹，内含元数据和指令。

github · K-Dense-AI · 8月11日 18:02

**背景**: Agent Skills 是一种轻量级开放格式，用于通过专业知识和工作流扩展 AI 代理的能力；一个技能是一个包含 SKILL.md 文件的文件夹，内含指令。Cursor 是一个 AI 辅助代码编辑器，是 Visual Studio Code 的分支，支持自然语言代码编辑和自动化。该仓库利用这些概念提供科学领域特定的技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_%28code_editor%29">Cursor (code editor)</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#open-source`, `#scientific-computing`, `#AI-tools`, `#GitHub`

---

<a id="item-5"></a>
## [将 LLM 输出重放到弱模型中可暴露隐藏的推理过程](https://stolen-thoughts.com/) ⭐️ 8.0/10

此攻击削弱了前沿模型隐藏推理功能的安全保障，引发了对模型透明度、蒸馏风险以及当前 API 防护措施有效性的担忧。 该技术通过获取前沿模型生成的痕迹，将其重放到较弱的兄弟模型中，并破解该较弱模型以提取明文推理。该方法已通过具体示例和社区交叉验证得到验证。

hackernews · quantumgarbage · 8月11日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49257876)

**背景**: 像 OpenAI 的 o1 或 Anthropic 的 Claude 这样的专有 LLM 通常输出最终答案，但将内部链式推理隐藏在加密信封之后。兄弟模型是同一模型家族中较弱或较旧的版本，可能具有不太严格的安全措施。链式推理提示要求模型在回答前生成中间推理步骤，这能提高准确性但可能敏感。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes Hidden Reasoning Traces</a></li>
<li><a href="https://www.technologyreview.com/2026/07/30/1140927/a-fundamental-flaw-leaves-llms-vulnerable-to-attack/">A fundamental flaw leaves LLMs strikingly vulnerable to attack | MIT Technology Review</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain - of - Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者认为称其为“盗窃”具有误导性，因为用户已为 token 付费，而提供商才是扣留推理的一方。有人建议其他方法，例如直接禁用思考并提供一个“deep\_think”工具，也能达到同样效果。总体而言，社区认为该攻击验证了长期存在的对模型透明度和当前 API 防护脆弱性的担忧。

**标签**: `#LLM`, `#reasoning`, `#security`, `#distillation`, `#research`

---

<a id="item-6"></a>
## [Meta 发布 Muse Glimmer：30B 开源权重智能体模型](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta 发布了 Muse Glimmer，一个 30B 参数的开源权重模型，采用 Apache 2.0 许可证，针对智能体任务、工具使用和多步推理进行了优化。该模型在 DeepSearch QA、MCP-Atlas、τ-Bench 和 SWE-Bench 等基准测试中表现出色。 这标志着 Meta 以宽松许可证回归开放权重模型，使开发者能够获得先进的智能体能力。30B 的尺寸适合在 32GB 以上 RAM 的消费级硬件上本地部署，实现离线运行 AI 智能体。 Muse Glimmer 是一个视觉模型，能处理图像，Simon Willison 展示了它通过工具调用描述照片和探索代码库的能力。LM Studio 提供了 18.16GB 的量化版本，仅需 32GB RAM 即可同时运行其他应用。

rss · Simon Willison · 8月10日 23:56

**背景**: Meta 之前发布的 Llama 模型使用带有商业使用限制的自定义许可证；Muse Glimmer 采用 Apache 2.0，这是一个完全开源许可证。提到的基准测试（MCP-Atlas、τ-Bench 等）评估模型自主使用工具和多步推理的能力，这对于构建能完成现实任务的 AI 智能体至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://labs.scale.com/leaderboard/mcp_atlas">MCP Atlas - Scale Labs Leaderboard</a></li>
<li><a href="https://taubench.com/">τ - bench — Benchmarking AI Agents on Real-World Tasks</a></li>
<li><a href="https://www.kaggle.com/benchmarks/google/dsqa">DeepSearchQA Leaderboard | Kaggle</a></li>

</ul>
</details>

**标签**: `#Meta`, `#Muse Glimmer`, `#open-weights`, `#agentic model`, `#AI`

---

<a id="item-7"></a>
## [OpenAI Agents SDK v0.20.0：新默认模型与 MCP v1/v2 支持](https://github.com/openai/openai-agents-python/releases/tag/v0.20.0) ⭐️ 7.0/10

OpenAI 发布了 openai-agents-python SDK 的 v0.20.0 版本，将默认模型改为 gpt-5.6-luna，增加了对 MCP Python SDK v1 和 v2 的支持，并引入了 RunState.add\_input\(\) 用于暂存用户输入。 此版本将默认模型更新为更经济高效的新模型，并扩展了 MCP 兼容性，这对于构建具有自定义工具集成的智能体工作流的开发者至关重要。 MCP 依赖迁移可能对使用自定义本地 HTTP 传输的应用程序造成破坏；开发者可以锁定 mcp&lt;2 或迁移到 httpx2。RunState.add\_input\(\) 支持护栏、持久化和序列化。

github · seratch · 8月11日 03:12

**背景**: OpenAI Agents SDK 是一个用于构建可使用工具和外部数据的 AI 智能体的 Python 框架。MCP（模型上下文协议）是由 Anthropic 引入的开放标准，用于连接 AI 模型与外部系统。GPT-5.6 Luna 是 GPT-5.6 系列中的一个经济高效模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.6-luna">GPT - 5 . 6 Luna Model | OpenAI API</a></li>

</ul>
</details>

**标签**: `#openai-agents-sdk`, `#python`, `#agent-framework`, `#mcp`, `#release`

---

<a id="item-8"></a>
## [OpenAI Agents JS SDK v0.15.0：新默认模型、MCP v2 与持久化状态](https://github.com/openai/openai-agents-js/releases/tag/v0.15.0) ⭐️ 7.0/10

OpenAI 发布了 Agents JS SDK v0.15.0，该版本将 gpt-5.6-luna 设为新默认模型，加入了 MCP v2 协议协商并向后兼容 v1 服务器，同时在 RunState 中实现了持久化的输入、工具输出和重试状态。更新还改进了沙箱挂载的凭证安全性，并为实时功能添加了 React Native 支持。 此版本直接影响使用 OpenAI SDK 构建 AI 代理的开发者，提供了更具成本效益的默认模型和强大的状态持久化能力，使代理工作流在中断时更加可靠。MCP v2 协商确保与新旧工具服务器的兼容性，减少了集成摩擦。 使用自定义 OpenAI 客户端的应用必须升级到 openai 7.2 或更高版本；新默认模型 gpt-5.6-luna 使用 reasoning.effort: &#x27;none&#x27; 和 text.verbosity: &#x27;low&#x27;。MCP 本地连接现在通过 MCP TypeScript SDK v2 协商 2026-07-28 协议，并自动回退到 v1；持久化状态功能（如 pendingInput）在序列化后仍能保留，从而支持暂停恢复。

github · seratch · 8月11日 05:38

**背景**: OpenAI Agents SDK 是一个 JavaScript/TypeScript 框架，用于构建能够使用工具、处理多步骤任务并与外部服务集成的 AI 代理。MCP（模型上下文协议）是连接代理与外部工具服务器的标准，v2 带来了改进的能力，而 v1 服务器仍广泛部署。gpt-5.6-luna 模型是 OpenAI GPT-5.6 系列中的一个成本高效变体，专为快速、高吞吐量的工作负载设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.6-luna">GPT - 5 . 6 Luna Model | OpenAI API</a></li>
<li><a href="https://github.com/modelcontextprotocol/typescript-sdk/issues/2619">[ v 2 ] versionNegotiation: 2xx server/discover response with an empty or...</a></li>

</ul>
</details>

**标签**: `#openai`, `#agents`, `#mcp`, `#sdk`, `#typescript`

---

<a id="item-9"></a>
## [llama.cpp 新增多输出后端采样，支持推测解码加速](https://github.com/ggml-org/llama.cpp/releases/tag/b10355) ⭐️ 7.0/10

该特性使得本地 LLM 推理可通过推测解码获得 2-3 倍的加速，让消费级硬件上的实时应用成为可能。同时，它也为基于共识的自我改进或语义熵检测等多输出技术打开了新的大门。 实现中需要调整 mask 求和剪裁、避免复用输出视图内存，并确保 CPU 与 GPU 后端之间的分布一致。该功能已集成到 llama-sampler 模块中，并支持所有后端，包括 CPU、CUDA、Vulkan、ROCm 等。

github · github-actions\[bot\] · 8月10日 23:15

**背景**: 推测采样（又称推测解码）是一种技术，它在前向传播中生成多个草稿 token，然后通过目标模型一次验证，通常能带来 2-3 倍的加速。llama.cpp 是一个流行的开源 C/C++ LLM 推理引擎，基于 ggml 库构建，支持多种后端（CPU、GPU、Vulkan 等），并可在本地运行模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/latest/advanced/speculative-decoding.html">Speculative Sampling — TensorRT- LLM</a></li>
<li><a href="https://www.youtube.com/watch?v=2ouqE9g6oeM">What is Speculative Sampling ? | Boosting LLM inference ... - YouTube</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#inference`, `#sampling`, `#open-source`, `#AI`

---

<a id="item-10"></a>
## [Mojo 1.0 Beta 发布，宣称 AI 高性能，但闭源编译器引发争议](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 7.0/10

Mojo 旨在将 Python 的易用性与系统级性能结合，为 AI 场景提供统一语言（CPU、GPU、TPU）。但闭源编译器以及模糊的 Python 超集定位引发开发者质疑，导致其虽受热捧但实际采纳有限。 编译器基于 MLIR（多层次中间表示）构建，可针对异构硬件进行高级优化。路线图表明 Mojo 可能不会成为完整的 Python 超集，编译器与工具链的开源计划定于 2026 年。

hackernews · dayanruben · 8月11日 16:56 · [社区讨论](https://news.ycombinator.com/item?id=49261128)

**背景**: Mojo 是由 Modular 公司（由 LLVM 与 Swift 创始人 Chris Lattner 创立）开发的专有系统编程语言。它采用类似 Python 的语法，但引入了静态类型、内存安全以及编译期元编程，主要面向 AI 基础设施。该语言利用 MLIR 编译器框架，相比仅使用 LLVM 能更高效地支持 CPU、GPU 和加速器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo (programming language) - Wikipedia</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了质疑：有人质疑闭源编译器的价值，认为已有 Rust 后端的 Python 库等替代方案；另一些人因路线图撤回了此前超集承诺而对 Mojo 的 Python 超集地位感到困惑。还有用户指出公告中使用了 AI 生成的图片，削弱了信心。

**标签**: `#Mojo`, `#programming language`, `#AI`, `#compiler`, `#performance`

---

<a id="item-11"></a>
## [H3-metal 让 Apple Silicon 原生运行 MiniMax-H3 推理](https://github.com/antirez/h3.c) ⭐️ 7.0/10

Redis 的作者 antirez 发布了 h3.c，这是一个专为 Apple Silicon 优化的原生 MiniMax-H3 推理 C 实现，使得用户可以在本地运行 MiniMax-H3 模型进行视频生成。 这使 Apple Silicon 用户无需依赖云服务或 Nvidia GPU 即可运行强大的视频生成模型，极大地扩展了开源 AI 视频模型的可及性。同时也展示了在消费级硬件上运行复杂多模态模型的能力正在提升。 该实现尚处于早期阶段，速度较慢——社区报告显示，在 M5 Pro 上生成一段 9 秒 480x864 的视频需要超过一小时，在 M4 Max 上生成 15 秒 480p 视频需要 1.5 小时。可以通过 ComfyUI 使用 GGUF 量化版本（如 Q5\_K\_M 或 Q8\_0），其中 Q8\_0 需要约 34GB 内存。

hackernews · swyx · 8月11日 01:22 · [社区讨论](https://news.ycombinator.com/item?id=49252179)

**背景**: MiniMax-H3 是 MiniMax 发布的开源多模态模型，能够处理文本、图像、音频和视频生成。GGUF 是一种量化模型权重的文件格式，可降低内存占用，使得在 Apple Silicon Mac 等消费级硬件上运行大型模型成为可能。ComfyUI 是一个流行的基于工作流的界面，用于本地运行 AI 图像和视频生成模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/MiniMax-H3 · Hugging Face</a></li>
<li><a href="https://www.datacamp.com/tutorial/gguf-format-a-complete-guide">GGUF Format: A Complete Guide to Local LLM Inference</a></li>

</ul>
</details>

**社区讨论**: 社区成员反馈该实现可用但速度较慢，常见瓶颈是 Apple Silicon 的内存带宽。用户正在尝试不同的量化级别和稀疏注意力优化，antirez 表示有意根据 MiniMax 的 AMA 提示实现稀疏注意力。部分用户指出 128GB 内存要求限制了可及性，但 96GB 机器在较低分辨率和量化下可能仍可运行。

**标签**: `#MiniMax-H3`, `#Apple Silicon`, `#inference`, `#video generation`, `#open-source`

---

<a id="item-12"></a>
## [IBM 研究用更少 Token 达到 ACE 级别效果](https://huggingface.co/blog/ibm-research/altk-evolve-sldd) ⭐️ 7.0/10

IBM 研究团队提出了一种新技术，在仅使用更少 Token 的情况下达到了与 ACE 方法相当的效果，从而提升了大语言模型的效率。 这一突破有望降低 AI 推理的计算成本和延迟，使高级 AI 能力更易于应用于实际场景并实现规模化。 该技术详细说明发布在 Hugging Face 博客上，但具体实现细节以及与 ACE 的对比在提供的内容中尚未公开。

rss · Hugging Face Blog · 8月11日 13:37

**背景**: 大语言模型以称为 token 的单位处理文本，在保持准确性的同时减少 token 使用量是关键优化目标。ACE（可能是一种先前的方法）是新方法旨在以更低 token 消耗追赶的基准技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**标签**: `#token efficiency`, `#model optimization`, `#IBM Research`, `#AI research`, `#Hugging Face`

---