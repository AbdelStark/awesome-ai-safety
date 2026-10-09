"""Regression checks for catalog links and duplicate detection."""
from pathlib import Path
import tempfile
import unittest

from scripts.check import duplicate_resources, errors


class CatalogChecks(unittest.TestCase):
    def test_cross_file_heading_and_encoded_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'other page.md').write_text('# Evaluation and red teaming\n')
            source = root / 'README.md'
            source.write_text('[go](other%20page.md#evaluation-and-red-teaming)\n')
            self.assertEqual(errors(source), [])
            source.write_text('[go](other%20page.md#missing)\n[absent](absent.md)\n')
            self.assertEqual(len(errors(source)), 2)

    def test_fenced_examples_are_not_links_or_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'README.md'
            source.write_text('# Real\n[go](#real)\n```markdown\n[example](absent.md)\n# Fake\n```\n')
            self.assertEqual(errors(source), [])
            source.write_text(source.read_text() + '[bad](#fake)\n')
            self.assertEqual(errors(source), ['missing heading: #fake'])

    def test_list_and_table_duplicates_ignore_navigation(self):
        text = '- [first](https://github.com/Org/Repo) - Tool.\n'
        text += '| 2026 | [second](https://github.com/org/repo/) | Paper. |\n'
        text += '```markdown\n- [example](https://github.com/Org/Repo) - Example.\n```\n'
        text += '- [section](#first)\nSee [first](https://github.com/Org/Repo).\n'
        self.assertEqual(duplicate_resources(text), ['https://github.com/org/repo/'])

    def test_mechanics_and_conflict_markers(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'README.md'
            source.write_text('Text \u2014 more.\n<<<<<<< HEAD\n')
            self.assertEqual(len(errors(source)), 2)


if __name__ == '__main__':
    unittest.main()
