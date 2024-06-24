import unittest

from textnode import TextNode


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

if __name__ == "__main__":
    unittest.main()