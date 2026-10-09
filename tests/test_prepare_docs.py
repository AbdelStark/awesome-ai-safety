"""Ensure source links survive the site's different document root."""
import unittest

from scripts.prepare_docs import site_markdown


class SiteLinks(unittest.TestCase):
    def test_repository_links_become_site_links(self):
        source = '[contribute](CONTRIBUTING.md#local-checks) [method](docs/methodology.md#scope) [license](LICENSE)'
        expected = '[contribute](contributing.md#local-checks) [method](methodology.md#scope) '
        expected += '[license](https://github.com/AbdelStark/awesome-ai-safety/blob/main/LICENSE)'
        self.assertEqual(site_markdown(source), expected)
        self.assertEqual(site_markdown('[anchor](#scope) [web](https://example.org/docs/)'),
                         '[anchor](#scope) [web](https://example.org/docs/)')


if __name__ == '__main__':
    unittest.main()
