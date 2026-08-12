---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 90 条内容中筛选出 12 条重要资讯。

---

1. [Anthropic 官方 Agent Skills 仓库在 GitHub 获得 16.8 万星标](#item-1) ⭐️ 9.0/10
2. [Superpowers：27 万星标框架，为 AI 编程提供技能与子代理开发方法论](#item-2) ⭐️ 8.0/10
3. [Matt Pocock 的 skills 仓库：21.5 万星的可复用 agent 技能集合](#item-3) ⭐️ 8.0/10
4. [11.6 万星 AI 技能，助编码代理构建专业 UI/UX](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4 Pro 0813 在 OpenRouter 正式上线：百万上下文、低价但评价不一](#item-5) ⭐️ 8.0/10
6. [Qwen3.8-2.4T：2.4T 参数 MoE 大模型，95B 激活参数](#item-6) ⭐️ 8.0/10
7. [重放攻击可还原大模型 API 的加密思维链](#item-7) ⭐️ 8.0/10
8. [Agent Plugins 1.0 在 VS Code、Copilot CLI 和 Copilot 应用中发布](#item-8) ⭐️ 8.0/10
9. [llama.cpp b10369 新增 pocket-tts，CUDA 生成提速 80%](#item-9) ⭐️ 7.0/10
10. [Zed 推出 Delta，开启实时协作式 AI 智能体对话](#item-10) ⭐️ 7.0/10
11. [SL2T 手语 AI 首次登陆 Pixel 11 的 Gboard 和 Live Transcribe](#item-11) ⭐️ 7.0/10
12. [LFM2.5-VL-3B：更快速、更强大的边缘端视觉语言模型](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 官方 Agent Skills 仓库在 GitHub 获得 16.8 万星标](https://github.com/anthropics/skills) ⭐️ 9.0/10

Anthropic 发布了官方公开仓库 anthropics/skills，提供一系列可直接用于 Claude 智能体的 Agent Skills。该仓库已获得 168,520 个星标和 20,075 个 fork，且最近一次推送时间是 2026-08-07，显示其仍在积极维护。 Agent Skills 是一种给 AI 智能体赋予专业技能的新开放格式，该仓库为开发者提供了一套官方、开箱即用的技能集合。凭借 16.8 万星标，它已成为 AI 智能体生态中最受关注的资源之一，并影响 Claude、Cursor、Codex 等工具的工作流。 一个技能本质上是一个包含 SKILL.md 文件及辅助资源的文件夹，技能设计为可组合、可移植，并能跨智能体使用。该仓库以 Python 为主，目前有 1,079 个未关闭 issue，反映出庞大且活跃的社区。

github · anthropics · 8月7日 17:14

**背景**: Agent Skills 是一种轻量级、开放的格式，用于通过专业知识和流程扩展 AI 智能体的能力。Claude 可以自动识别需要哪些技能并协调使用，而且同一格式可应用于 Claude Code、Agent SDK、API 以及越来越多的智能体产品。该仓库是 Anthropic 面向 Claude 的实现，更广泛的标准说明见 agentskills.io。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/skills">GitHub - anthropics/ skills : Public repository for Agent Skills · GitHub</a></li>
<li><a href="https://agentskills.io/">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://claude.com/blog/skills">Introducing Agent Skills | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#agent-skills`, `#Anthropic`, `#Claude`, `#AI-agents`, `#GitHub`

---

<a id="item-2"></a>
## [Superpowers：27 万星标框架，为 AI 编程提供技能与子代理开发方法论](https://github.com/obra/superpowers) ⭐️ 8.0/10

开源 GitHub 仓库 obra/superpowers 是一个面向 AI 编程代理的智能体技能框架与软件开发方法论，目前已获得超过 27.1 万颗星标。它提供可组合的技能模块和子代理驱动开发流程，适用于 Claude Code、Cursor、Codex、OpenCode 和 Gemini CLI 等工具。 随着 AI 编码代理逐渐成为主流，一个由社区支持、用于规范技能与执行流程的框架，能够显著提升 AI 生成代码的可靠性与一致性。该项目的迅速普及表明，业界对智能体软件开发中的结构化指导存在强烈需求。 该仓库主要使用 Shell 编写，包含 writing-skills（编写技能）和 using-superpowers（使用技能系统）等技能模块，其中较有代表性的是子代理驱动开发技能：为每个任务派发全新的实现子代理，并进行两阶段审查。仓库最近一次推送在 2026 年 8 月，目前有 317 个未关闭问题和超过 2.4 万个 fork。

github · obra · 8月12日 22:31

**背景**: 智能体技能框架为 AI 代理提供可复用、可组合的指令与工作流，使其能够完成复杂任务，类似于传统软件中插件的作用。子代理驱动开发方法论主张将任务委派给具有隔离上下文的专业代理，而不是让单个代理包办一切，这有助于管理上下文长度限制并提升代码质量。该项目是围绕 AI 编码助手形成的更广泛工具生态的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Superpowers_agentic_skills_framework">Superpowers (agentic skills framework)</a></li>
<li><a href="https://github.com/obra/superpowers">GitHub - obra/superpowers: An agentic skills framework &amp; software...</a></li>
<li><a href="https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md">superpowers/skills/ subagent - driven - development /SKILL.md at main...</a></li>

</ul>
</details>

**标签**: `#ai`, `#coding-agents`, `#skills`, `#sdlc`, `#github`

---

<a id="item-3"></a>
## [Matt Pocock 的 skills 仓库：21.5 万星的可复用 agent 技能集合](https://github.com/mattpocock/skills) ⭐️ 8.0/10

Matt Pocock 的 GitHub 仓库 skills 已获得超过 21.5 万个 Star，收录了来自他 .agents 目录的、面向工程师的可复用 agent 技能。仓库最近一次推送时间为 2026 年 8 月 7 日。 这验证了将 agent 技能作为社区驱动生态进行共享的趋势。开发者只需一条命令就能安装技能，增强 Codex、Claude 等编码 agent 的能力。 这些技能主要用 Shell 编写，仓库已有超过 1.8 万个 fork，说明社区活跃复用。一个技能通常是包含 SKILL.md 文件的文件夹，可能包含脚本、模板、示例和领域说明。

github · mattpocock · 8月7日 15:50

**背景**: .agents 目录是一种提议的约定，用于在代码库中放置 agent 专用资源。它与 AGENTS.md 互补，后者相当于面向 AI 编码 agent 的 README；.agents 还可以把 MCP 工具、技能、记忆和配置等统一放在一个目录中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bgreenwell/dotagents">GitHub - bgreenwell/dotagents: A proposed convention for the .agents/ directory to prevent context bloat and improve agent reasoning in complex codebases. · GitHub</a></li>
<li><a href="https://agents.md/">AGENTS.md</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#developer tools`, `#skills`, `#GitHub`, `#coding agents`

---

<a id="item-4"></a>
## [11.6 万星 AI 技能，助编码代理构建专业 UI/UX](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) ⭐️ 8.0/10

nextlevelbuilder/ui-ux-pro-max-skill 仓库在 GitHub 上获得超过 11.6 万星标，成为最受欢迎的 AI 技能之一。它为 Claude Code、Codex 和 Cursor 等编码代理提供设计智能，使其能够跨多个平台构建专业 UI/UX。 这标志着 AI 编码代理现在无需人工设计干预即可生成高质量、专业外观的用户界面，大大加速了前端开发。它使缺乏设计专业知识的开发者也能获得 UI/UX 设计能力，而大规模采用表明社区认可度极高。 该技能使用 Python 编写，支持 Claude Code、Codex、Copilot、Cursor、Trae 和 Windsurf AI 等多种 AI 编码代理。它处于活跃维护状态，有 80 个未关闭 issue，最近一次推送在 2026 年 8 月 12 日。

github · nextlevelbuilder · 8月12日 10:20

**背景**: AI 技能是一组 markdown 文件，用于指导 AI 编码代理如何编写更好的软件，在过去一年中作为开发者工具的新类别迅速流行起来。这个特定技能专注于 UI/UX 设计智能，为代理提供设计原则、组件库和平台特定的最佳实践，以生成专业界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill">GitHub - nextlevelbuilder/ui-ux-pro-max-skill: An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms · GitHub</a></li>
<li><a href="https://dev.to/aws/the-most-popular-ai-coding-skills-right-now-4183">The most popular AI coding skills right now - DEV Community</a></li>

</ul>
</details>

**标签**: `#AI skills`, `#UI/UX`, `#Claude Code`, `#coding agents`, `#design`

---

<a id="item-5"></a>
## [DeepSeek V4 Pro 0813 在 OpenRouter 正式上线：百万上下文、低价但评价不一](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek 于 2026 年 8 月 12 日在 OpenRouter 和自家 API 上发布了旗舰模型 V4 Pro 0813 的正式版（GA），这是一款拥有 100 万上下文窗口的混合专家模型，输入每百万 token 定价 0.435 美元、输出每百万 token 定价 0.87 美元。社区成员迅速贴出各自的基准测试以及与其他前沿模型在智能体编码任务上的对比。 这次发布为开发者提供了一个拥有 100 万 token 上下文窗口、价格比顶尖闭源模型便宜约 20 倍的替代选择，对 Anthropic Opus、xAI Grok 等竞品形成价格压力。社区的真实测试显示它竞争力很强但并非完美，因此团队需要在智能体工作流中权衡成本节省与可靠性。 该模型采用大规模混合专家架构，上下文窗口为 1,048,576 token，最大输出 384,000 token。社区一项 Codex CLI 测试中，V4 Pro 0813 完成功能开发耗时 12 分 02 秒、花费 0.12 美元但留下 bug；Grok 4.6 耗时 3 分 18 秒、花费 1.41 美元且无 bug；社区自测的 HLE 基准（不含工具）得分为 42.7，使用工具时为 60.0。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek V4 Pro 0813 是 DeepSeek 旗舰模型的正式发布版（GA），在预览阶段后于 2026 年 8 月 12 日上线，OpenRouter 和 DeepSeek API 文档均有收录。它采用混合专家（Mixture-of-Experts）架构——一种常见设计，每个 token 只激活部分参数以降低推理成本。OpenRouter 托管了众多前沿模型并提供实时排行榜，因此像 HLE（Humanity&#x27;s Last Exam）这样的社区基准成为快速比较不同模型价格与能力的常用方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves Preview – Unite.AI</a></li>
<li><a href="https://daily.dev/posts/deepseek-v4-pro-0813-b1mmdmajb">DeepSeek V4 Pro 0813 | daily.dev</a></li>

</ul>
</details>

**社区讨论**: HN 评论区态度谨慎乐观：有人称赞其价格比 Opus 4.8 便宜约 20 倍，但也指出其质量低于 Sol 或 Fable；有用户发现在 docker-compose 部署任务中它弱于 GPT-5.6-terra-high。开发者报告了 Codex CLI 测试中的明显成本-质量权衡（便宜但有 bug，对比 Grok 4.6 贵但干净），并对 GLM-5.2 和 Kimi-K3 的基准得分进行了比较。此外还有一条关于用 markdown SVG 渲染器模拟自行车链条的无关评论。

**标签**: `#DeepSeek`, `#LLM`, `#model release`, `#benchmarks`, `#OpenRouter`

---

<a id="item-6"></a>
## [Qwen3.8-2.4T：2.4T 参数 MoE 大模型，95B 激活参数](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 8.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一款混合专家（MoE）模型，总参数 2.4T，激活参数 95B，提供 BF16 和 FP8 两种精度版本。模型卡片声称其性能介于 Opus 4.5 与 Fable 5 之间。 这是 Qwen 在开源权重模型方面的一次重大发布，将大规模 MoE 模型的边界向前推进，让开发者能以远低于稠密 2.4T 模型的计算成本获得接近前沿的能力。这也加剧了中国 AI 实验室之间的竞争，尤其是与 Kimi k3 和 DeepSeek 的较量。 发布时仅提供 BF16 和 FP8 权重，完整 BF16 版本约需 4.9TB 存储；FP8 版本更小，据报道 1 比特量化版约 397GB。官方未提供 4 比特量化所需的 QAT（量化感知训练），因此可能需要社区自行用校准数据进行量化。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）架构每个 token 只激活一小部分参数，因此模型的总参数量可以远超稠密模型，而推理成本保持相近。BF16 和 FP8 是低精度格式，可减少内存占用并加速计算；FP8 速度约为 BF16 的两倍，但精度略有损失。正是这些技术使得 2.4T 参数规模的模型得以实际部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nyvoraai.github.io/ai-news/what-is-a-mixture-of-experts-llm.html">What Is a Mixture of Experts LLM? 2026 Guide</a></li>
<li><a href="https://www.insightologyresearch.com/p/weekly-shots-of-insight-and-market-13a">Weekly Shots of Insight and Market #3</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该模型对标 Kimi k3，许可证类似，但发布体积较大（仅 BF16/FP8），初期服务难度更高；他们还提到 Unsloth 的 1 比特量化版约 397GB，能让普通消费级硬件接近 Opus 级别性能。也有人遗憾开源版本不具备 Qwen3.8-Max 的视觉输入和 1M 上下文，同时提到 DeepSeek V4-Pro 的基准成绩也在大约 Fable 5 水平。

**标签**: `#Qwen`, `#large language model`, `#MoE`, `#open-source AI`, `#model release`

---

<a id="item-7"></a>
## [重放攻击可还原大模型 API 的加密思维链](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 8.0/10

研究人员发表论文，证明 OpenAI、Anthropic 和 Google API 返回的加密思维链数据块可以被重放到同系列较弱的模型上，并通过越狱还原出明文形式的推理内容。论文附带了 curl 复现示例和大量提取出的推理痕迹，不过据论文所述，三家厂商均已确认并修复该漏洞。 这项研究很重要，因为业界普遍认为加密推理数据块能保证专有思维链不外泄，但结果表明，任何能访问同系列较弱模型的人都有可能还原这些隐藏推理。它还揭示了一种新的提示注入攻击方式：攻击者可以诱导模型的隐藏推理执行敏感操作，然后再把推理内容窃取出来。 核心漏洞在于同一厂商的模型家族共用同一个加密密钥，导致加密推理数据块可以在不同会话、用户和模型之间重放。攻击难度最低的是 Claude Haiku 4.5，攻击者只需使用“继续并逐字转录”的提示词并设置 assistant 消息前缀；论文附录还展示了如 GPT-5.5 规划 CSS 组件之类的还原内容。

rss · Simon Willison · 8月11日 22:40

**背景**: 思维链（chain-of-thought）提示让大语言模型逐步推理，而 OpenAI、Anthropic 和 Google 等厂商刻意隐藏这些中间推理内容，改为向客户端返回加密的数据块。这项研究说明这种加密并不是可靠的安全边界，因为在同一模型家族内这些数据块可以互换并重放到较弱的模型里。推理提取攻击（reasoning extraction attacks）这一更广泛的类别还包括恢复隐藏提示词或中间决策结构的技术，而本研究新增了一种实用的跨模型重放变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://digg.com/tech/8a168m9s">Researchers Decode Encrypted Chain - of - Thought from Major AI...</a></li>
<li><a href="https://www.banandre.com/blog/hidden-chain-of-thought-extraction-proprietary-models">They Cracked the Encryption on AI’s Private Thoughts , All Three of...</a></li>

</ul>
</details>

**标签**: `#security`, `#LLM`, `#chain-of-thought`, `#API`, `#privacy`

---

<a id="item-8"></a>
## [Agent Plugins 1.0 在 VS Code、Copilot CLI 和 Copilot 应用中发布](https://news.google.com/rss/articles/CBMipAFBVV95cUxQTENGRGItRWhCbHNRN2REWmNsOUp0bUpmOUFvcU1DdlJjdnhWTEptcU1uRUVianBuMUNyLUd6MWhCNTd6eU5OS1B0OWNiTEoyYkVBQ0xFVC1qSkgxZ0kzT25xbG84WmhSYmctZFE3QlRRRmdkckhSTlQ3NUZyalJfN1d5VUtqQ0pDblhoNldjN1p5M0ZPSWg1WmpkOFMwUVBWUzcwdg?oc=5) ⭐️ 8.0/10

GitHub 宣布了 Agent Plugins 1.0 的发布，这是一个新的插件系统，将 GitHub Copilot 的能力扩展到 VS Code、Copilot CLI 和 Copilot 应用中。该版本允许开发者创建自定义技能和指令，使 Copilot 能够作为自主编码代理运行。 Agent Plugins 1.0 标志着 AI 编码助手向更可扩展和更自主方向迈出的重要一步，允许开发者根据特定工作流和任务定制 Copilot。这可以通过自动化更复杂的多步编码操作来大幅提升开发者生产力。 Agent Plugins 支持自定义技能（任务特定的提示包）和自定义指令（通用指导），其中技能更适用于可复用的提示。该功能在所有 GitHub Copilot 计划（Free、Pro、Pro+、Max、Business 和 Enterprise）中均可使用。

google\_news · The GitHub Blog · 8月12日 18:39

**背景**: GitHub Copilot 是一款基于 OpenAI 大语言模型的 AI 编码助手，提供代码建议和基于聊天的帮助。Agent Plugins 扩展了 Copilot 的代理模式，允许开发者给出高级指令（例如“用 Astro 和 Sanity CMS 构建一个作品集网站”），然后由 Copilot 自主执行任务。Copilot CLI 将这些能力带到命令行，使得在终端中直接进行代理驱动的工作流成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat">GitHub Copilot Chat - Visual Studio Marketplace</a></li>
<li><a href="https://github.com/features/copilot/cli">GitHub Copilot CLI · GitHub</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Copilot`, `#Agent Plugins`, `#VS Code`, `#CLI`

---

<a id="item-9"></a>
## [llama.cpp b10369 新增 pocket-tts，CUDA 生成提速 80%](https://github.com/ggml-org/llama.cpp/releases/tag/b10369) ⭐️ 7.0/10

llama.cpp b10369 在 mtmd 多模态模块中新增了对 pocket-tts 文本转语音模型的支持，用 GEMM+col2im 重构了转置卷积。这使得每帧生成时间在 CUDA 上降低 80%，在 CPU 上降低 50%。 将轻量级 TTS 引入 llama.cpp，使该项目从单纯的文本生成扩展到统一的本地推理工具。实测的加速效果让实时端侧语音生成在 GPU 和 CPU 上都变得更加可行。 该优化把转置卷积折叠为 GEMM + col2im 运算，避免了每个通道一个图节点。输出与旧实现逐样本匹配，相关系数为 0.999994；新增的 frames\_after\_eos 等按语言包设置要求重新转换现有的 mmproj 文件。

github · github-actions\[bot\] · 8月12日 04:52

**背景**: llama.cpp 是一个流行的开源 C/C++ 推理引擎，用于在本地运行大型语言模型。pocket-tts 是一个轻量级、开源的 1 亿参数文本转语音模型。llama.cpp 中的 mtmd（多模态）模块负责处理视觉和音频输入，本次发布将其扩展为可以直接生成语音。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Pocket_TTS">Pocket TTS</a></li>
<li><a href="https://pockettts.org/">Pocket - TTS - Lightweight, Open-Source Text-to- Speech</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#text-to-speech`, `#inference-optimization`, `#multimodal`, `#release`

---

<a id="item-10"></a>
## [Zed 推出 Delta，开启实时协作式 AI 智能体对话](https://zed.dev/blog/introducing-delta) ⭐️ 7.0/10

Zed 发布了 Delta 功能，支持与 AI 智能体进行实时多人协作会话，并提供行内评论和“对话即文档”工作流。Delta 基于 DeltaDB 构建，为其新原语提供了集中的迭代场所。 这将 AI 辅助编程从单人、基于聊天的活动，转变为可协作、可审查的流程。它可能会改变团队指导初级开发者的方式，以及拉取请求讨论的进行方式。 DeltaDB 使用基于增量（delta）的本地存储来记录代码历史，使 AI 智能体能够理解代码库的演进过程，而不仅仅是最终状态。Delta 目前是一个集中测试这些原语的环境，DeltaDB 后续将集成到 Zed 中。

hackernews · khy · 8月12日 18:19 · [社区讨论](https://news.ycombinator.com/item?id=49276574)

**背景**: Zed 是一款注重协作功能的高性能代码编辑器。Delta 引入了一种新工作流，将智能体对话视为文档，支持行内评论和多人编辑。DeltaDB 是一种基于增量的存储引擎，记录每一次变更，为智能体理解代码提供更丰富的上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zed.dev/blog/introducing-delta">Introducing Delta — Zed &#x27;s Blog</a></li>
<li><a href="https://asibiont.com/en/blog/zed-deltadb-fishka-vibe-coding-kak-uskorit-razrabotku-v-10-raz">Zed DeltaDB: The Hidden Engine Behind Seamless... — ASI Biont Blog</a></li>
<li><a href="https://runtimewire.com/article/zed-deltadb-version-control-agent-conversations">Nathan Sobo&#x27;s Zed takes aim at pull requests with... - RuntimeWire</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一。有人认为多人协作与“对话即文档”功能对指导新人、审查 PR 生成过程很有用；也有人认为随着过去一年编码智能体的飞速进步，这一功能的价值已经下降。还有评论者抱怨博客页面对比度过低，以及 AI 生成代码摘要过于啰嗦。

**标签**: `#AI agents`, `#collaborative coding`, `#Zed`, `#developer tools`

---

<a id="item-11"></a>
## [SL2T 手语 AI 首次登陆 Pixel 11 的 Gboard 和 Live Transcribe](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 7.0/10

Google DeepMind 推出了全新的手语转文本模型 SL2T，并已将其用于 Gboard 和 Live Transcribe 中的新功能，首先在 Pixel 11 上提供，且无需额外付费。 这是手语 AI 首次直接集成到消费级产品中，为聋人和听障用户提供了更自然的交流方式。 SL2T 首先在 Pixel 11 上可用，预计后续支持更多设备；该模型由 Google DeepMind 和 Android 团队联合开发。

rss · Google DeepMind · 8月12日 14:01

**背景**: 手语是一种复杂且完整的视觉语言，拥有独立的语法和词汇，因此自动翻译难度很大。能将手语手势转换为文本的 AI 模型有望帮助聋人群体弥合沟通鸿沟，但在此之前，这类系统很少真正进入消费级产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/">Putting sign language AI into users’ hands — Google DeepMind</a></li>
<li><a href="https://promptowy.com/google-deepmind-sl2t-jezyk-migowy-na-tekst/">Google DeepMind tłumaczy język migowy na tekst</a></li>

</ul>
</details>

**标签**: `#AI`, `#sign language`, `#accessibility`, `#DeepMind`, `#model release`

---

<a id="item-12"></a>
## [LFM2.5-VL-3B：更快速、更强大的边缘端视觉语言模型](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b) ⭐️ 7.0/10

LiquidAI 发布了 LFM2.5-VL-3B，这是一个紧凑的 3B 多模态模型，在视觉语言任务中显著提升了工具使用和函数调用能力。基准测试显示 ToolSandbox 得分从 26.4 翻倍至 59.5，BFCL v4 从 20.5 升至 32.5。 该发布增强了边缘 AI，将先进的视觉语言能力带到资源受限的设备。工具使用能力的提升使小型模型能实际用于多模态工作流的智能体，缩小了与更大模型的差距。 该模型基于 LFM 2-VL-3B 进行进一步的中期和后期训练，是面向设备端部署的 LFM 2.5 混合模型系列的一员。发布首日即支持 llama.cpp、MLX、vLLM、SGLang 和 ONNX 等推理生态。

rss · Hugging Face Blog · 8月12日 14:00

**背景**: 视觉语言模型（VLM）能够同时从图像和文本中理解和生成信息，将大语言模型的能力扩展到纯文本之外。像 LFM2.5-VL-3B 这样的小型 VLM 旨在边缘和移动设备上实现这些功能，在这些场景中低延迟和端侧隐私保护至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/LiquidAI/LFM2.5-VL-3B">LiquidAI/ LFM 2 . 5 - VL - 3 B · Hugging Face</a></li>
<li><a href="https://www.liquid.ai/blog/lfm2-5-vl-3b">LFM 2 . 5 - VL - 3 B : A Better and Faster Vision-Language... — Liquid AI</a></li>
<li><a href="https://zenn.dev/kun432/scraps/10b1efe7eb0d26">「 LFM 2 . 5 - VL - 3 B 」を試す</a></li>

</ul>
</details>

**标签**: `#vision-language-model`, `#edge-ai`, `#model-release`, `#efficiency`

---