import unittest
from markdown_blocks import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()
