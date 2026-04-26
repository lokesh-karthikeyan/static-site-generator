import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_blocks(self):
        md = """
This is a paragraph

     

This is another paragraph with excessive newlines


And this is the final paragraph.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph",
                "This is another paragraph with excessive newlines",
                "And this is the final paragraph.",
            ],
        )

    def test_trailing_newlines(self):
        md = """
This is a paragraph with a trailing newline


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["This is a paragraph with a trailing newline"],
        )

    def test_leading_newlines(self):
        md = """

This is a paragraph with leading newlines
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["This is a paragraph with leading newlines"],
        )

if __name__ == "__main__":
    unittest.main()
