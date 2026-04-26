import unittest
from textnode import TextNode, TextType
from textnode_to_html import text_node_to_html_node

class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold tag", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold tag")

    def test_link(self):
        node = TextNode("Click", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click")
        self.assertEqual(html_node.props["href"], "google.com")

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt"], "alt text")
        self.assertEqual(html_node.props["src"], "img.png")

if __name__ == "__main__":
    unittest.main()
