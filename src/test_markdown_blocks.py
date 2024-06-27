import unittest
from markdown_blocks import (
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


if __name__ == "__main__":
    unittest.main()
