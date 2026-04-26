import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_without_props(self):
        node = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_with_empty_props(self):
        node = HTMLNode(tag="div", value="Content", props={})
        self.assertEqual(node.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()
