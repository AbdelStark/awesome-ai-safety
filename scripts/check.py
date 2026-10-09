"""Check published Markdown links, catalog duplicates and writing mechanics."""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.targets = []
        self.ids = set()
        self.feed(markdown.markdown(text, extensions=['tables', 'toc', 'fenced_code']))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag in ('a', 'img'):
            self.targets.append(attrs.get('href' if tag == 'a' else 'src', ''))


def errors(path):
    text = path.read_text()
    problems = []
    if re.search('[\u2013\u2014]', text):
        problems.append('use plain hyphens instead of en/em dashes')
    if re.search(r'^(<<<<<<<|=======|>>>>>>>)', text, re.M):
        problems.append('unresolved merge marker')
    for target in Links(text).targets:
        url = urlsplit(target)
        if url.scheme or url.netloc:
            continue
        destination = path.parent / unquote(url.path) if url.path else path
        if not destination.is_file():
            problems.append(f'missing file: {target}')
        elif url.fragment and destination.suffix == '.md':
            if unquote(url.fragment) not in Links(destination.read_text()).ids:
                problems.append(f'missing heading: {target}')
    return problems


def duplicate_resources(text):
    # shortcut: catalog entries use inline links, extend if the format changes.
    text = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1[ \t]*$', '', text)
    resources = re.findall(r'^(?:- |\| (?:[^|\n]*\| )?)\[[^\]]+\]\((https?://[^)]+)\)', text, re.M)
    seen, duplicates = set(), []
    for url in resources:
        key = url.rstrip('/')
        if urlsplit(url).hostname == 'github.com':
            key = key.lower()
        if key in seen:
            duplicates.append(url)
        seen.add(key)
    return duplicates


if __name__ == '__main__':
    files = [ROOT / 'README.md', ROOT / 'CONTRIBUTING.md',
             ROOT / '.github/pull_request_template.md',
             ROOT / 'docs/methodology.md', *sorted((ROOT / 'docs').glob('review-*.md'))]
    problems = [f'{path.relative_to(ROOT)}: {error}' for path in files for error in errors(path)]
    problems += [f'README.md: duplicate resource: {url}'
                 for url in duplicate_resources((ROOT / 'README.md').read_text())]
    for problem in problems:
        print(problem)
    if problems:
        raise SystemExit(1)
    print(f'Catalog checks passed ({len(files)} Markdown files).')
