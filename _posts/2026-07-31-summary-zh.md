---
layout: default
title: "Horizon Summary: 2026-07-31 (ZH)"
date: 2026-07-31
lang: zh
---

> 从 100 条内容中筛选出 8 条重要资讯。

---

1. [Graphify 将任意代码库转化为可查询的知识图谱](#item-1) ⭐️ 8.0/10
2. [开源应用把编码代理变成设计引擎](#item-2) ⭐️ 8.0/10
3. [wshobson/agents：面向 AI 编码代理的多平台插件市场](#item-3) ⭐️ 8.0/10
4. [为 AI 编程代理提供防崩溃文件规划，收获 2.59 万星](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4 Flash 0731 以每百万输出 0.28 美元实现前沿智能](#item-5) ⭐️ 8.0/10
6. [GPT-5.6 Luna 价格暴跌 80%，Sol 推理优化立功](#item-6) ⭐️ 8.0/10
7. [llama.cpp b10208 为 SYCL 后端新增 oneMKL 闪存注意力](#item-7) ⭐️ 7.0/10
8. [smevals：一个轻量级开源 LLM 评估套件](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Graphify 将任意代码库转化为可查询的知识图谱](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

Graphify-Labs/graphify 是一个极受欢迎的 GitHub 仓库（99,720 星），它为 Claude Code、Cursor、Codex 和 Gemini CLI 提供技能，通过本地确定性 AST 解析将任意代码库转化为可查询的知识图谱。 这种方法为基于向量的代码搜索提供了确定性、可解释的替代方案，使 AI 编程助手在复杂代码库的理解和导航上更加可靠。 Graphify 使用 tree-sitter 进行本地 AST 解析，支持包括文档和 PDF 在内的多种文件类型，明确避免使用向量存储，并提供知识图谱中每条边的解释。

github · Graphify-Labs · 7月30日 18:15

**背景**: 抽象语法树（AST）是源代码语法结构的树状表示，常用于编译器和代码分析工具。Tree-sitter 是一个解析器生成工具，可为多种编程语言生成高效、增量的 AST，实现快速准确的代码解析。知识图谱存储实体及其关系，支持结构化查询和推理。Graphify 利用 tree-sitter 将代码库解析为 AST，然后构建知识图谱，其中节点代表代码实体，边代表关系，整个过程不依赖向量数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/lovestaco/getting-started-with-tree-sitter-syntax-trees-and-express-api-parsing-5c2d">Getting Started with Tree - sitter : Syntax Trees and... - DEV Community</a></li>

</ul>
</details>

**标签**: `#knowledge-graph`, `#code-analysis`, `#developer-tools`, `#AI-agents`, `#MCP`

---

<a id="item-2"></a>
## [开源应用把编码代理变成设计引擎](https://github.com/nexu-io/open-design) ⭐️ 8.0/10

GitHub 仓库 nexu-io/open-design 已获得超过 82,000 颗星，它是一个开源桌面应用，能将 Claude Code、Codex、Cursor 等编码代理转变为设计引擎，用于创建原型、落地页、仪表盘等，并支持导出为 HTML、PDF、PPTX 和 MP4 格式。 该项目弥合了 AI 辅助编程与视觉设计之间的鸿沟，让开发者能够通过自然语言提示快速制作原型并生成设计资产。它利用现有的编码代理和本地优先架构，降低了对专有工具的依赖，使设计更加民主化。 该应用支持自带密钥（BYOK）模式，允许用户提供自己的 API 密钥以使用各种 AI 模型，并且是用 TypeScript 构建的本地优先桌面应用。它集成了超过 20 种 CLI 工具，包括 Claude Code、Codex、Cursor、Gemini、OpenCode 和 Qwen。

github · nexu-io · 7月31日 18:45

**背景**: 编码代理是能够理解代码库并根据自然语言指令生成代码的 AI 工具。Vibe coding（氛围编程）是由 Andrej Karpathy 提出的术语，描述了一种 AI 辅助开发方式：开发者描述项目需求并接受生成的代码，而不进行深入审查。该应用将这一概念扩展到视觉设计领域，让用户通过对话式提示生成设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#ai-design`, `#coding-agents`, `#design-tools`, `#local-first`, `#prototyping`

---

<a id="item-3"></a>
## [wshobson/agents：面向 AI 编码代理的多平台插件市场](https://github.com/wshobson/agents) ⭐️ 8.0/10

GitHub 仓库 wshobson/agents 已获得超过 38,000 颗星，提供了一个多平台插件市场，支持包括 Claude Code、Codex CLI、Cursor、OpenCode、GitHub Copilot 和 Gemini CLI 在内的主要 AI 编码代理。 该仓库通过为不同 AI 编码代理提供统一的插件市场，解决了工具碎片化问题，使开发者能够更轻松地扩展和集成工作流程。 该仓库主要使用 Python 编写，涵盖 MCP（模型上下文协议）、代理技能、自动化和提示工程等主题。它有 4,107 个复刻和仅 11 个未解决问题，表明维护活跃。

github · wshobson · 7月22日 15:32

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在标准化 AI 系统与外部工具和数据的集成方式。Codex CLI 是 OpenAI 开发的本地终端 AI 编码代理，而 Gemini CLI 是 Google DeepMind 的命令行工具。该仓库充当一个插件市场，支持这些不同代理，并利用 MCP 等协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://github.com/openai/codex">GitHub - openai/ codex : Lightweight coding agent that runs in your...</a></li>
<li><a href="https://geminicli.com/">Build, debug &amp; deploy with AI | Gemini CLI</a></li>

</ul>
</details>

**标签**: `#agentic-ai`, `#developer-tools`, `#plugins`, `#mcp`, `#claude-code`

---

<a id="item-4"></a>
## [为 AI 编程代理提供防崩溃文件规划，收获 2.59 万星](https://github.com/OthmanAdi/planning-with-files) ⭐️ 8.0/10

开源仓库 OthmanAdi/planning-with-files 已获得 25,889 星和 2,170 个 fork，为 AI 编程代理提供基于 Markdown 的持久化规划系统。它提供防崩溃的任务计划、在 /clear 或上下文压缩后的会话恢复，以及每次对话回转时重新注入内容以对抗上下文腐烂（context rot），并通过 Agent Skills 标准兼容 Claude Code、Codex、Cursor 及 60 多个代理。 该工具直接解决了长期运行的 AI 代理的两个关键失败模式——上下文腐烂和会话丢失——使多步骤编码任务更加可靠。它对 Agent Skills 标准的采用，标志着行业正在向跨工具的便携式代理能力转变。 它在磁盘上实现了 Manus 风格的工作记忆，创建 task\_plan.md、findings.md 和 progress.md 文件，并带有可选择启用的确定性完成门控。该项目使用 Python 编写，有 7 个未关闭 issue，最近一次推送时间为 2026-07-24。

github · OthmanAdi · 7月24日 18:18

**背景**: Agent Skills 是一种轻量、开放的格式，用于扩展 AI 代理的能力；一个技能就是一个包含 SKILL.md 文件的文件夹，工具可以按需发现并加载。上下文腐烂（context rot）是指随着上下文窗口被无关或过时信息过度饱和，大语言模型的短期记忆逐渐退化，导致长期运行的代理失败。该项目采用了“Manus 风格”的规划方法，即使用基于文件的工作记忆来保持计划在会话之间的持久性和可恢复性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/OthmanAdi/planning-with-files">GitHub - OthmanAdi/ planning -with-files: Persistent file-based...</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://code.visualstudio.com/docs/agent-customization/agent-skills">Use Agent Skills in VS Code</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#coding-agent`, `#planning`, `#session-recovery`, `#context-engineering`

---

<a id="item-5"></a>
## [DeepSeek V4 Flash 0731 以每百万输出 0.28 美元实现前沿智能](https://artificialanalysis.ai/models/deepseek-v4-flash) ⭐️ 8.0/10

DeepSeek 发布了 V4 Flash 0731，这是一个重新训练后的混合专家模型，在基准测试中达到前沿智能水平，而每百万输出 token 仅需 0.28 美元，性能超越其 Pro 版本。 该模型以极低的成本提供了前沿 AI 能力，可能让开发者与研究人员更易获得先进的编码、推理和智能体工作流。 这是一个稀疏混合专家模型，总参数 284B，激活参数 13B，支持 100 万 token 的上下文窗口，专为编码、推理和智能体任务优化。该模型已在 HuggingFace 上开放下载，并可通过量化（如 Unsloth Q8 仅需 162GB）在本地运行。

hackernews · theanonymousone · 7月31日 07:59 · [社区讨论](https://news.ycombinator.com/item?id=49120299)

**背景**: 混合专家模型（MoE）每个 token 仅激活部分参数，从而以较低计算成本实现高性能。DeepSeek 是一家以发布具有竞争力的开源权重模型而闻名的中国 AI 公司。Flash 变体旨在保持高智能的同时实现更快的推理和更低的成本，0731 版本包含了训练后的改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>
<li><a href="https://lmmarketcap.com/model/deepseek-v4-flash-0731">DeepSeek V 4 Flash 0731 - Pricing &amp; Benchmarks 2026 | LM Market Cap</a></li>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing/">Models &amp; Pricing | DeepSeek API Docs</a></li>

</ul>
</details>

**社区讨论**: 社区对该模型的性价比感到兴奋，用户指出它以极低的成本与 GLM 5.2 和 Gemini 3.6 等模型相媲美。部分讨论涉及未来可能更新的 Pro 版本以及本地运行模型的能力。也有人提出了关于 HuggingFace 托管经济性的疑问。

**标签**: `#deepseek`, `#model-release`, `#ai-economics`, `#performance-analysis`, `#frontier-model`

---

<a id="item-6"></a>
## [GPT-5.6 Luna 价格暴跌 80%，Sol 推理优化立功](https://simonwillison.net/2026/Jul/30/luna-price-drop/#atom-everything) ⭐️ 8.0/10

OpenAI 宣布大幅下调 GPT-5.6 系列模型价格，其中 Luna 降价 80%，Terra 降价 20%。这一降价得益于使用 GPT-5.6 Sol 优化推理和负载均衡，使服务成本降低 20%。 此次降价使 Luna 成为主流 AI 提供商中最便宜的高质量模型，价格低于 Google 的 Gemini 3.1 Flash-Lite 和 Anthropic 的 Claude Haiku 4.5，并展示了 AI 自我优化服务基础设施的新范式。 优化过程包括 GPT-5.6 Sol 自主重写 Triton 和 Gluon 中的生产内核，以减少内存移动和 GPU 空闲时间，从而将端到端服务成本降低 20%。Luna 的新价格为每百万输入令牌 0.20 美元，每百万输出令牌 1.20 美元。

rss · Simon Willison · 7月30日 23:58

**背景**: GPT-5.6 是 OpenAI 的最新模型系列，其中 Sol 是旗舰模型，专为复杂推理和编程任务设计。推理优化是指降低 AI 模型运行计算成本和延迟的技术。OpenAI 使用 GPT-5.6 Sol 分析和改进执行模型操作的底层内核，利用其开源 GPU 编程语言 Triton 和 Gluon。这种方法结合更好的负载均衡，使服务成本降低 20%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT - 5 . 6 Sol - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://gcore.com/learning/what-is-ai-inference">What is AI inference and how does it work? | Gcore</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#price drop`, `#inference optimization`, `#AI models`

---

<a id="item-7"></a>
## [llama.cpp b10208 为 SYCL 后端新增 oneMKL 闪存注意力](https://github.com/ggml-org/llama.cpp/releases/tag/b10208) ⭐️ 7.0/10

llama.cpp b10208 为 SYCL 后端引入了基于 oneMKL GEMM 的闪存注意力机制，利用 Intel XMX 硬件加速提示处理，修复了关键布局错误，并在 Intel GPU 上实现了最高 1.97 倍的性能提升。 此版本显著提升了 Intel GPU 上的提示处理性能，使 llama.cpp 在 Intel 硬件上的大语言模型推理更加高效，并扩大了其用户覆盖范围。 该功能通过环境变量 GGML\_SYCL\_ENABLE\_MKL\_FA 控制，现已支持所有 KV 缓存类型（F16、BF16、F32、量化）。调试和诊断模式可通过 GGML\_SYCL\_MKL\_FA\_DEBUG 和 GGML\_SYCL\_MKL\_FA\_DIAG 启用。

github · github-actions\[bot\] · 7月31日 16:02

**背景**: SYCL 是一种基于 C++ 的跨平台异构计算编程模型。oneMKL（Intel oneAPI 数学内核库）为 Intel CPU 和 GPU 提供高度优化的数学例程。XMX（Xe 矩阵扩展）是 Intel Arc GPU 中专用的矩阵乘法单元，用于加速深度学习工作负载。闪存注意力（flash attention）是一种高效的注意力算法，通过分块和避免大型中间矩阵来减少内存带宽使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Math_Kernel_Library">Math Kernel Library - Wikipedia</a></li>
<li><a href="https://www.intel.com/content/www/us/en/docs/oneapi/optimization-guide-gpu/2024-2/boost-matrix-multiplication-performance-with-intel.html">Boost Matrix Multiplication Performance with Intel® Xe Matrix ...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#SYCL`, `#flash-attention`, `#oneMKL`, `#performance`

---

<a id="item-8"></a>
## [smevals：一个轻量级开源 LLM 评估套件](https://simonwillison.net/2026/Jul/31/smevals/#atom-everything) ⭐️ 7.0/10

Prime Radiant 与 Simon Willison 合作发布了 smevals，这是一个新的开源工具，用于在不同模型配置上运行小型评估套件并对结果进行评分。该工具已上架 PyPI，可通过 uvx 命令运行。 smevals 提供了一个简单、词汇驱动的框架，使 AI 开发者能够系统地评估模型、提示词和智能体框架。其开源特性和简洁的 CLI 命令降低了 AI 社区进行严格模型测试的门槛。 该工具将运行执行与评分分离，用户可使用 `uvx smevals run` 运行评估，稍后用 `uvx smevals grade` 进行评分。它还能生成静态 HTML 报告以便分享，如俳句写作基准示例所示。

rss · Simon Willison · 7月31日 21:15

**背景**: 评估套件（evals）对于衡量大型语言模型（LLM）和提示词配置的能力与局限性至关重要。smevals 使用清晰的词汇——eval、task、config、run、grader、check——来结构化流程。`uvx` 命令是 uv Python 包管理器的一部分，可在临时环境中运行工具，无需永久安装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/smevals/">smevals · PyPI</a></li>
<li><a href="https://docs.astral.sh/uv/">uv is an extremely fast Python package and project manager, written in...</a></li>

</ul>
</details>

**标签**: `#eval suite`, `#model evaluation`, `#AI tools`, `#open source`, `#prompts`

---