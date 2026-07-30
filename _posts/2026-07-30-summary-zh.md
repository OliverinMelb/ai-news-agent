---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
---

> 从 91 条内容中筛选出 8 条重要资讯。

---

1. [多工具插件市场统一六大 AI 编码代理](#item-1) ⭐️ 9.0/10
2. [OpenMontage：首个开源智能体视频制作系统](#item-2) ⭐️ 8.0/10
3. [AI 代理营销技能提示仓库获 4.2 万星](#item-3) ⭐️ 8.0/10
4. [用三万两千星的 Agent 技能去除 AI 写作痕迹](#item-4) ⭐️ 8.0/10
5. [Gemini Robotics 2 为机器人带来全身智能](#item-5) ⭐️ 8.0/10
6. [OpenAI 通过内核优化将 GPT-5.6 Luna 成本降低 80%](#item-6) ⭐️ 8.0/10
7. [GitHub 堆叠 PR 公开预览上线](#item-7) ⭐️ 7.0/10
8. [AI 辅助重构的经济效益量化分析](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [多工具插件市场统一六大 AI 编码代理](https://github.com/wshobson/agents) ⭐️ 9.0/10

开源项目 wshobson/agents 推出了一个多工具代理插件市场，允许技能在 Claude Code、Codex CLI、Cursor、OpenCode、GitHub Copilot 和 Gemini CLI 之间运行，从单一 Markdown 源生成各工具原生工件。 该项目通过提供统一的插件系统解决了 AI 编码工具的碎片化问题，使开发者能够跨不同代理框架共享和复用技能而无需重写，从而显著提高生产力和生态系统互操作性。 该市场使用模型上下文协议（MCP）作为底层标准，每个适配器生成工具原生工件而非最低公分母翻译，确保与每个工具的最佳集成。

github · wshobson · 7月22日 15:32

**背景**: 模型上下文协议（MCP）是 Anthropic 提出的开放标准，用于将 AI 代理连接到数据库、代码仓库等外部系统。Claude Code、OpenAI Codex CLI、Cursor、OpenCode、GitHub Copilot 和 Gemini CLI 是流行的 AI 编码代理，各自拥有自己的插件或扩展系统。wshobson/agents 提供了一个统一的市场，允许一次编写的技能在所有这些工具上运行，利用 MCP 实现互操作性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wshobson/agents">wshobson/agents: Multi - harness agentic plugin marketplace for...</a></li>
<li><a href="https://opensourceai.tech/project/wshobson-agents.html">agents — Multi - harness agentic plugin marketplace ... | OpenSourceAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#agentic-ai`, `#developer-tools`, `#open-source`, `#mcp`, `#coding-agents`

---

<a id="item-2"></a>
## [OpenMontage：首个开源智能体视频制作系统](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10

OpenMontage 作为首个开源智能体视频制作系统发布，它将 AI 编码助手转变为完整的视频制作工作室，提供 12 条流水线、100 多个工具以及 700 多个智能体技能和生产知识文件。 该项目通过允许开发者使用自然语言或代码生成视频，将 AI 智能体与 FFmpeg、Remotion 等传统工具相结合，大幅降低了视频制作的门槛。它代表了一种新范式：AI 编码助手可以自主编排复杂的多媒体工作流。 OpenMontage 基于 Remotion（一个基于 React 的程序化视频创建框架）构建，并集成了多个 AI 模型，包括 Stable Diffusion、Flux 和 ElevenLabs，用于图像生成、文本转语音和视频生成。该系统使用 Python 编写，支持 Claude、Copilot 和 Cursor 等智能体。

github · calesthio · 7月24日 19:25

**背景**: 智能体 AI 指的是能够通过编排多个工具和模型来自主规划和执行复杂任务的 AI 系统。Remotion 是一个开源框架，允许开发者使用 React、CSS、Canvas 和 SVG 以编程方式创建视频。OpenMontage 结合了这些概念，让 AI 智能体利用超过 700 个技能文件库来协调视频制作流水线，从故事板到最终渲染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/calesthio/OpenMontage">GitHub - calesthio/OpenMontage: World&#x27;s first open-source, agentic ...</a></li>
<li><a href="https://www.remotion.dev/">Remotion | Make videos programmatically</a></li>
<li><a href="https://openmontage.video/">OpenMontage — open-source agentic video production</a></li>

</ul>
</details>

**标签**: `#video-generation`, `#agentic-ai`, `#open-source`, `#python`, `#developer-tools`

---

<a id="item-3"></a>
## [AI 代理营销技能提示仓库获 4.2 万星](https://github.com/coreyhaines31/marketingskills) ⭐️ 8.0/10

GitHub 仓库 coreyhaines31/marketingskills 为 Claude Code 和 Codex 等 AI 编码代理提供营销技能提示，目前已获得 42,437 颗星，并持续更新维护。 该仓库弥合了营销专业知识与 AI 代理能力之间的差距，使开发者能够将转化率优化、文案撰写、SEO、分析和增长工程直接融入其 AI 驱动的工作流程。其高星数和活跃开发反映了社区对 AI 代理领域特定提示的强烈兴趣。 该仓库主要使用 JavaScript 编写，拥有 6,686 个分支和 85 个未解决问题，最近一次推送是在 2026 年 7 月 29 日。它涵盖多个营销学科，包括 CRO、文案撰写、SEO、分析和增长工程。

github · coreyhaines31 · 7月29日 05:41

**背景**: Claude Code 和 OpenAI Codex 是能够通过提示自主执行任务的 AI 编码代理。CRO（转化率优化）专注于提高网站上执行所需操作的用户百分比，而增长工程则将技术技能与营销策略相结合，推动可扩展的增长。该仓库提供了即用型提示，使这些 AI 代理能够执行营销相关任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.shopify.com/ae/blog/19-cro-growth-expert-tips">CRO Expert Tips: 19 Growth Pros on Optimization - Shopify UAE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_%28AI_agent%29">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://github.com/Piebald-AI/claude-code-system-prompts">GitHub - Piebald-AI/claude-code-system-prompts: All parts of Claude Code&#x27;s system prompt, 27 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation). Updated for each Claude Code version. · GitHub</a></li>

</ul>
</details>

**标签**: `#claude`, `#codex`, `#ai-agents`, `#marketing`, `#open-source`

---

<a id="item-4"></a>
## [用三万两千星的 Agent 技能去除 AI 写作痕迹](https://github.com/blader/humanizer) ⭐️ 8.0/10

blader/humanizer 仓库已获得超过 32,211 个星标，提供了一个专门用于去除文本中 AI 生成写作痕迹的 Agent 技能。 随着 AI 生成文本的普及，该工具为开发者和写作者提供了一种绕过检测、恢复更自然人类写作风格的实用方法，直接回应了 AI 辅助写作生态中日益增长的需求。 该项目在 2026 年 7 月仍有近期提交，处于活跃维护状态，支持与 Codex、Cursor 和 Claude Code 等 AI 代理集成，拥有超过 2,900 个复刻和仅 13 个未解决问题。

github · blader · 7月22日 06:26

**背景**: AI 写作模型会留下可检测的痕迹模式，例如过度使用某些过渡词或过于平衡的句子结构。Agent 技能是可复用的指令，用于指导 AI 助手执行特定任务，而 blader/humanizer 正是这样一个技能，用于清理文本中的那些可识别标记。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/engineering/writing-tools-for-agents">Writing effective tools for AI agents—using AI agents \ Anthropic</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#ai-writing`, `#prompt-engineering`, `#claude-code`

---

<a id="item-5"></a>
## [Gemini Robotics 2 为机器人带来全身智能](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

Google DeepMind 发布了 Gemini Robotics 2，该模型整合了全身智能，能够控制人形机器人进行流畅协调的动作。它从之前的仅上半身控制扩展到全身协调、高级灵巧操作以及多机器人协作。 这代表了向通用机器人迈出的重要一步，因为全身智能使机器人能够执行复杂任务，如在狭窄空间导航、双手操作物体以及从跌倒中恢复。它将大语言模型与物理动作连接起来，使机器人控制更自然、能力更强。 Gemini Robotics 2 使用一个视觉语言模型来理解环境，并使用两个视觉语言动作模型分别控制全身运动和手部灵巧操作。该模型可以同时协调多个机器人在共享环境中工作。

hackernews · ai2027 · 7月30日 15:15 · [社区讨论](https://news.ycombinator.com/item?id=49111237)

**背景**: 具身智能（Embodied AI）指的是通过传感器和执行器与物理世界交互的 AI 系统，它们从感官-运动经验中学习。之前的机器人模型通常只控制上半身，将任务局限于桌面操作。全身控制使得机器人能够利用整个身体——包括腿、躯干和手臂——实现更接近人类的运动和任务执行。Google DeepMind 的 Gemini 模型系列包括大语言模型（Gemini）、开放权重模型（Gemma），以及现在的机器人模型（Gemini Robotics）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body intelligence to robots — Google DeepMind</a></li>
<li><a href="https://deepmind.google/models/gemini-robotics/">Gemini Robotics 2</a></li>
<li><a href="https://www.engadget.com/2227268/google-gemini-robotics-2-platform-intelligent-whole-body-control/">Google&#x27;s new Gemini Robotics 2 platform allows for &#x27;intelligent whole-body control&#x27; - Engadget</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者既兴奋又持怀疑态度。一位 DeepMind 研究员证实了实验室的可信度，并强调了 DeepMind 在前沿模型、开放模型、科学和机器人等领域的广泛工作。其他评论者指出机器人动作仍然比人类慢，但将其与早期看起来笨拙的 LLM 相提并论。一些评论者由于机械执行器的限制而对人形机器人持怀疑态度，建议采用基因改造生物体等替代方法。

**标签**: `#robotics`, `#Google DeepMind`, `#Gemini`, `#AI models`, `#embodied AI`

---

<a id="item-6"></a>
## [OpenAI 通过内核优化将 GPT-5.6 Luna 成本降低 80%](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) ⭐️ 8.0/10

OpenAI 发布了 GPT-5.6 Luna，这是其最快、最便宜的模型，通过内核级改进和令牌生成效率提升，成本降低 80%，推理速度更快。 这种显著的性价比提升标志着 AI 推理成本下降的新阶段，使开发者能够以更低的成本运行更复杂的智能体工作流并扩展应用。这也加剧了 AI 提供商之间的竞争，惠及整个生态系统。 优化包括通过内核工作将端到端服务成本降低 20%，令牌生成效率提升 15%，综合效果使总成本降低 80%。该模型原本就被认为能力很强且价格低廉，此次变化堪称数量级飞跃。

hackernews · OpenAI News · 7月30日 17:15 · [社区讨论](https://news.ycombinator.com/item?id=49112867)

**背景**: LLM 推理成本主要由 GPU 计算时间、内存带宽和服务基础设施决定。内核优化——例如融合操作、减少内存访问和提高并行性——直接降低了这些成本。OpenAI 的内核工作可能针对底层 CUDA 优化，类似于 vLLM 和其他推理引擎使用的技术。随着提供商投资推理效率，整个行业出现了快速的价格下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dl.acm.org/doi/10.1145/3617689">Improving Computation and Memory Efficiency for Real-world Transformer Inference on GPUs | ACM Transactions on Architecture and Code Optimization</a></li>
<li><a href="https://www.runpod.io/blog/llm-inference-optimization-techniques-reduce-latency-cost">LLM inference optimization: techniques that actually reduce latency and cost</a></li>
<li><a href="https://www.datacamp.com/blog/ai-cost-optimization">Top 10 Methods to Reduce LLM Costs | DataCamp</a></li>

</ul>
</details>

**社区讨论**: 评论者对价格降幅之大表示惊讶和兴奋，有人将其比作从拨号上网到宽带的过渡。几位评论者指出模型选择（为每个任务选择合适模型）的挑战，并强调了以相同成本运行更多样本和智能体的潜力。

**标签**: `#openai`, `#gpt-5.6`, `#inference-optimization`, `#pricing`, `#llm-deployment`

---

<a id="item-7"></a>
## [GitHub 堆叠 PR 公开预览上线](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) ⭐️ 7.0/10

GitHub 已公开发布堆叠式拉取请求（Stacked PRs）预览版，允许开发者创建和管理相互依赖的 PR 堆栈。该功能现已面向所有用户开放试用。 这是一项重大的工作流程变革，使开发者能够进行更小、更渐进的代码审查，减少合并冲突并提高审查效率。它可能从根本上改变团队在 GitHub 上进行代码审查和协作的方式。 该功能仍处于公开预览阶段，存在已知问题，例如堆栈合并功能在某些情况下完全失效，以及使用压缩合并时需要重新审批。GitHub 团队称这是公司历史上规模最大的发布之一，涉及 Actions 等多个服务。

hackernews · tomzorz · 7月30日 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49112232)

**背景**: 堆叠式拉取请求是一种工作流程，将一系列小型、相互依赖的变更堆叠在一起，每个变更作为一个独立的 PR。这允许进行增量审查和更快的迭代，与传统的将所有变更放在一个大型 PR 中的功能分支工作流形成对比。这种方法在大型代码库和优先考虑快速、安全代码变更的团队中很受欢迎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.git-tower.com/blog/stacked-prs">Understanding the Stacked Pull Requests Workflow | Tower Blog</a></li>
<li><a href="https://www.graphite.com/guides/stacked-diffs">Stacked diffs</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，知名开发者 steveklabnik 称这是 GitHub 多年来最大的变化之一。但也有用户报告了严重问题，如合并整个堆栈功能损坏，以及压缩合并需要重新审批，部分用户对在未修复这些 bug 的情况下扩大预览范围表示惊讶。GitHub 团队成员正在积极收集反馈并承诺更多更新。

**标签**: `#github`, `#stacked-prs`, `#developer-tools`, `#workflow`, `#version-control`

---

<a id="item-8"></a>
## [AI 辅助重构的经济效益量化分析](https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html) ⭐️ 7.0/10

Martin Fowler 的文章基于实际使用指标，而非模糊评论，对使用 AI 进行代码重构的经济效益进行了量化分析。 这为 AI 辅助开发提供了具体、数据驱动的视角，帮助开发者和管理者就采用 AI 工具进行重构做出明智决策，并超越了推测性或轶事式的讨论。 该分析基于 AI 编码工具在重构任务中的实际使用情况，衡量了实际的生产力提升，例如减少的 token 消耗和节省的时间。

hackernews · javaeeeee · 7月30日 15:10 · [社区讨论](https://news.ycombinator.com/item?id=49111176)

**背景**: 代码重构是在不改变外部行为的前提下重组现有代码的过程，通常旨在提高可读性、可维护性或性能。AI 大语言模型越来越多地被用于辅助编码任务，但它们在重构等活动中的经济价值一直不明确。这篇文章通过实际使用中的定量证据填补了这一空白。

**社区讨论**: 评论者指出一种讽刺现象：公司中常被忽视的编程最佳实践如今被重新发明给 AI 使用，并称赞该文章立足实际、量化分析。一些人强调，人类监督仍然不可或缺，因为 AI 缺乏对整体项目背景的理解，尤其是在出于优雅性或冗余性进行重构时。

**标签**: `#refactoring`, `#AI-assisted development`, `#software engineering`, `#productivity`

---