# Awesome AI Safety

A curated guide to tools, benchmarks and research for evaluating and reducing AI risk. Covers alignment, control, interpretability, application security, formal verification and governance.

**Use the evidence at its stated scope.** A benchmark score measures sampled behavior. A formal certificate covers an encoded property. A signature authenticates an artifact or statement. None establishes general safety.

[Read the website](https://abdelstark.github.io/awesome-ai-safety/) · [Curation methodology](docs/methodology.md) · [October 2026 review](docs/review-2026-10-09.md) · [Contribute](CONTRIBUTING.md)

## Start here

| Your task | Start with | Check before drawing a conclusion |
|---|---|---|
| Evaluate a model or agent | [Evaluation frameworks](#evaluation-frameworks) | Task coverage, elicitation, scorer validity and contamination. |
| Test prompt injection or harmful requests | [Red teaming](#red-teaming) and [agent evaluations](#agent-evaluations) | Attack access, tool permissions, benign utility and repeated trials. |
| Study a training intervention | [Alignment and control](#alignment-and-control) | Baselines, held-out behavior and generalization after further training. |
| Investigate model computation | [Interpretability](#interpretability) | Supported models, intervention evidence and approximation error. |
| Restrict application behavior | [Runtime safeguards and security](#runtime-safeguards-and-security) | Enforcement boundaries and failure behavior. |
| Verify a precise property or artifact | [Formal verification and execution evidence](#formal-verification-and-execution-evidence) | The specification, identity binding and trusted assumptions. |
| Build a risk-management process | [Governance and assurance](#governance-and-assurance) | Applicable context, current official guidance and unresolved risks. |

**Reading labels:** **Research** means a reference implementation or experimental method, with no promise of ongoing maintenance. **Historical** means archived or superseded. **Restricted** means public access carries additional use or model terms. Other code entries have documented use instructions and an inspected project license; inclusion is not a security audit. Dataset and model terms can differ from code terms.

## Contents

- [Evaluation and red teaming](#evaluation-and-red-teaming)
- [Alignment and control](#alignment-and-control)
- [Interpretability](#interpretability)
- [Runtime safeguards and security](#runtime-safeguards-and-security)
- [Benchmarks and datasets](#benchmarks-and-datasets)
- [Formal verification and execution evidence](#formal-verification-and-execution-evidence)
- [Governance and assurance](#governance-and-assurance)
- [Research papers and reports](#research-papers-and-reports)
- [Research groups](#research-groups)
- [Learning resources](#learning-resources)

## Evaluation and red teaming

### Evaluation frameworks

- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - Model and agent evaluations with composable tasks, scorers, tools, sandboxes and inspectable logs.
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) - Benchmark implementations and documented tasks for Inspect; individual tasks have their own dependencies and terms.
- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) - General language-model benchmark runner with reusable task definitions, including safety-relevant evaluations.
- [METR Public Tasks](https://github.com/METR/public-tasks) - Public agent capability tasks, with instructions for running legacy tasks through an Inspect bridge; a subset of METR's evaluation work.
- [JevOss](https://github.com/mertkayacs/jevoss) - Accuracy, calibration and robustness probes for decision-model servers that implement the Jev API, measuring answer changes under injected instructions, reordered options, irrelevant padding and repeated calls; supports that one API shape.

### Red teaming

- [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) - Attacks, defenses and evaluation tools for evasion, poisoning, extraction and inference across supported machine-learning models.
- [PyRIT](https://github.com/microsoft/PyRIT) - Generative AI red-teaming framework with attack strategies, targets, scoring and conversation records.
- [garak](https://github.com/NVIDIA/garak) - Scanner that probes language models for failure modes such as injection, leakage and harmful generation.
- [promptfoo](https://github.com/promptfoo/promptfoo) - Application evaluations and red-team tests with configurable prompts, assertions and attack plugins.
- [HarmBench](https://github.com/centerforaisafety/HarmBench) - **Research.** Harmful-behavior test cases, attack methods and classifiers for comparing automated red teaming.
- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) - **Research.** Jailbreak robustness benchmark with shared behaviors, threat models and attack artifacts.
- [StrongREJECT](https://github.com/dsbowen/strong_reject) - **Research.** Jailbreak benchmark and scorers that assess refusal and the usefulness of harmful responses; results depend on the judge.
- [LLM Attacks](https://github.com/llm-attacks/llm-attacks) - **Research.** Reference implementation of gradient-based adversarial suffix attacks on aligned language models.

### Agent evaluations

- [AgentDojo](https://github.com/ethz-spylab/agentdojo) - Environment for testing indirect prompt injection attacks and defenses in tool-using agents.
- [AgentHarm](https://ukgovernmentbeis.github.io/inspect_evals/evals/agentharm/) - **Restricted benchmark.** Harmful multi-step requests with synthetic tools and benign counterparts; use is limited to improving AI safety and security.
- [Petri Bloom](https://github.com/meridianlabs-ai/petri_bloom) - **Research.** Generate targeted behavioral scenarios and score model interactions; preserve seed configurations and review judges.
- [Inspect Petri](https://github.com/meridianlabs-ai/inspect_petri) - **Research.** Auditing agent that explores alignment hypotheses using simulated interactions and rubric-scored transcripts.
- [CyberGym](https://github.com/sunblaze-ucb/cybergym) - Vulnerability-analysis and proof-of-concept reproduction tasks on real software; requires substantial local infrastructure and containment.
- [Cybench](https://github.com/andyzorigin/cybench) - Capture-the-flag agent tasks with intermediate subtasks; report guided and unguided results separately.

For an evaluation report, record the threat model, model and harness versions, permissions, budgets, benign utility, scorer validation, failures and uncertainty. See the [evaluation checklist](docs/methodology.md#evaluating-evaluation-results).

## Alignment and control

### Post-training and preference learning

Training tools implement optimization procedures. Preference fit and refusal behavior alone do not establish robust alignment.

- [TRL](https://github.com/huggingface/trl) - Language-model post-training library with supervised fine-tuning and preference or reinforcement-learning trainers.
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) - Distributed reinforcement-learning and preference-training framework built around Ray and vLLM.
- [Alignment Handbook](https://github.com/huggingface/alignment-handbook) - Training recipes and released artifacts for supervised and preference-based language-model fine-tuning.
- [Direct Preference Optimization](https://github.com/eric-mitchell/direct-preference-optimization) - **Research.** Reference implementation of direct policy optimization from preference comparisons.
- [RewardBench](https://github.com/allenai/reward-bench) - Reward-model evaluation tasks and scoring code for preference-training research.
- [OpenUnlearning](https://github.com/locuslab/open-unlearning) - Compare unlearning methods and metrics on TOFU, MUSE and WMDP; reduced benchmark performance does not establish irreversible deletion.

### Control and monitoring

- [ControlArena](https://github.com/UKGovernmentBEIS/control-arena) - Framework for testing control protocols, monitors and adversarial policies in agent environments with benign and sabotage tasks.
- [Monitorability Evals](https://github.com/openai/monitorability-evals) - **Research data.** Public evaluation splits and prompt mappings for chain-of-thought monitorability; private splits are omitted and some evaluations are deprecated.

### Activation interventions

- [Representation Engineering](https://github.com/andyzoujm/representation-engineering) - **Research.** Read and steer language-model behavior using learned representation directions.
- [Circuit Breakers](https://github.com/GraySwanAI/circuit-breakers) - **Research.** Training methods that reroute representations associated with harmful behavior in the tested settings.
- [Honest LLaMA](https://github.com/likenneth/honest_llama) - **Research.** Inference-time activation interventions evaluated for truthfulness on specific models and tasks.

## Interpretability

### Libraries and analysis

- [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) - Inspect transformer activations and conduct mechanistic-interpretability experiments on supported models.
- [SAELens](https://github.com/decoderesearch/SAELens) - Train, load and analyze sparse autoencoders for language-model activations.
- [circuit-tracer](https://github.com/decoderesearch/circuit-tracer) - Generate, visualize and intervene on transcoder attribution graphs for supported models; graphs approximate model computation.
- [nnsight](https://github.com/ndif-team/nnsight) - Trace and intervene on neural-network internals, with local and remote execution interfaces.
- [pyvene](https://github.com/stanfordnlp/pyvene) - Interventions on model representations for activation patching, causal tracing and steering experiments.
- [CircuitsVis](https://github.com/TransformerLensOrg/CircuitsVis) - Interactive visualizations for attention patterns and interpretability experiments.

### Artifacts and research interfaces

- [Gemma Scope 2](https://huggingface.co/google/gemma-scope-2) - **Research weights.** Sparse autoencoders and transcoders for Gemma 3, distributed under CC BY 4.0; base-model terms remain separate.
- [Neuronpedia](https://www.neuronpedia.org/) - Explore model features, activation examples and attribution graphs through an interactive research interface.
- [Transformer Circuits](https://transformer-circuits.pub/) - Research articles on transformer mechanisms, sparse features and circuit tracing.

Features and graphs are hypotheses about computation. Validate interpretations with interventions and task-level evidence; a readable feature label does not establish a safety mechanism.

## Runtime safeguards and security

### Application controls

- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Programmable dialog and application rails for language-model systems.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Schema and custom-validator checks for language-model inputs and outputs; guarantees depend on what each validator actually checks.
- [Llama Guard](https://github.com/meta-llama/PurpleLlama/tree/main/Llama-Guard) - **Restricted models.** Input/output content-safety classifiers; model terms differ from PurpleLlama's evaluation-code license.
- [Inspect Sandboxing](https://inspect.aisi.org.uk/sandboxing.html) - Evaluation execution guide; only work explicitly routed through the sandbox interface runs inside that boundary.
- [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) - Guidance on tool permissions, memory separation, approvals and monitoring for agent applications.

### Model supply chain

- [Model Transparency](https://github.com/sigstore/model-transparency) - Sign and verify model-file hashes and signer identity; signatures do not establish benign model behavior.
- [Fickling](https://github.com/trailofbits/fickling) - Static analysis and loading checks for pickle-based ML artifacts; detection has incomplete coverage.

## Benchmarks and datasets

These are bounded research artifacts. Code, data, model weights and underlying assets may have different licenses. Check the exact release before use. Public tests are vulnerable to contamination, judge errors and coverage gaps.

### Harmful content and bias

- [RealToxicityPrompts](https://github.com/allenai/real-toxicity-prompts) - Prompts and annotations for studying toxic language-model continuation.
- [ToxiGen](https://github.com/microsoft/TOXIGEN) - **Historical dataset.** Machine-generated text for studying implicit and adversarial hate speech.
- [SafetyBench](https://github.com/thu-coai/SafetyBench) - English and Chinese multiple-choice questions across safety-related categories; knowledge questions do not measure deployed behavior.
- [BBQ](https://github.com/nyu-mll/BBQ) - Question-answering benchmark for social bias under ambiguous and disambiguated contexts.
- [WinoBias](https://github.com/uclanlp/corefBias) - Gender-bias evaluation and data for coreference resolution.
- [CrowS-Pairs](https://github.com/nyu-mll/crows-pairs) - Paired-sentence benchmark for social biases in masked language models; its authors warn it may not reliably measure bias.
- [Winogender](https://github.com/rudinger/winogender-schemas) - Minimal-pair sentences for gender-bias analysis in coreference resolution.

### Truthfulness and grounding

- [TruthfulQA](https://github.com/sylinrl/TruthfulQA) - Questions designed to elicit commonly held false beliefs; measures truthfulness on this distribution.
- [HaluEval](https://github.com/RUCAIBox/HaluEval) - Generated and human-annotated samples for studying hallucination recognition in language models.
- [Vectara Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard) - Summarization consistency evaluation using a commercial judge and a particular task setup; rankings are not general hallucination rates.

### Capabilities and behavioral probes

- [WMDP](https://github.com/centerforaisafety/wmdp) - Hazardous-knowledge multiple-choice questions in biology, chemistry and cybersecurity; a proxy rather than an operational capability test.
- [LABBench2](https://github.com/EdisonScientific/labbench2) - Scientific research tasks and an evaluation harness; measures research capabilities, not harmful-use or wet-lab outcomes.
- [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks) - Cybersecurity evaluation code from PurpleLlama; task suites measure different attack and assistance behaviors.
- [MACHIAVELLI](https://github.com/aypan17/machiavelli) - Text-game benchmark of agent competence and harmful or unethical choices in simulated scenarios.
- [DecodingTrust](https://github.com/AI-secure/DecodingTrust) - Evaluation suite covering multiple trustworthiness dimensions on specified tasks and models.
- [Anthropic Model-Written Evaluations](https://github.com/anthropics/evals) - **Historical data.** Model-generated evaluations of persona, sycophancy, risk-related behavior and bias, released under CC BY 4.0.

## Formal verification and execution evidence

### Neural-network properties

Formal results apply to specified networks, input domains, numerical semantics and properties. They do not verify unrestricted language-model behavior.

- [alpha-beta-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) - Bound propagation and branch-and-bound for specified neural-network properties.
- [auto_LiRPA](https://github.com/Verified-Intelligence/auto_LiRPA) - Compute certified bounds for supported neural-network computation graphs.
- [Marabou](https://github.com/NeuralNetworkVerification/Marabou) - Solver for neural-network input/output properties expressed through supported interfaces and VNNLIB.
- [NNV](https://github.com/verivital/nnv) - Reachability-based verification of neural networks and controllers; requires MATLAB and explicit system models.
- [ERAN](https://github.com/eth-sri/eran) - **Research.** Abstract-interpretation reference for neural-network robustness certification.
- [VNN-COMP](https://vnn-comp.github.io/) - Competition resources, benchmarks and results for comparing neural-network verifiers.
- [Certified Adversarial Robustness via Randomized Smoothing](https://arxiv.org/abs/1902.02918) - **Paper.** Probabilistic robustness certificates under a specified noise distribution and perturbation norm.

### Computation proofs and signed evidence

A computation proof covers its encoded circuit or program under the proof system's assumptions. Quantization, public/private inputs and model commitments matter. Signed receipts authenticate statements and expose some tampering; check who can observe and attest the underlying event.

- [zkml](https://github.com/ddkang/zkml) - **Research.** Halo2 proof-of-concept for supported ONNX inference computations.
- [Orion](https://github.com/gizatechxyz/orion) - **Historical.** Archived Cairo implementation of ONNX inference operators for verifiable computation.
- [Signet](https://github.com/Prismer-AI/signet) - Signed agent-action receipts and policy evidence; execution remains an assertion unless independently observed.
- [Phionyx](https://github.com/halvrenofviryel/phionyx-research) - **Research.** Experimental governance gates and signed replay evidence; no independent validation of safety effectiveness is established here.
- [Remote Attestation Procedures Architecture](https://www.rfc-editor.org/rfc/rfc9334.html) - **Standard.** Roles, evidence and appraisal for remote attestation; measured platform state is evaluated under an explicit policy.

## Governance and assurance

### Official frameworks and application security

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Voluntary framework organized around Govern, Map, Measure and Manage.
- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) - Generative AI risk-management actions that accompany the AI RMF.
- [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) - Secure-development practices for generative AI and foundation-model producers, used with the SSDF.
- [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) - Commission overview of the risk-based regulatory framework, with links to legislation and current implementation guidance.
- [GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) - Voluntary guidance supporting general-purpose AI transparency, copyright and systemic-risk obligations.
- [OWASP LLM Top 10](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) - Application-security risks, attack scenarios and mitigations in the 2026 edition.
- [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) - Threats and mitigations for agentic applications in the 2026 edition.
- [AISI Cyber Safety-Case Template](https://www.aisi.gov.uk/research/safety-case-template-for-frontier-ai-a-cyber-inability-argument-2) - Research template connecting risk models, proxy tasks and evaluation evidence in a structured assurance argument.

### Fairness assessment

Metrics depend on the affected population, decision context and definition of harm. A score alone does not establish sociotechnical fairness.

- [AI Fairness 360](https://github.com/Trusted-AI/AIF360) - Dataset and model fairness metrics with mitigation algorithms and examples.
- [Fairlearn](https://github.com/fairlearn/fairlearn) - Group-fairness assessment and mitigation for machine-learning systems.
- [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) - Interfaces for model/data exploration, error analysis and fairness assessment.

## Research papers and reports

Years below refer to the first public version. Later revisions may change results. Empirical findings describe their experimental settings; conceptual proposals describe an approach, not demonstrated deployment guarantees.

### Foundations and alignment methods

| Year | Resource | Scope |
|---|---|---|
| 2012 | [The Superintelligent Will](https://nickbostrom.com/superintelligentwill.pdf) | Argument for instrumental convergence across many possible final goals. |
| 2015 | [Research Priorities for Robust and Beneficial AI](https://arxiv.org/abs/1602.03506) | Research agenda spanning technical robustness, control and societal impacts. |
| 2016 | [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) | Side effects, reward hacking, scalable supervision, safe exploration and distributional shift. |
| 2017 | [Deep RL from Human Preferences](https://arxiv.org/abs/1706.03741) | Learn reward signals from comparisons of agent behavior. |
| 2018 | [AI Safety via Debate](https://arxiv.org/abs/1805.00899) | Proposal for adversarial debate judged by weaker overseers. |
| 2018 | [Scalable Agent Alignment via Reward Modeling](https://arxiv.org/abs/1811.07871) | Recursive reward-modeling research agenda for scalable supervision. |
| 2019 | [Risks from Learned Optimization](https://arxiv.org/abs/1906.01820) | Mesa-optimization and the possibility of objectives differing from the training objective. |
| 2019 | [Optimal Policies Tend to Seek Power](https://arxiv.org/abs/1912.01683) | Conditional results on power-seeking in Markov decision processes. |
| 2021 | [Goal Misgeneralization in Deep RL](https://arxiv.org/abs/2105.14111) | Experiments where capabilities generalize while the learned goal does not. |
| 2022 | [InstructGPT](https://arxiv.org/abs/2203.02155) | Instruction-following language-model training with demonstrations and preference feedback. |
| 2022 | [Constitutional AI](https://arxiv.org/abs/2212.08073) | Critique and preference training guided by written principles. |
| 2022 | [Red Teaming Language Models](https://arxiv.org/abs/2209.07858) | Human red-teaming study of language-model failure modes. |
| 2023 | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | Optimize a preference objective directly without training a separate reward model. |
| 2023 | [Weak-to-Strong Generalization](https://arxiv.org/abs/2312.09390) | Study stronger models trained using weaker model supervision. |
| 2023 | [AI Control](https://arxiv.org/abs/2312.06942) | Evaluate monitoring and editing protocols against intentionally subversive code generation. |
| 2024 | [Debating with More Persuasive LLMs](https://arxiv.org/abs/2402.06782) | Weaker judges supervise stronger debaters on information-asymmetric question answering. |
| 2024 | [Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624) | Proposed certificates relative to explicit world models, specifications and verifiers. |

### Failure modes and auditing

| Year | Resource | Scope |
|---|---|---|
| 2024 | [Sleeper Agents](https://arxiv.org/abs/2401.05566) | Intentionally backdoored models can retain triggered behavior after the tested safety-training procedures. |
| 2024 | [Alignment Faking](https://arxiv.org/abs/2412.14093) | Experiments on context-dependent behavior when a model is told about its training process. |
| 2024 | [Sycophancy to Subterfuge](https://arxiv.org/abs/2406.10162) | Study generalization from specification gaming to reward tampering in constructed environments. |
| 2024 | [Unlearning or Obfuscating?](https://arxiv.org/abs/2406.13356) | Benign relearning can recover information suppressed by the tested approximate unlearning methods. |
| 2025 | [Emergent Misalignment](https://arxiv.org/abs/2502.17424) | Broad behavioral changes after narrow insecure-code fine-tuning, with model and context dependence. |
| 2025 | [SAEBench](https://arxiv.org/abs/2503.09532) | Compare sparse autoencoders across interpretability and application metrics; proxy gains need not improve practical performance. |
| 2026 | [AuditBench](https://arxiv.org/abs/2602.22755) | Evaluate auditing tools on models with deliberately implanted hidden behaviors. |
| 2026 | [Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/) | Deliberate training on vulnerable reward environments and bounded tests of subsequent reward-seeking behavior. |

### Behavioral specifications

- [Claude's Constitution](https://www.anthropic.com/constitution) - Published training and behavior specification; stated values do not establish consistent model adherence.

## Research groups

Links lead to primary research feeds or organizational pages. Their inclusion is a route to research, not an endorsement of every claim or policy.

| Group | Research route |
|---|---|
| [Anthropic](https://www.anthropic.com/research) | Alignment, interpretability and model evaluations. |
| [Google DeepMind](https://deepmind.google/responsibility-and-safety/) | Responsibility, safety research and evaluation publications. |
| [OpenAI](https://openai.com/safety/) | Safety, alignment and preparedness publications. |
| [Redwood Research](https://www.redwoodresearch.org/) | AI control and evaluation of deceptive behavior. |
| [ARC](https://www.alignment.org/) | Theoretical research on explaining model behavior. |
| [METR](https://metr.org/) | Evaluations of autonomous model and agent capabilities. |
| [Center for AI Safety](https://safe.ai/) | Risk research, evaluations and educational resources. |
| [FAR AI](https://www.far.ai/) | Technical AI-safety research and research support. |
| [Apollo Research](https://www.apolloresearch.ai/) | Evaluating deceptive behavior and related model risks. |
| [MIRI](https://intelligence.org/) | Research and policy work focused on advanced AI risk. |
| [UK AI Security Institute](https://www.aisi.gov.uk/) | Frontier AI risk and mitigation research. |
| [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office) | General-purpose AI oversight and AI Act implementation. |
| [NIST](https://www.nist.gov/super-intelligence) | Measurement, standards and risk-management publications. |

## Learning resources

- [BlueDot AI Alignment Curriculum](https://bluedot.org/courses/alignment) - Public reading curriculum on alignment problems, methods and research directions.
- [ARENA Curriculum](https://learn.arena.education/) - Exercises in interpretability, reinforcement learning, evaluations and alignment science.
- [ML Safety Course](https://course.mlsafety.org/) - Technical lectures and assignments covering machine-learning safety topics.
- [MATS](https://www.matsprogram.org/) - Mentored AI-safety research program; admissions and participation terms vary by cohort.
- [AI Safety Camp](https://www.aisafety.camp/) - Collaborative AI-safety research program with project-based teams.
- [Alignment Forum](https://www.alignmentforum.org/) - Community discussion of alignment research; posts vary in evidence and review status.
- [AI Safety Landscape Map](https://aisafety.com/map) - Community-maintained directory for discovering organizations and projects; check primary sources after discovery.

## Contributing

Propose a resource or correction through a pull request. Include primary-source evidence, license or access terms, reproduction instructions where applicable, and the gap it fills. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [methodology](docs/methodology.md).

## License

The original descriptions and arrangement of this list are dedicated to the public domain under [CC0 1.0](LICENSE). Linked resources retain their own licenses and terms.
