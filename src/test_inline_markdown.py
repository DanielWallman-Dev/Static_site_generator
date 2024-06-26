import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("Under a **bolded** dome", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Under a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" dome", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode("Under a **bolded** dome and **bridge**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Under a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" dome and ", text_type_text),
                TextNode("bridge", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode("Under a **bolded dome** and **bridge**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("Under a ", text_type_text),
                TextNode("bolded dome", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("bridge", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("Under an *italic* dome", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("Under an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" dome", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**dome** and *bridge*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("dome", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("bridge", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_coded(self):
        node = TextNode("Under a `coded` dome", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("Under a ", text_type_text),
                TextNode("coded", text_type_code),
                TextNode(" dome", text_type_text),
            ],
            new_nodes,
        )
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("Under a dome with an ![image](https://image.com/dome.pgn)")
        self.assertListEqual([("image", "https://image.com/dome.pgn")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is a dome with a [link](https://image.com)")
        self.assertListEqual([("link", "https://image.com")], matches)
    
if __name__ == "__main__":
    unittest.main()