import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    )


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_diff(self):
        node1 = TextNode("Under the bridge", "bold", None)
        node2 = TextNode("Under the bridge", "bold", "https://test.com")
        self.assertNotEqual(node1, node2)

    def test_diff_text(self):
        node1 = TextNode("Under the bridge", "bold", "https://test.com")
        node2 = TextNode("Under a dome", "bold", "https://test.com")
        self.assertNotEqual(node1, node2)

    def test_diff_text_type(self):
        node1 = TextNode("Under a dome", "bold", "https://test.com")
        node2 = TextNode("Under a dome", "italic", "https://test.com")
        self.assertNotEqual(node1, node2)

    def test_eq_url(self):
        node = TextNode("Under a dome", text_type_text, "https://test.com")
        node2 = TextNode("Under a dome", text_type_text, "https://test.com")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("Under a dome", text_type_text, "https://test.com")
        self.assertEqual("TextNode(Under a dome, text, https://test.com)", repr(node))
        
if __name__ == "__main__":
    unittest.main()