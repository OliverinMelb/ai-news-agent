---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 35 条内容中筛选出 5 条重要资讯。

---

1. [OpenAI Agents JS SDK v0.14.0 增加程序化工具调用](#item-1) ⭐️ 8.0/10
2. [SlopCodeBench 评估 Opus 5 在跨任务中的代码可维护性](#item-2) ⭐️ 8.0/10
3. [月之暗面开源 2.8 万亿参数 Kimi K3 模型权重](#item-3) ⭐️ 8.0/10
4. [llama.cpp b10155 新增 MiMo V2.5 音频输入支持](#item-4) ⭐️ 7.0/10
5. [NVIDIA Cosmos-H-Dreams 实现实时手术机器人仿真](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Agents JS SDK v0.14.0 增加程序化工具调用](https://github.com/openai/openai-agents-js/releases/tag/v0.14.0) ⭐️ 8.0/10

OpenAI 发布了 JavaScript Agents SDK v0.14.0，新增了程序化工具调用支持，让模型能够生成托管的 JavaScript 来协调工具、减少往返次数；同时默认禁用敏感数据日志，并默认启用任务和回合追踪。 程序化工具调用可大幅减少 API 往返次数，降低复杂多工具代理工作流的 token 消耗与延迟；安全改进（日志需主动启用）与更好的追踪功能也提升了 AI 代理开发者的开发体验和生产安全性。 该功能的原理是让支持的模型在隔离的 V8 沙箱中编写 JavaScript 编排代码，并在流式、会话和回放中保留中间结果。追踪方面，运行现在默认发出任务和回合跨度；敏感数据日志则需要显式调用 `setSensitiveDataLoggingEnabled(true)`。

github · seratch · 7月28日 03:12

**背景**: OpenAI Agents SDK 是一个构建 AI 代理工作流的框架，支持函数工具、MCP 工具、任务交接和可观测性。程序化工具调用最初随 GPT-5.6 在 Responses API 中推出，允许模型在单个执行块中组合循环、条件判断和多工具聚合，而无需为每次工具调用单独进行往返。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bota.chat/chat-gpt-5-6/openai-programmatic-tool-calling/">OpenAI Programmatic Tool Calling : 63.5% Fewer Tokens</a></li>
<li><a href="https://apidog.com/blog/gpt-5-6-programmatic-tool-calling/">GPT-5.6 programmatic tool calling : the model writes the...</a></li>
<li><a href="https://openai.github.io/openai-agents-python/tracing/">Tracing - OpenAI Agents SDK</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#agents`, `#SDK`, `#tool calling`, `#JavaScript`

---

<a id="item-2"></a>
## [SlopCodeBench 评估 Opus 5 在跨任务中的代码可维护性](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md) ⭐️ 8.0/10

一个名为 SlopCodeBench \(SCB\) 的新基准被推出，它评估像 Anthropic 的 Claude Opus 5 这样的编码代理在顺序、迭代任务中的代码复杂性和可维护性，而不是单次问题。评估显示，Opus 5 在降低代码复杂性方面相比之前模型有显著改进。 该基准通过测量代码在多个步骤中的退化，填补了 AI 编码评估中的一个关键空白，更贴近现实软件开发中代理必须维护和扩展自身代码的场景。这可能会促使模型提供方在未来的训练中优先考虑代码质量和可维护性，而不仅仅是正确性。 该基准包含 36 个问题，共 196 个检查点，代理在其中迭代扩展自己的解决方案，测量代码行数 \(LoC\) 和圈复杂度等复杂性与可维护性指标。Opus 5 在此基准上表现突出，相较之前模型代码复杂性降低 25%，但需要人类基线数据才能提供完整背景。

hackernews · dhorthy · 7月27日 22:37 · [社区讨论](https://news.ycombinator.com/item?id=49076391)

**背景**: 大多数现有的编码基准只评估 AI 代理在单个孤立任务上的表现，无法捕捉代理随时间修改或扩展自己代码时出现的代码退化。SlopCodeBench 的灵感来源于“代码侵蚀”概念——即代码库随着每次迭代变得越来越复杂、难以维护的趋势，这是软件工程中众所周知但在 AI 评估中很少被衡量的挑战。该基准旨在通过模拟更真实的多步骤开发周期来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.24755">[2603.24755] SlopCodeBench : Benchmarking How Coding Agents...</a></li>
<li><a href="https://www.scbench.ai/">SlopCodeBench</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞 SlopCodeBench 被低估且比单任务基准更真实，有人主张将其用于强化学习管道中以优先降低代码复杂性。其他人则指出缺少人类表现基线，警告 headline 数字可能被误解；一位用户还分享了使用 SCB 评估代理技能的实践经验。

**标签**: `#benchmark`, `#coding agents`, `#code quality`, `#AI evaluation`, `#maintainability`

---

<a id="item-3"></a>
## [月之暗面开源 2.8 万亿参数 Kimi K3 模型权重](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 8.0/10

月之暗面 AI 在 Hugging Face 上发布了其 2.8 万亿参数的 Kimi K3 模型权重，总大小为 1.56 TB。该模型采用修改后的许可证，要求大型模型即服务（MaaS）企业另行签署协议。 这是迄今为止发布的最大开源权重模型之一，为开发者和研究人员提供了前沿规模模型的访问权。然而，限制性许可证可能限制商业采用，并凸显了开放性与商业控制之间的持续矛盾。 许可证不再称为“修改版 MIT”，新增条款要求年收入超过 2000 万美元且运营模型即服务业务的公司与月之暗面另行协商协议。OpenRouter 已从七个提供商处提供 K3，定价与月之暗面自有 API 相同。

rss · Simon Willison · 7月27日 23:39

**背景**: 月之暗面 AI 是一家总部位于北京的人工智能公司，以其 Kimi 系列大语言模型而闻名。开放权重模型允许用户本地检查并运行权重，但可能附带使用限制，使其不能被视为真正意义上的开源。2.8 万亿的参数规模使 Kimi K3 成为公开可用的最大模型之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/daya-shankar/open-source-llms">Best Open -Source LLM Models in 2026: Coding, Local, Agentic AI...</a></li>

</ul>
</details>

**标签**: `#Kimi K3`, `#Moonshot`, `#open-weight model`, `#large language model`, `#Hugging Face`

---

<a id="item-4"></a>
## [llama.cpp b10155 新增 MiMo V2.5 音频输入支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10155) ⭐️ 7.0/10

llama.cpp 版本 b10155 引入了对 MiMo V2.5 音频输入的支持，使得基于 RVQ 的多模态模型推理成为可能。该版本包含 GGUF 转换器、C++ 实现，以及面向 macOS、Linux、Windows、Android 和 iOS 的预编译二进制文件。 这使得开发者能够通过 llama.cpp 在本地消费级硬件上高效运行小米的 MiMo V2.5 音频模型，为开源 AI 带来了强大的多模态音频理解能力。它降低了在不依赖云 API 的情况下实验语音识别和音频驱动 AI 应用的门槛。 MiMo V2.5 支持包括文本、图像、视频和音频在内的多种输入类型，并提供 ASR（语音识别）和 TTS（文本转语音）能力。RVQ（残差向量量化）方法实现了高效高保真音频分词，新的实现包含用于准备模型的 GGUF 转换器和用于推理的 C++ 运行时。

github · github-actions\[bot\] · 7月27日 21:59

**背景**: MiMo V2.5 是小米推出的多模态模型系列，能够处理文本、图像、视频和音频。RVQ（残差向量量化）是一种通过多阶段量化残差误差将音频数据压缩为离散令牌的技术，从而实现高保真音频生成与识别。llama.cpp 是一个流行的开源项目，能够以最小的依赖在 CPU 和 GPU 上高效运行大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.mi.com/docs/en-US/quick-start/usage-guide/audio/Speech-Recognition">Speech Recognition（MiMo-V2.5-ASR） - Xiaomi</a></li>
<li><a href="https://deepinfra.com/blog/mimo-v2-5-on-deepinfra">MiMo-V2.5 Is Now Available on DeepInfra</a></li>
<li><a href="https://arxiv.org/pdf/2412.10208">Efficient Generative Modeling with Residual Vector...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#multimodal`, `#audio`, `#open-source`, `#inference`

---

<a id="item-5"></a>
## [NVIDIA Cosmos-H-Dreams 实现实时手术机器人仿真](https://huggingface.co/blog/nvidia/cosmos-h-dreams) ⭐️ 7.0/10

NVIDIA 推出了 Cosmos-H-Dreams，这是一个用于手术机器人的实时、动作条件生成式模拟器。它将更大的 Cosmos-H-Surgical-Simulator 蒸馏成一个因果学生模型，可在单个 RTX PRO 6000 GPU 上运行。 这实现了实时闭环机器人测试，大幅减少了对昂贵物理设备的需求，加速了手术机器人的开发。它将生成式模拟的强大能力带入了高风险的医疗领域。 该模型是动作条件式的，即根据机器人的动作生成模拟帧。它可在单个 RTX PRO 6000 GPU 上实时流式传输手术模拟，使其易于用于研究和开发。

rss · Hugging Face Blog · 7月27日 09:32

**背景**: 生成式模拟利用 AI 模型为机器人创建逼真的训练环境，减少了对手动场景设计的需求。手术机器人需要高保真模拟以确保安全有效的训练。NVIDIA 的 Cosmos 平台提供了理解物理世界的基础模型，而 Cosmos-H-Dreams 是专门用于手术机器人的模型，实现了实时交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/nvidia/Cosmos-H-Dreams">nvidia / Cosmos - H - Dreams · Hugging Face</a></li>
<li><a href="https://korshunov.ai/en/article/14290-nvidia-introduces-cosmos-h-dreams-a-real-time-generative-simulator-for-surgical/">NVIDIA introduces Cosmos - H - Dreams , a real-time generative...</a></li>
<li><a href="https://thorstenmeyerai.com/ai-work/nvidia-cosmos-h-dreams-bringing-real-time-generative-simulation-to-surgical-robo/">NVIDIA Cosmos - H - Dreams : Bringing Real-Time... - Thorsten Meyer AI</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#generative simulation`, `#surgical robotics`, `#AI`, `#robotics`

---