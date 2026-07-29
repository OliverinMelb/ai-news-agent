---
layout: default
title: "Horizon Summary: 2026-07-29 (ZH)"
date: 2026-07-29
lang: zh
---

> 从 88 条内容中筛选出 10 条重要资讯。

---

1. [Superpowers：拥有 26 万星的开源智能体技能框架](#item-1) ⭐️ 8.0/10
2. [Graphify 无需向量数据库，将代码库转化为可查询知识图谱](#item-2) ⭐️ 8.0/10
3. [多平台研究技能在 GitHub 上获得 55000+ 星标](#item-3) ⭐️ 8.0/10
4. [CowAgent：开源 AI 智能体框架，一行命令安装](#item-4) ⭐️ 8.0/10
5. [2GB 内存运行 Gemma 4 26B：M 系列 Mac 开源引擎](#item-5) ⭐️ 8.0/10
6. [OpenAI Codex rust-v0.146.0 新增 Agent 插件、线程分支和 WebSocket 远程执行](#item-6) ⭐️ 7.0/10
7. [Kimi K3-256k 将 256k 以下上下文的配额消耗减半](#item-7) ⭐️ 7.0/10
8. [AI 蠕虫通过隐藏指令在 Word Copilot 中自我复制](#item-8) ⭐️ 7.0/10
9. [Claude Code PreToolUse 钩子强制执行项目工具规则](#item-9) ⭐️ 7.0/10
10. [GitHub Copilot 代码审查现已支持代理技能和 MCP](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Superpowers：拥有 26 万星的开源智能体技能框架](https://github.com/obra/superpowers) ⭐️ 8.0/10

GitHub 仓库 obra/superpowers 已获得 263,241 颗星和 23,507 个复刻，提供了一个用于 AI 辅助编程的开源智能体技能框架及软件开发方法论。 凭借极高的社区参与度，该项目显示出开发者对于 AI 编码的结构化、智能体驱动工作流的强烈兴趣，可能影响团队在软件开发生命周期中采用 AI 的方式。 该仓库主要使用 Shell 编写，有 332 个未关闭议题且近期有提交，表明其维护活跃，并专注于为 AI 编码智能体提供实用的、可脚本化的技能。

github · obra · 7月28日 19:25

**背景**: 该项目引入了“智能体技能”的概念——即可复用、可组合的能力，AI 编码智能体可以执行这些能力，例如头脑风暴、编码或软件开发生命周期任务。它还定义了“子智能体驱动开发”方法论，将任务分解并委托给专门的子智能体，从而实现更结构化、可扩展的 AI 辅助开发。

**标签**: `#AI`, `#agentic-skills`, `#software-development-methodology`, `#agent-framework`, `#open-source`

---

<a id="item-2"></a>
## [Graphify 无需向量数据库，将代码库转化为可查询知识图谱](https://github.com/Graphify-Labs/graphify) ⭐️ 8.0/10

拥有超过 98,000 颗 GitHub 星星的 Graphify-Labs/graphify 现在允许开发者通过 tree-sitter 的确定性 AST 解析，将任何代码库（包括文档、SQL 模式、配置文件和 PDF）转化为可查询的知识图谱。它作为一项技能集成了 Claude Code、Cursor、Codex、Gemini CLI 及 15 个以上其他 AI 编程助手。 该工具在不依赖昂贵向量存储或大模型调用来获取结构的情况下，弥合了 AI 编程助手与深度代码理解之间的鸿沟。通过提供可解释的确定性关系，它使得跨多个流行平台的代码搜索、重构和上下文感知的代理行为更加可靠。 所有代码解析均在本地通过 tree-sitter AST 完成，意味着数据不会离开机器；只有文档、PDF、图片和视频可能使用助手的模型。该图谱还可以通过 Leiden 社区检测算法进行可选的层次聚类增强，并且在 Claude Code 中的“严格模式”会强制助手实际使用该图谱。

github · Graphify-Labs · 7月29日 16:34

**背景**: 知识图谱将实体及其关系表示为网络，使查询诸如“哪些函数调用了这个 API”之类的连接变得容易。Tree-sitter 是一个解析器生成器，它能确定性地构建具体语法树，与基于概率模型的大语言模型提取方式不同。Leiden 算法是一种社区检测方法，用于对相关节点进行分组以提供层次化概览，常用于 GraphRAG 系统中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Graphify-Labs/graphify">GitHub - Graphify -Labs/ graphify : Turn any codebase, with its docs...</a></li>
<li><a href="https://arxiv.org/html/2601.08773">Reliable Graph -RAG for Codebases: AST -Derived Graphs vs...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leiden_algorithm">Leiden algorithm - Wikipedia</a></li>

</ul>
</details>

**标签**: `#knowledge-graph`, `#code-analysis`, `#ai-agents`, `#developer-tools`, `#ast-parsing`

---

<a id="item-3"></a>
## [多平台研究技能在 GitHub 上获得 55000+ 星标](https://github.com/mvanhorn/last30days-skill) ⭐️ 8.0/10

GitHub 仓库 &#x27;mvanhorn/last30days-skill&#x27; 已获得超过 55000 个星标，提供一种 AI 智能体技能，可在 Reddit、X、YouTube、Hacker News、Polymarket、Instagram、TikTok、Bluesky 以及网络上研究任何主题，然后综合生成有依据的摘要。 这一技能为开发者提供了一个实用且可检查的模板，用于构建多来源研究智能体，显著降低了创建利用实时网页和社交媒体数据的、有依据的 AI 摘要工具的门槛。 该技能设计用于 Anthropic 的 Claude Code 环境，使用 Python 编写，截至 2026 年 7 月 28 日的最新推送，已有 4756 个复刻和 83 个未解决问题。

github · mvanhorn · 7月28日 21:16

**背景**: Claude Code 是 Anthropic 的命令行工具，用于 AI 辅助编程。技能是可重用的指令包，教 AI 智能体如何处理特定任务。ClawHub 是一个智能体技能注册中心，可以发现像这样的社区贡献的技能。Polymarket 是一个预测市场平台，用户可以在上面交易事件结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ComposioHQ/awesome-claude-skills">GitHub - ComposioHQ/awesome- claude - skills : A curated list of...</a></li>
<li><a href="https://clawhub.ai/">ClawHub</a></li>
<li><a href="https://polymarket.com/">Polymarket | The World&#x27;s Largest Prediction Market</a></li>

</ul>
</details>

**标签**: `#ai-skill`, `#claude`, `#research`, `#web-search`, `#ai-prompts`

---

<a id="item-4"></a>
## [CowAgent：开源 AI 智能体框架，一行命令安装](https://github.com/zhayujie/CowAgent) ⭐️ 8.0/10

zhayujie/CowAgent 仓库（原名 chatgpt-on-wechat）已获得超过 46,000 颗星，成为一个开源超级 AI 助手和智能体框架，支持多模型、多通道、工具使用、记忆和技能，并提供一行命令安装。 CowAgent 的流行和积极开发使其成为探索 AI 智能体基础设施的开发者的关键资源，提供了一个实用、可扩展的框架，集成多种模型和通道。 CowAgent 支持模型上下文协议（MCP）进行工具集成，包含多智能体能力，并具有自我进化的记忆和知识。它设计为轻量级且可扩展，提供一行命令安装。

github · zhayujie · 7月29日 07:13

**背景**: 智能体框架（Agent Harness）是包裹在大语言模型（LLM）周围的基础设施层，提供记忆、工具和防护措施，使智能体能够完成任务。模型上下文协议（MCP）是一个开放标准，为 AI 系统连接数据源和工具提供通用方式，取代碎片化的集成。CowAgent 利用这些概念，提供了一个灵活、多模型的智能体平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>
<li><a href="https://www.domo.com/glossary/agent-harness">What Is an Agent Harness ? Definition and Key Components</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Agent Harness`, `#Open Source`, `#Python`, `#MCP`

---

<a id="item-5"></a>
## [2GB 内存运行 Gemma 4 26B：M 系列 Mac 开源引擎](https://github.com/drumih/turbo-fieldfare) ⭐️ 8.0/10

TurboFieldfare 是一个开源的 Swift/Metal 推理引擎，通过从 SSD 流式传输路由专家，在任何 M 系列 Mac 上仅用约 2GB 内存运行 4-bit Gemma 4 26B 模型。在 M1 MacBook Air 上达到 5-6 tok/s，在 M5 MacBook Pro 上达到 31-35 tok/s。 这种方法让内存受限的 Apple 硬件也能运行大型模型，使拥有 8GB 或 16GB 内存 Mac 的用户可以运行传统工具无法加载的 14GB 模型，无需昂贵升级即可体验设备端 AI。 模型的 4-bit 量化权重约 14GB，但引擎仅将共享层和 KV 缓存保留在 RAM 中，每次 token 只从 SSD 流式传输所需专家，使用有界并行 pread。还包括一个实验性的 OpenAI 兼容服务器，支持流式输出和工具调用。

hackernews · gitpusher42 · 7月29日 15:05 · [社区讨论](https://news.ycombinator.com/item?id=49098510)

**背景**: Mixture of Experts \(MoE\) 模型包含多个专家子网络，每个 token 只激活其中一部分，因此可以按需加载专家权重。4-bit 量化将模型参数精度从 32 位降至 4 位，大幅减少内存占用。传统推理工具需要将整个模型加载到 RAM，而 TurboFieldfare 借鉴了 Flash-MoE 等项目的思路，将共享层常驻内存，专家权重从 SSD 按需流式传输，从而在低内存设备上运行大模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/mixture-of-experts-moe">What Is Mixture of Experts ( MoE )? How It Works, Use... | DataCamp</a></li>
<li><a href="https://huggingface.co/blog/4bit-transformers-bitsandbytes">Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA</a></li>
<li><a href="https://insiderllm.com/guides/flash-moe-run-397b-model-laptop/">Flash-MoE: Run a 397B Model on a 48GB Laptop... | InsiderLLM</a></li>

</ul>
</details>

**社区讨论**: 社区评论中，有用户指出这是第二次看到该项目，并质疑为何必须全量加载模型；有人提供了在 macOS 15 上编译的兼容性提示；另有人将该项目与 llama.cpp 的 mmap 方式对比，认为主要区别在于同步 SSD 读取与推理活动；还有用户正在开发 DiffusionGemma，表示可能合作优化内核。整体氛围积极，关注技术实现细节。

**标签**: `#on-device AI`, `#inference engine`, `#Mac`, `#MoE`, `#Gemma`

---

<a id="item-6"></a>
## [OpenAI Codex rust-v0.146.0 新增 Agent 插件、线程分支和 WebSocket 远程执行](https://github.com/openai/codex/releases/tag/rust-v0.146.0) ⭐️ 7.0/10

OpenAI 发布了 Codex 的 rust-v0.146.0 版本，引入了基于清单文件的 Agent 插件支持、带分页历史和临时分支的线程分支功能，以及用于将 app-server 连接到远程 Code Mode 主机的 WebSocket 远程执行。该版本还修复了认证、插件下载、MCP 授权和远程执行等多个环节的代理配置问题。 Agent 插件允许开发者通过 Amazon Bedrock 和 Claude Code 等市场的自定义技能来扩展 Codex，使其成为一个更灵活、由插件驱动的发展平台。结合线程分支和 WebSocket 远程执行，该版本显著改善了多会话工作流以及在远程主机上运行代理的能力。 该版本在包括 MCP 授权和远程执行在内的六个领域遵循配置的代理设置，并在认证发生变化时保持 MCP 连接最新，无需重启健康连接。线程分支支持分页历史，临时分支不会出现在线程列表中。

github · github-actions\[bot\] · 7月29日 01:42

**背景**: Codex 是 OpenAI 的 AI 编程代理，能够自主规划和执行软件开发任务。Agent 插件是由 manifest 文件 \(plugin.json\) 定义的模块化技能包，为代理配备特定领域的能力；模型上下文协议 \(MCP\) 是将外部工具和数据源与 AI 代理集成的标准。WebSocket 远程执行使开发者能够在远程机器上运行 Codex app-server，同时通过本地终端 UI 进行交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/agent-toolkit/latest/userguide/plugins.html">Plugins - Agent Toolkit for AWS</a></li>
<li><a href="https://github.com/awslabs/agent-plugins">GitHub - awslabs/agent-plugins: Agent Plugins for AWS equip AI coding agents with the skills to help you architect, deploy, and operate on AWS. · GitHub</a></li>
<li><a href="https://codex.danielvaughan.com/2026/03/31/codex-cli-app-server-remote-websocket/">Codex CLI App Server: Remote Access, WebSocket Transport, and Headless Deployment | Codex Knowledge Base</a></li>

</ul>
</details>

**标签**: `#codex`, `#mcp`, `#agent-plugins`, `#developer-tools`, `#github-release`

---

<a id="item-7"></a>
## [Kimi K3-256k 将 256k 以下上下文的配额消耗减半](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 7.0/10

Kimi（月之暗面）发布了 K3 模型的新变体 K3-256k，提供 256k token 的上下文窗口，对于不超过 256k 的输入，其配额消耗约为原 1M 版本的一半。 这直接降低了不需要完整 1M 上下文的开发者的 API 成本，使 Kimi K3 在 LLM API 市场中更具竞争力。这反映了提供分层上下文窗口以优化推理支出的趋势。 K3-256k 变体在 256k 上下文窗口内提供与 1M 版本相同的结果。原版 K3 模型拥有 1,048,576 token 的上下文窗口，输入 token 价格为每百万 $3，输出 token 价格为每百万 $15。

hackernews · monneyboi · 7月29日 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49101852)

**背景**: 上下文窗口是 LLM 一次可以处理的最大文本量，以 token 为单位。Kimi K3 是月之暗面推出的 2.8 万亿参数开源多模态推理模型，默认拥有 1M token 的上下文窗口。新的 K3-256k 变体提供了更小的上下文窗口，成本更低，适合不需要完整 1M 容量的用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Context_window">Context window - Wikipedia</a></li>
<li><a href="https://artificialanalysis.ai/models/kimi-k3">Kimi K3 - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: HN 评论普遍积极，指出 256k 通常足够使用，价格降低意义重大。有评论者称 Kimi 突然对所有 256k 以下用户半价是‘巨大的’。还有人评论说 LLM 正在变成商品，美国 AI 实验室正在失去护城河。

**标签**: `#LLM`, `#API pricing`, `#context window`, `#Kimi`, `#AI developer tools`

---

<a id="item-8"></a>
## [AI 蠕虫通过隐藏指令在 Word Copilot 中自我复制](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 7.0/10

研究员 Håkon Måløy 发现了一种新的提示注入变体，可将 Microsoft Word Copilot 转变为自我复制的蠕虫。攻击者将隐藏指令嵌入文档中，使 Copilot 将指令复制到新文档中，并在这些文档被再次使用时传播攻击。 这是首次针对企业生产力工具（如 Microsoft Word Copilot）的自复制 AI 蠕虫的演示。它表明提示注入攻击可以超越数据窃取，实现蠕虫式传播，这给依赖 AI 辅助文档工作流的组织带来了严重的安全隐患。 该攻击使用白底白字的隐藏文本（一种已知的求职申请技术）来隐藏指令，指示 Copilot 操纵当前文档并将隐藏指令复制到输出中。Måløy 在 144 天前已负责任地向 Microsoft 披露了漏洞，但 Microsoft 尚未发布能完全覆盖此类攻击的修复。

rss · Simon Willison · 7月29日 18:43

**背景**: 提示注入攻击利用了大语言模型无法区分开发者定义的指令和用户提供的内容的弱点。在这个变体中，恶意指令被放置在 Copilot 作为源材料读取的文档中，从而有效绕过了预期防护措施。之前的自复制 AI 蠕虫（如 Morris II）针对的是邮件助手，但这是首个针对 Microsoft Word Copilot 的案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://thehackernews.com/2026/06/researchers-build-self-replicating-ai.html">Researchers Build Self - Replicating AI Worm That Operates Entirely...</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#security`, `#Microsoft Word`, `#Copilot`, `#AI worm`

---

<a id="item-9"></a>
## [Claude Code PreToolUse 钩子强制执行项目工具规则](https://www.reddit.com/r/ClaudeCode/comments/1va4x2n/spent_months_ignoring_claude_code_hooks_set_them/) ⭐️ 7.0/10

一位开发者分享了如何利用 Claude Code 的 PreToolUse 钩子阻止不想要的工具调用，例如在 pnpm 管理的仓库中使用 npm，只需返回一个简单的 JSON 响应，代理会读取并执行。该帖子还介绍了一个 Stop 钩子，在移交完成的工作之前运行 TypeScript 类型检查。 这一发现通过让开发者强制执行项目特定约束而无需手动监督，使 Claude Code 在实际项目中更加可靠。它还凸显了钩子在代理定制方面的强大功能，尤其是对于即将推出的 Opus 5 模型，该模型会产生更长的未监控工作序列。 PreToolUse 钩子通过标准输入接收工具名称和命令的 JSON 数据，可以通过退出码 2 并将原因打印到标准错误来阻止调用，或者返回包含拒绝决定的 JSON 对象。Stop 钩子必须设计为避免无限循环，在第一轮类型检查后放弃。

reddit · r/ClaudeCode · /u/techpotions · 7月29日 18:38

**背景**: Claude Code 钩子是附加到代理循环中事件的 shell 脚本，例如 PreToolUse（在工具调用之前）和 Stop（当代理完成任务时）。它们可以检查上下文并允许或阻止操作。pnpm 是一个快速、节省磁盘空间的 Node.js 包管理器，使用 pnpm-lock.yaml 文件，与 npm 混用可能导致问题。开发者的钩子检查锁文件并拒绝错误的包管理器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-code-hooks">Claude Code Hooks: A Practical Guide to Workflow Automation | DataCamp</a></li>
<li><a href="https://pnpm.io/">Fast, disk space efficient package manager | pnpm</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#hooks`, `#developer tooling`, `#agent customization`, `#workflow`

---

<a id="item-10"></a>
## [GitHub Copilot 代码审查现已支持代理技能和 MCP](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPUk5Hc0xPMmdNTjFFM0NfNkFvd0sxNVZaLVYzS2RqZGVpSHNpVW00bGFOZmFhNjlYMWhpeUZYWGRlZUVPUk1CVnY5Q2lscVVaeDZnYnR1X3Q5QnFyeVpnWGtGaHZyTXJZNDdjNUo0MUE2dDBTV3B0SjEtUkQ0N1pnbkEyMllreEo0dmtNU1lsZ3Fta3hDWGtVZzJFc0ltR3BpaUJyU2NRSkZidw?oc=5) ⭐️ 7.0/10

GitHub 宣布 Copilot 代码审查中的代理技能和模型上下文协议 \(MCP\) 现已全面可用，使开发者能够将自定义工具和数据源直接集成到审查流程中。 这一更新将 Copilot 代码审查从静态建议工具转变为动态、可扩展的代理，让团队能够自动化复杂的审查任务，例如检查安全漏洞或强制执行自定义编码标准，从而显著加快开发工作流程。 代理技能和 MCP 服务器必须在仓库中配置后，Copilot 代码审查才能使用它们，并且仅在审查相关代码时才会被调用。这意味着团队可以根据具体项目需求定制审查流程，而无需为每个拉取请求进行手动配置。

google\_news · The GitHub Blog · 7月29日 21:26

**背景**: MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，它规范了 AI 系统如何连接到外部工具和数据源，类似于 AI 应用的 USB-C 端口。GitHub Copilot 代码审查一直是用于自动在拉取请求中提供改进建议的热门功能，而新功能通过允许审查期间与外部服务（如数据库、问题跟踪器或自定义脚本）交互，使其更加强大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review">Using GitHub Copilot code review - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#code review`, `#MCP`, `#agent skills`, `#developer tools`

---