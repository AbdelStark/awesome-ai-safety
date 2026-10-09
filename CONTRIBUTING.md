# Contributing to Awesome AI Safety

Small, evidence-backed contributions are welcome. Edit `README.md`, the catalog's source of truth. The website copies it during the build.

## What belongs

- Tools with an explicit project license, documented use and a concrete AI-safety workflow.
- Public benchmarks and datasets with stated access and reuse terms, including clearly labeled restrictions.
- Freely readable papers or research reports with a defined question, method and limitations.
- Official governance sources, standards, research feeds and accessible learning material.
- Stable research artifacts that preserve a distinct method or reproducible baseline, labeled **Research** or **Historical**.

New work can qualify through a runnable reproduction path. Established work can qualify through documented independent use. Stars, citation counts and institutional affiliation alone are insufficient. Maintainer-owned resources follow the same rules.

Exclude commercial product directories, unsupported effectiveness claims, generic engineering tools without a safety-specific use, duplicates and code without a clear reuse grant. A useful paper can be included even when its accompanying code is not eligible as open-source software.

## Proposing an entry

1. Find the closest section and explain the gap your entry fills.
2. Read the primary source, not a search snippet or a summary of it.
3. Use a canonical URL and one concise sentence. State what the resource does; qualify material limits or restrictions.
4. In the PR, cite the source section supporting the description, the license/access terms and a reproduction example or independent use.
5. Declare authorship, employment, funding or other affiliation with the resource. Self-submissions are welcome and face the same review.
6. Run the local checks below. New sections can be proposed in the same PR with a rationale.

```markdown
- [Resource Name](https://example.org/resource) - One sentence describing its concrete use and material scope.
- [Reference Method](https://example.org/reference) - **Research.** A stable reference implementation, with a bounded description.
```

Order entries by practitioner workflow, then by distinct relevance. The order is not a ranking of safety or quality. Add an entry once; use section links for navigation instead of duplicating it.

## Reviewing maintenance and terms

A recent commit is a signal, not proof of maintenance. Check releases, deprecation notices, supported interfaces and the documented run path. Review tools with no activity for twelve months; retain only when the stable-reference exception is justified. Label archived or superseded resources **Historical** and name the replacement when known.

Inspect the actual project license. A vendored dependency's license does not license the application. Dataset assets, pretrained weights and hosted features may have separate restrictions. Clearly mark restricted public artifacts; do not call them unrestricted open source.

For numeric results, cite the specific version and include the experimental conditions. Avoid claims such as best, standard, production-ready or guaranteed safe. See the [methodology](docs/methodology.md) for claim boundaries and evaluation reporting.

## Local checks

Use Python 3.12 and an environment outside the checkout if your workspace requires one:

```bash
python3.12 -m venv /tmp/awesome-ai-safety-venv
/tmp/awesome-ai-safety-venv/bin/python -m pip install -r requirements-docs.txt
/tmp/awesome-ai-safety-venv/bin/python -m unittest discover -s tests
/tmp/awesome-ai-safety-venv/bin/python scripts/check.py
/tmp/awesome-ai-safety-venv/bin/python scripts/prepare_docs.py
/tmp/awesome-ai-safety-venv/bin/mkdocs build --strict
```

Preview with `mkdocs serve` from that environment. Do not edit generated `docs/index.md`, `docs/contributing.md` or `site/`.

External links are checked separately by the **Links** workflow, on a weekly schedule and on manual dispatch. To reproduce it with [lychee](https://github.com/lycheeverse/lychee), run `lychee --config .lychee.toml README.md CONTRIBUTING.md docs/methodology.md docs/review-*.md`. Investigate failures at the source. A blocked automated request is not a successful link check; record any narrow exemption and its manual verification date.

Documentation dependencies are pinned in `requirements-docs.txt`. Update the three direct versions in `requirements-docs.in`, regenerate with `uv pip compile requirements-docs.in --python-version 3.12 --no-header --output-file requirements-docs.txt`, and run the same checks.

## Conduct

Be respectful, precise and constructive. Critique claims and methods. Explain corrections with sources, and disclose unresolved uncertainty. Inclusion is an editorial decision, not certification or endorsement.
