# Awesome AI Safety [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

> A curated collection of resources for building safe, aligned, and trustworthy AI systems.

This list covers the full stack of AI safety: alignment techniques, interpretability, evaluation, formal verification, governance, and verifiable AI. Maintained with a focus on **working tools, code, and actionable resources** — not just papers.

If you find this useful, consider giving it a ⭐ to help others discover it.

---

## Contents

- [Alignment & Training](#alignment--training)
- [Interpretability & Mechanistic Analysis](#interpretability--mechanistic-analysis)
- [Red Teaming & Evaluation](#red-teaming--evaluation)
- [Formal Verification & Robustness](#formal-verification--robustness)
- [Verifiable AI & ZKML](#verifiable-ai--zkml)
- [Governance, Policy & Compliance](#governance-policy--compliance)
- [Safety Benchmarks & Datasets](#safety-benchmarks--datasets)
- [Foundational Papers](#foundational-papers)
- [Organizations](#organizations)
- [Courses & Educational Resources](#courses--educational-resources)

---

## Alignment & Training

*Tools and frameworks for aligning AI systems with human values and intentions.*

### RLHF & Preference Optimization

- [TRL](https://github.com/huggingface/trl) — Hugging Face library for RLHF, DPO, PPO, and SFT training of language models. The standard open-source alignment training library.
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) — High-performance RLHF framework built on Ray, vLLM, and DeepSpeed. Scales to 70B+ models.
- [Direct Preference Optimization](https://github.com/eric-mitchell/direct-preference-optimization) — Reference implementation of DPO, which simplifies RLHF by eliminating the separate reward model.
- [DeepSpeed-Chat](https://github.com/microsoft/DeepSpeedExamples/tree/master/applications/DeepSpeed-Chat) — Microsoft's end-to-end RLHF pipeline (SFT → reward modeling → PPO) with DeepSpeed integration.
- [RewardBench](https://github.com/allenai/reward-bench) — Allen AI benchmark for evaluating reward models used in alignment training.

### Guardrails & Output Safety

- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) — NVIDIA's toolkit for adding programmable safety rails to LLM applications.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) — Framework for adding structure, type, and quality guarantees to LLM outputs.
- [LLM Guard](https://github.com/protectai/llm-guard) — Self-hosted toolkit for sanitizing and securing LLM interactions (prompt injection detection, PII filtering, toxicity checks).
- [Llama Guard](https://github.com/meta-llama/PurpleLlama) — Meta's safety classifier models for content moderation of LLM inputs and outputs. Part of PurpleLlama.
- [Alignment Handbook](https://github.com/huggingface/alignment-handbook) — Hugging Face recipes for aligning language models with human and AI preferences. Practical guides for SFT, DPO, and RLHF.

### Representation & Activation Engineering

- [Representation Engineering](https://github.com/andyzoujm/representation-engineering) — Top-down approach to AI transparency. Read and control model behavior via representation-level interventions.
- [repeng](https://github.com/vgel/repeng) — Library for making RepE control vectors with language models. Steer model behavior at inference time.
- [Circuit Breakers](https://github.com/GraySwanAI/circuit-breakers) — Interrupt harmful model behavior by operating on internal representations rather than output filtering.
- [Honest LLaMA (ITI)](https://github.com/likenneth/honest_llama) — Inference-Time Intervention for eliciting truthful answers by shifting model activations.

---

## Interpretability & Mechanistic Analysis

*Understanding what neural networks learn and how they compute.*

### Libraries & Frameworks

- [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) — The primary library for mechanistic interpretability of GPT-style models. Hook into and analyze any transformer internal.
- [SAELens](https://github.com/decoderesearch/SAELens) — Training, analyzing, and using Sparse Autoencoders on language models. The tool behind much of the recent feature extraction research.
- [nnsight](https://github.com/ndif-team/nnsight) — Intervene on and inspect neural network internals. Enables causal interventions and tracing in large models (from David Bau's group).
- [pyvene](https://github.com/stanfordnlp/pyvene) — Stanford NLP's unified framework for activation patching, causal tracing, and representation engineering.
- [CircuitsVis](https://github.com/alan-cooney/CircuitsVis) — Visualization tools for attention patterns and circuit-level interpretability.
- [Baukit](https://github.com/davidbau/baukit) — Toolkit for editing and understanding neural network representations.
- [OpenAI Sparse Autoencoder](https://github.com/openai/sparse_autoencoder) — OpenAI's sparse autoencoder implementation for extracting interpretable features.

### Platforms & Resources

- [Neuronpedia](https://neuronpedia.org) — Interactive platform for exploring individual neuron and feature behaviors in language models.
- [Transformer Circuits Thread](https://transformer-circuits.pub) — Anthropic's ongoing publication series on mechanistic interpretability of transformers.

---

## Red Teaming & Evaluation

*Testing AI systems for dangerous capabilities, vulnerabilities, and failure modes.*

### Automated Red Teaming

- [garak](https://github.com/NVIDIA/garak) — LLM vulnerability scanner. Probes for hallucination, toxicity, prompt injection, data leakage, and more. Extensible and automated.
- [HarmBench](https://github.com/centerforaisafety/HarmBench) — Standardized evaluation framework for automated red teaming of LLMs, from the Center for AI Safety.
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) — Meta's safety suite including CyberSecEval for cybersecurity risk evaluation and Llama Guard for content safety.
- [Anthropic Evals](https://github.com/anthropics/evals) — Anthropic's public evaluation suite for dangerous capabilities and safety properties.
- [promptfoo](https://github.com/promptfoo/promptfoo) — LLM evaluation and red-teaming tool. Includes safety-specific plugins for toxicity, PII, and jailbreak testing.

### Evaluation Frameworks

- [Inspect AI](https://github.com/UKAIResearch/inspect_ai) — UK AI Safety Institute's framework for evaluating AI capabilities and alignment. Task-based and extensible.
- [METR Task Standard](https://github.com/METR/task-standard) — Task standard for evaluating dangerous autonomous capabilities in AI systems (from the team that evaluates frontier models pre-deployment).
- [EleutherAI LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) — The de facto standard for LLM benchmarking across hundreds of tasks, including safety-relevant ones.
- [Vivaria](https://github.com/METR/vivaria) — METR's tool for running AI agents on evaluation tasks. Used internally for frontier model capability assessments.
- [METR Public Tasks](https://github.com/METR/public-tasks) — Collections of tasks for evaluating dangerous capabilities of autonomous AI agents.

### Adversarial Attacks & Jailbreaking

- [LLM Attacks](https://github.com/llm-attacks/llm-attacks) — Universal and transferable adversarial attacks on aligned language models (GCG attack). Foundational adversarial ML research.
- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) — Open robustness benchmark for jailbreaking language models. Evolving repository of attack and defense methods.
- [StrongREJECT](https://github.com/dsbowen/strong_reject) — Rejection benchmark for evaluating how well models refuse harmful jailbreak attempts.

---

## Formal Verification & Robustness

*Mathematically proving properties about neural network behavior.*

### Neural Network Verifiers

- [α-β-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) — GPU-accelerated neural network verifier using bound propagation and branch-and-bound. Winner of VNN-COMP multiple years.
- [auto_LiRPA](https://github.com/Verified-Intelligence/auto_LiRPA) — Automatic Linear Relaxation based Perturbation Analysis. General-purpose certified robustness library underlying α-β-CROWN.
- [ERAN](https://github.com/eth-sri/eran) — ETH Zurich's certification tool using abstract interpretation. Handles ReLU, sigmoid, tanh, and MaxPool.
- [NNV](https://github.com/verivital/nnv) — Verification for deep neural networks and neural network control systems. Focus on safety-critical systems (autonomous vehicles, robotics).

### Certified Robustness

- [Randomized Smoothing](https://github.com/locuslab/smoothing) — Reference implementation of Cohen et al. 2019. Scalable certified robustness via randomized smoothing.
- [VNN-COMP](https://github.com/ChristopherBrix/vnncomp2024) — Annual competition benchmarking neural network verification tools. Defines standard benchmarks.

---

## Verifiable AI & ZKML

*Cryptographic techniques for proving properties about AI systems without revealing their internals.*

### Zero-Knowledge ML Frameworks

- [EZKL](https://github.com/zkonduit/ezkl) — Create zero-knowledge proofs of ML model inference. Converts ONNX models to ZK circuits. The most mature ZKML framework.
- [Giza / Orion](https://github.com/gizatechxyz/orion) — Open-source framework for provable machine learning. ONNX runtime for verifiable inference on-chain.
- [Modulus Labs / Remainder](https://github.com/modulus-labs/remainder_prover) — Custom prover engineered for ZK proofs of large ML model inference on Ethereum.
- [RISC Zero zkVM](https://github.com/risc0/risc0) — General-purpose zero-knowledge virtual machine based on RISC-V and zk-STARKs. Supports ML workloads.
- [zkml](https://github.com/ddkang/zkml) — Proof-of-concept ZKML library using the Halo2 proving system. Converts ONNX models to Halo2 format.

### Curated ZKML Resources

- [awesome-zkml](https://github.com/worldcoin/awesome-zkml) — Worldcoin's curated list of ZKML resources, frameworks, and tools.

### Key Use Cases

- **Verifiable inference** — Prove that a specific model produced a specific output on specific inputs, without revealing model weights.
- **Model auditing** — Prove a deployed model has certain safety properties (passed evals, meets fairness criteria) without exposing the model.
- **Compute governance** — Hardware attestation combined with ZK proofs for verifying international AI governance agreements.

---

## Governance, Policy & Compliance

*Frameworks, tools, and resources for responsible AI deployment and regulatory compliance.*

### Regulatory Frameworks

- [EU AI Act](https://artificialintelligenceact.eu/) — The first comprehensive AI regulation. Risk-based approach with strict requirements for high-risk systems. [Full text](https://artificialintelligenceact.eu/ai-act-explorer/).
- [NIST AI Risk Management Framework](https://github.com/usnistgov/AI-RMF-Knowledge-Base) — US framework for managing AI risks. Voluntary but widely referenced.
- [EU AI Act Compliance Kit](https://github.com/ericmacai/ai-act-compliance-kit) — Open-source templates, checklists, and tools for EU AI Act compliance.
- [EU AI Act Compliance Checker](https://github.com/aionthebeach/eu-ai-act-compliance-checker) — Tool to check AI systems against EU AI Act requirements.

### Fairness & Bias Tools

- [AI Fairness 360](https://github.com/Trusted-AI/AIF360) — IBM's comprehensive toolkit for detecting and mitigating bias in datasets and ML models.
- [Fairlearn](https://github.com/fairlearn/fairlearn) — Microsoft's Python library for assessing and improving AI system fairness.
- [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) — Microsoft's suite for model and data exploration, error analysis, and fairness assessment.

### Governance Platforms

- [Credo AI](https://www.credo.ai/) — AI governance platform for EU AI Act compliance, risk assessment, and responsible AI management.
- [Holistic AI](https://www.holisticai.com/) — AI governance and risk management platform.

---

## Safety Benchmarks & Datasets

*Standardized evaluations for measuring AI safety properties.*

### Harmful Content & Toxicity

- [RealToxicityPrompts](https://github.com/allenai/real-toxicity-prompts) — Allen AI dataset for evaluating neural toxic degeneration in language models.
- [ToxiGen](https://github.com/microsoft/TOXIGEN) — Microsoft's large-scale machine-generated dataset for adversarial and implicit hate speech detection.
- [SafetyBench](https://github.com/thu-coai/SafetyBench) — 11,435 multiple-choice questions evaluating LLM safety across multiple dimensions.

### Bias & Fairness

- [BBQ](https://github.com/nyu-mll/BBQ) — Bias Benchmark for QA. 58,492 hand-generated examples targeting nine social bias categories.
- [WinoBias](https://github.com/uclanlp/corefBias) — Gender bias benchmark for coreference resolution.
- [CrowS-Pairs](https://github.com/nyu-mll/crows-pairs) — Challenge dataset measuring social biases in masked language models.
- [Winogender](https://github.com/rudinger/winogender-schemas) — Minimal pair sentences testing gender bias in coreference resolution.

### Truthfulness & Hallucination

- [TruthfulQA](https://github.com/sylinrl/TruthfulQA) — 817 questions measuring whether language models generate truthful answers.
- [HaluEval](https://github.com/RUCAIBox/HaluEval) — Large-scale hallucination evaluation benchmark for LLMs.
- [Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard) — Public leaderboard measuring LLM hallucination rates.

### Dangerous Capabilities

- [WMDP](https://github.com/centerforaisafety/wmdp) — Weapons of Mass Destruction Proxy benchmark. Measures hazardous knowledge in biosecurity, cybersecurity, and chemical security.
- [MACHIAVELLI](https://github.com/aypan17/machiavelli) — Benchmark measuring both competence and ethical behavior of language agents in 134 text-based scenarios.
- [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks) — Meta's evaluation for cybersecurity risks in LLMs (part of PurpleLlama).

### Comprehensive Trust

- [DecodingTrust](https://github.com/AI-secure/DecodingTrust) — Comprehensive trustworthiness assessment across eight dimensions: toxicity, bias, robustness, privacy, ethics, fairness, and more.

---

## Foundational Papers

*Essential reading, ordered chronologically. The intellectual backbone of the field.*

### Foundations & Problem Framing

| Year | Paper | Key Contribution |
|------|-------|-----------------|
| 2012 | [The Superintelligent Will](https://nickbostrom.com/superintelligentwill.pdf) — Bostrom | Instrumental convergence thesis: advanced AI systems will converge on self-preservation and resource acquisition regardless of final goals. |
| 2015 | [Research Priorities for Robust and Beneficial AI](https://arxiv.org/abs/1602.03506) — Russell, Dewey, Tegmark | The research agenda that launched AI safety as a serious field. |
| 2016 | [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) — Amodei, Olah, Steinhardt, Christiano, Schulman | Five concrete problems: safe exploration, distributional shift, reward hacking, scalable oversight, safe interruptibility. |
| 2019 | [Risks from Learned Optimization](https://arxiv.org/abs/1906.01820) — Hubinger, van Merwijk, Mikulik, Skalse | Mesa-optimization and deceptive alignment: models may learn internal optimizers with misaligned objectives. |
| 2019 | [The Bitter Lesson](http://www.incompleteideas.net/IncsightIdea/BitterLesson.html) — Sutton | General methods leveraging computation beat specialized approaches. One page, most cited essay in ML. |
| 2019 | [Optimal Policies Tend to Seek Power](https://arxiv.org/abs/1912.01683) — Turner, Smith, Shah, Critch | Formal proof that optimal policies tend toward power-seeking behaviors. |

### Alignment Techniques

| Year | Paper | Key Contribution |
|------|-------|-----------------|
| 2017 | [Deep RL from Human Preferences](https://arxiv.org/abs/1706.03741) — Christiano, Leike, Brown, Amodei | The foundational RLHF paper. Learning goals from human preference comparisons. |
| 2018 | [AI Safety via Debate](https://arxiv.org/abs/1805.00899) — Irving, Christiano, Amodei | Two AI systems debate; humans judge. Scalable oversight via adversarial interaction. |
| 2018 | [Scalable Agent Alignment via Reward Modeling](https://arxiv.org/abs/1811.07871) — Leike, Krueger, Everitt, Martic | DeepMind's research agenda: recursive reward modeling for scalable alignment. |
| 2021 | [Goal Misgeneralization in Deep RL](https://arxiv.org/abs/2105.14111) — Langosco, Koch, Sharkey, Pfau, Krueger | First extensive study of agents pursuing wrong goals despite correct reward specification. |
| 2022 | [Training Language Models to Follow Instructions (InstructGPT)](https://arxiv.org/abs/2203.02155) — Ouyang et al. | Applied RLHF to language models at scale. The foundation for ChatGPT. |
| 2022 | [Constitutional AI](https://arxiv.org/abs/2212.08073) — Bai et al. | Self-supervised alignment using AI critique against written principles. Reduced reliance on human feedback for harmlessness. |
| 2022 | [Red Teaming Language Models](https://arxiv.org/abs/2209.07858) — Ganguli et al. | Anthropic's systematic approach to discovering LLM failure modes. |
| 2023 | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — Rafailov, Sharma, Mitchell, Manning, Ermon, Finn | Simplified RLHF by eliminating the reward model. Closed-form policy optimization from preferences. |
| 2023 | [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390) — Burns, Ye, Klein, Steinhardt | Can weak models supervise strong ones? OpenAI's empirical study of the superalignment problem. |
| 2024 | [Sleeper Agents](https://arxiv.org/abs/2401.05566) — Hubinger et al. | Demonstrated that deceptive behaviors persist through standard safety training. |
| 2024 | [Alignment Faking](https://arxiv.org/abs/2412.14093) — Anthropic | First empirical evidence of a large language model engaging in alignment faking to avoid modification. |
| 2024 | [Model Organisms of Misalignment](https://arxiv.org/abs/2407.04507) — Hubinger et al. | Proposes creating intentionally misaligned models to study and develop detection methods. |
| 2024 | [Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624) — Dalrymple et al. | Framework combining world models, safety specifications, and verifiers for provable safety guarantees. |
| 2025 | [The Claude Model Spec](https://www.anthropic.com/research/the-claude-model-spec) — Anthropic | Comprehensive specification of Claude's values, behavior, and reasoning principles. A new approach to alignment via detailed specification. |

---

## Organizations

*Research labs, institutes, and nonprofits working on AI safety.*

### Frontier Labs with Safety Teams

| Organization | Focus | Location |
|-------------|-------|----------|
| [Anthropic](https://www.anthropic.com/research) | Constitutional AI, interpretability, RSP | SF / London |
| [Google DeepMind](https://deepmind.google/safety-and-responsibility/) | Scalable oversight, evaluations, debate | London |
| [OpenAI Safety](https://openai.com/safety) | Preparedness, superalignment research | SF / London / Dublin |
| [Meta FAIR](https://ai.meta.com/research/) | Open models, responsible release | Paris / NYC |

### Independent Research Orgs

| Organization | Focus | Location |
|-------------|-------|----------|
| [MIRI](https://intelligence.org/) | Agent foundations, theoretical alignment | Berkeley |
| [Redwood Research](https://www.redwoodresearch.org/) | Control agenda, adversarial training, interpretability | SF |
| [ARC (Alignment Research Center)](https://alignment.org/) | ELK (Eliciting Latent Knowledge), theoretical alignment | Berkeley |
| [METR](https://metr.org/) | Model evaluation for dangerous autonomous capabilities | Berkeley |
| [Center for AI Safety](https://safe.ai/) | Field-building, benchmarks, risk research | SF |
| [FAR AI](https://far.ai/) | Practical AI safety research | Berkeley |
| [Apollo Research](https://www.apolloresearch.ai/) | Detecting and evaluating deceptive AI behaviors | London |
| [Conjecture](https://www.conjecture.dev/) | Alignment research, controllable AI systems | London |

### Government & Policy

| Organization | Focus | Location |
|-------------|-------|----------|
| [UK AI Safety Institute](https://www.gov.uk/government/organisations/ai-safety-institute) | Pre-deployment evaluations, safety testing | London |
| [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office) | EU AI Act implementation and enforcement | Brussels |
| [NIST AI](https://www.nist.gov/artificial-intelligence) | AI Risk Management Framework, standards | US |
| [Frontier Model Forum](https://www.frontiermodelforum.org/) | Industry consortium for frontier AI safety | Global |

---

## Courses & Educational Resources

- [AGI Safety Fundamentals](https://www.agisafetyfundamentals.com/) — 8-week structured course covering the core concepts of AI alignment.
- [ARENA (Alignment Research Engineer Accelerator)](https://www.arena.education/) — Hands-on technical curriculum for alignment research engineering.
- [David Silver's RL Course](https://www.deepmind.com/learning-resources/introduction-to-reinforcement-learning-with-david-silver) — 10 lectures from the creator of AlphaGo. Essential for understanding RL-based alignment.
- [Anthropic's Research Blog](https://www.anthropic.com/research) — Ongoing publications on interpretability, alignment, and safety.
- [Alignment Forum](https://www.alignmentforum.org/) — Community forum for AI alignment research discussion.
- [LessWrong AI Safety Tag](https://www.lesswrong.com/tag/ai-safety) — Long-form discussion and analysis of AI safety topics.
- [ML Safety Course (CAIS)](https://course.mlsafety.org/) — Technical AI safety course by the Center for AI Safety. Intended for ML researchers and engineers.
- [MATS](https://www.matsprogram.org/) — Research training program supporting the next generation of AI alignment researchers. Mentored by leading safety researchers.
- [AI Safety Camp](https://aisafety.camp/) — Collaborative research meetups where people from diverse backgrounds work on AI safety projects.
- [AI Safety Map](https://aisafety.world/) — Interactive visualization of the AI safety research landscape.

---

## Contributing

Contributions are welcome. Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a PR.

**Quality standards:**
- Every entry must include a working link and a concise description
- Tools and frameworks should be actively maintained (last commit within 12 months)
- Papers must be peer-reviewed or from established research institutions
- No promotional content, paywalled resources, or vaporware

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is dedicated to the public domain under CC0 1.0.
