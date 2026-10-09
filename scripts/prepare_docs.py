"""Build the site copies from the repository's Markdown sources."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def site_markdown(text):
    return (text.replace('(CONTRIBUTING.md)', '(contributing.md)')
            .replace('(CONTRIBUTING.md#', '(contributing.md#')
            .replace('(docs/', '(')
            .replace('(LICENSE)', '(https://github.com/AbdelStark/awesome-ai-safety/blob/main/LICENSE)'))


if __name__ == '__main__':
    for source, target in [('README.md', 'index.md'), ('CONTRIBUTING.md', 'contributing.md')]:
        (ROOT / 'docs' / target).write_text(site_markdown((ROOT / source).read_text()))
