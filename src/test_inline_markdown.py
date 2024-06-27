import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
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
        matches = extract_markdown_images("Under a dome with an ![image](https://image.com/dome.png)")
        self.assertListEqual([("image", "https://image.com/dome.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is a dome with a [link](https://image.com)")
        self.assertListEqual([("link", "https://image.com")], matches)

    def test_split_image(self):
        node = TextNode(
            "Under a dome with an ![image](https://image.com/dome.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Under a dome with an ", text_type_text),
                TextNode("image", text_type_image, "https://image.com/dome.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://image.com/dome.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://image.com/dome.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "Under a dome with an ![image](https://image.com/dome.png) and a ![bridge](https://image.com/bridge.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Under a dome with an ", text_type_text),
                TextNode("image", text_type_image, "https://image.com/dome.png"),
                TextNode(" and a ", text_type_text),
                TextNode(
                    "bridge", text_type_image, "https://image.com/bridge.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "Under a dome with a [link](https://image.com) and [another link](https://imagenew.com) with a bridge that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Under a dome with a ", text_type_text),
                TextNode("link", text_type_link, "https://image.com"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://imagenew.com"),
                TextNode(" with a bridge that follows", text_type_text),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "Under a **dome** with a *bridge* and a coded `sign` and an ![image](https://image.com/dome.png) and a [link](https://image.com)"
        )
        self.assertListEqual(
            [
                TextNode("Under a ", text_type_text),
                TextNode("dome", text_type_bold),
                TextNode(" with a ", text_type_text),
                TextNode("bridge", text_type_italic),
                TextNode(" and a coded ", text_type_text),
                TextNode("sign", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://image.com/dome.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://image.com"),
            ],
            nodes,
        )
    
if __name__ == "__main__":
    unittest.main()