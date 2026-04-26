import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_simple_text(self):
        text = "Just plain text"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("Just plain text", TextType.TEXT)],
            result
        )

    def test_bold_text(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            result
        )

    def test_italic_text(self):
        text = "This is an _italic_ word"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            result
        )

    def test_code_block(self):
        text = "This is a `code block`"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ],
            result
        )

    def test_image_and_link(self):
        text = "An image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("An image ", TextType.TEXT),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result
        )

    def test_combined(self):
        text = "This is **bold** with _italic_ and a `code block`, an ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(", an ", TextType.TEXT),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(", and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            result
        )


if __name__ == "__main__":
    unittest.main()
