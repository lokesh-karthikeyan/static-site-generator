import unittest
from textnode import TextNode, TextType
from split_nodes_link import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        node = TextNode(
            "Here is a [link](http://example.com/img.png)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("Here is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "http://example.com/img.png"),
            ],
            result,
        )

    def test_multiple_links(self):
        node = TextNode(
            "[one](url1) and [two](url2)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("one", TextType.LINK, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.LINK, "url2"),
            ],
            result,
        )

    def test_link_in_middle(self):
        node = TextNode(
            "Text before [img](url) text after",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.TEXT),
                TextNode("img", TextType.LINK, "url"),
                TextNode(" text after", TextType.TEXT),
            ],
            result,
        )

    def test_no_links(self):
        node = TextNode(
            "Just plain text",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertListEqual([node], result)

    def test_link_at_start(self):
        node = TextNode(
            "[start](url) then text",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("start", TextType.LINK, "url"),
                TextNode(" then text", TextType.TEXT),
            ],
            result,
        )

    def test_link_at_end(self):
        node = TextNode(
            "text then [end](url)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("text then ", TextType.TEXT),
                TextNode("end", TextType.LINK, "url"),
            ],
            result,
        )

if __name__ == "__main__":
    unittest.main()
