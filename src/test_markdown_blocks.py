import unittest
from markdown_blocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
Under a **bolded** dome

With an *italic* bridge and `coded` sign
This is the same bridge and sign on a new line

* This is a dome
* with bridges
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Under a **bolded** dome",
                "With an *italic* bridge and `coded` sign\nThis is the same bridge and sign on a new line",
                "* This is a dome\n* with bridges",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
Under a **bolded** dome




With an *italic* bridge and `coded` sign
This is the same bridge and sign on a new line

* This is a dome
* with bridges
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "Under a **bolded** dome",
                "With an *italic* bridge and `coded` sign\nThis is the same bridge and sign on a new line",
                "* This is a dome\n* with bridges",
            ],
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ndome and bridge\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> dome\n> bridge"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* domes\n* bridge"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "- domes\n- bridge"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. dome\n2. bridge"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "dome and bridges"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_paragraphs(self):
        md = """
This is **bolded** dome
text in a p
tag here

This is a bridge with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> dome text in a p tag here</p><p>This is a bridge with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a dome
- with items
- and *more* items

1. This is an `ordered` bridge
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a dome</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> bridge</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is dome text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is dome text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is dome text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is dome text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()
