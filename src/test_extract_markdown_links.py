import unittest
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://i.imgur.com/zjjcJKZ.png")])

    def test_multiple_links(self):
        text = "[one](url1) some text [two](url2)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("one", "url1"), ("two", "url2")])

    def test_no_links(self):
        text = "This has no links, just a ![image](http://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_empty_link_text(self):
        text = "[](http://example.com/image.png)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("", "http://example.com/image.png")])

if __name__ == "__main__":
    unittest.main()
