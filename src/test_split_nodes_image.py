import unittest
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = TextNode(
            "Here is an ![image](http://example.com/img.png)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "http://example.com/img.png"),
            ],
            result,
        )

    def test_multiple_images(self):
        node = TextNode(
            "![one](url1) and ![two](url2)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("one", TextType.IMAGE, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "url2"),
            ],
            result,
        )

    def test_image_in_middle(self):
        node = TextNode(
            "Text before ![img](url) text after",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text before ", TextType.TEXT),
                TextNode("img", TextType.IMAGE, "url"),
                TextNode(" text after", TextType.TEXT),
            ],
            result,
        )

    def test_no_images(self):
        node = TextNode(
            "Just plain text",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertListEqual([node], result)

    def test_image_at_start(self):
        node = TextNode(
            "![start](url) then text",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("start", TextType.IMAGE, "url"),
                TextNode(" then text", TextType.TEXT),
            ],
            result,
        )

    def test_image_at_end(self):
        node = TextNode(
            "text then ![end](url)",
            TextType.TEXT,
        )
        result = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("text then ", TextType.TEXT),
                TextNode("end", TextType.IMAGE, "url"),
            ],
            result,
        )

if __name__ == "__main__":
    unittest.main()
