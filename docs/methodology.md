# Curation methodology

This catalog helps practitioners find a resource for a concrete question. It is selective, not exhaustive. Inclusion is not an endorsement, a security audit or a claim that a system is safe. The order follows workflows rather than a league table.

## Scope and admission

An entry must fill a distinct AI-safety need: evaluating capabilities or failure modes, studying alignment or control, understanding model computation, enforcing an application boundary, verifying a specified property, or managing risks with evidence.

Review the following before adding or retaining a resource:

| Criterion | Evidence required |
|---|---|
| Relevance | A concrete task or threat model, and a gap not already covered by a close equivalent. |
| Primary source | The publisher's paper, repository, documentation, regulator or standard. Discover through secondary sources, then verify at the source. |
| Access and terms | A working public resource and explicit terms. Inspect the project license itself; code, datasets, weights and embedded assets may differ. |
| Usability | Documented commands, examples, data or experimental setup. For established tools, documented independent use is additional evidence. |
| Claim scope | A description supported by the source, with material restrictions and limitations. No unsupported ranking, performance or compliance claims. |
| Maintenance | Check current releases, archive/deprecation notices, supported interfaces and the reproduction path. Commit recency alone is insufficient. |
| Independence | Disclose submitter or maintainer affiliation. Apply the same criteria to their own projects. |

A runnable reproduction path can justify new work before it gains widespread use. Citation counts, stars and an institutional name are not substitutes for method and evidence. Papers can be listed even when accompanying code lacks a clear license, but the code must not be described as open-source software.

Commercial product directories and generic tracing, training, cloud or cryptographic infrastructure are excluded unless the entry supplies a distinct safety-specific method or artifact. We prefer one useful canonical entry over several overlapping wrappers.

## Resource labels

- **Research:** a stable reference implementation, research dataset or experimental method. It may require old dependencies or model APIs. Do not infer ongoing maintenance or validated effectiveness.
- **Historical:** an archived or superseded artifact retained for methodological or reproducibility value. Prefer a current replacement for new projects when one exists.
- **Restricted:** a public benchmark or model whose terms impose additional use restrictions. Public access and open weights do not necessarily mean unrestricted open-source software.
- **Paper, Standard, Research data, Research weights:** identify the artifact when treating it as a software library would mislead.

The benchmarks section is a collection of bounded research artifacts, including older baselines. Age alone is not grounds to discard a reproducible method. A tool with no activity for twelve months receives a maintenance review; it stays only with a justified reference role and an appropriate label. An unmaintained application with no distinct research value is removed.

## What the evidence supports

| Evidence | Supports | Requires more evidence |
|---|---|---|
| Sampled evaluations | Behavior or capability on stated tasks, attacks and budgets. | Coverage outside the sample, operational consequences, robustness to stronger elicitation and generalization. |
| Interpretability experiments | Hypotheses about internal computation, strengthened by interventions. | Faithfulness and completeness of the explanation, and effectiveness of a proposed safety intervention. |
| Formal verification | An encoded property for a specified network/program, domain and semantics under the verifier's assumptions. | Correct specifications, deployment equivalence and unrestricted semantic safety. |
| Cryptographic computation proofs | A specified computation related to public inputs, outputs or commitments under the proof system's assumptions. | Correct circuits, numerical equivalence, identity binding and correspondence with all deployed executions. |
| Signatures and audit trails | Authenticity of a signed statement or artifact, and some detectable modifications. | Truth of the statement, completeness of logging and independent observation of execution. |
| Hardware attestation | Evidence about measured platform state, appraised under a relying party's policy. | Coverage, sound measurements, runtime behavior and security of the trusted components. |
| Governance frameworks | A structured process for identifying and addressing risk. | Implementation quality, evidence for each assurance claim and applicable legal interpretation. |

A model passing an evaluation is not equivalent to proving the evaluation ran on every deployed model. A proof of inference is not proof that an output is harmless. Fairness and harmfulness also require contextual judgments that a metric cannot settle by itself.

## Evaluating evaluation results

Before using a result to make a deployment or research decision, ask:

1. **What is being tested?** State the threat model, attacker access, task distribution and the observable success criterion. Separate knowledge proxies, synthetic tools, CTF tasks and real software tasks.
2. **What system ran?** Record model version, prompts, sampling settings, harness/scorer versions, tool permissions, sandbox/network boundaries and available context.
3. **How hard was it tried?** Record attempts, time/token/compute budgets, scaffolding, elicitation improvements and fixable execution failures. A weak scaffold can hide capability.
4. **Is the score valid?** Validate judges against reviewed examples. Report false positives, false negatives, partial completion and benign task utility, including over-refusal.
5. **What uncertainty remains?** Use repeated trials when stochastic behavior matters, report variation or confidence intervals, and explain sample selection and contamination controls.
6. **Can another person inspect it?** Provide task/scorer versions, run instructions, sanitized logs and negative results where release is appropriate. State withheld materials and reproduction limits.

These questions are informed by [METR's capability-elicitation guidance](https://metr.org/blog/2024-03-15-guidelines-for-capability-elicitation/), [HELM Safety's limitations](https://crfm.stanford.edu/2024/11/08/helm-safety.html) and the [Inspect sandbox boundary](https://inspect.aisi.org.uk/sandboxing.html). They are a reporting checklist, not a certification scheme.

## Review and maintenance

- **Each PR:** verify source claims, terms, distinct value and labels. Run the catalog checker and strict site build. CI checks structure; a human review still checks evidence.
- **Weekly:** the Links workflow requests published URLs and records failures. It does not file issues or edit entries automatically. Investigate redirects, soft 404s and blocked requests manually.
- **Quarterly target:** review maintenance notices, key benchmark/scorer changes, governance source updates and gaps in practitioner workflows. This is an editorial target, not an automated research review.
- **On a material change:** correct the canonical entry and append a dated review note. Explain removals and unresolved evidence so decisions remain inspectable.

`README.md` is the catalog's source of truth. `scripts/prepare_docs.py` creates the site's copies, and pinned documentation dependencies build them in CI. Markdown links and heading anchors are checked locally. External checks cannot determine semantic relevance, licensing or truth.

## Review record and assistance

See the [2026-10-09 review](review-2026-10-09.md) for source-level corrections, additions and exclusions. Reviews distinguish reading documentation from executing a benchmark or auditing a proof system.

The October 2026 refresh used AI-assisted source discovery, comparison and drafting, followed by editorial checks against primary sources. It did not independently reproduce the listed research results. Corrections with specific evidence are welcome through the contribution process.
