import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_with_headings(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_with_multi_level_heading(self):
        md = """
## Not this
### Also not this
# Real Title
"""
        self.assertEqual(extract_title(md), "Real Title")

    def test_no_heading(self):
        md = """
This is a paragraph

## No H1 here
Just text
"""
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
