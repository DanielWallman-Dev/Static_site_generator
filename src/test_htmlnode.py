import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode( "","", "", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "My bridge")
        self.assertEqual(node.to_html(), "<p>My bridge</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "My bridge")
        self.assertEqual(node.to_html(), "My bridge")


if __name__ == "__main__":
    unittest.main()
