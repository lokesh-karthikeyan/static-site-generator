import unittest
from htmlnode import ParentNode, LeafNode

class TestParenNode(unittest.TestCase):
    def test_parent_to_html(self):
        node1 = LeafNode("b", "Bold text")
        node2 = LeafNode(None, "Normal text")
        parent = ParentNode("p", [node1, node2])
        self.assertEqual(parent.to_html(), "<p><b>Bold text</b>Normal text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "Grandfather")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>Grandfather</b></span></div>")

    def test_parent_to_html_with_empty_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", [])

    def test_parent_to_html_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])
