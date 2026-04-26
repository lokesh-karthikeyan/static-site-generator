import unittest
from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("image", "https://i.imgur.com/zjjcJKZ.png")])

    def test_multiple_images(self):
        text = "![one](url1) some text ![two](url2)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("one", "url1"), ("two", "url2")])

    def test_no_images(self):
        text = "This has no images, just a [link](http://example.com)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_empty_alt_text(self):
        text = "![](http://example.com/image.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("", "http://example.com/image.png")])

if __name__ == "__main__":
    unittest.main()
