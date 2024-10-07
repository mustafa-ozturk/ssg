import unittest

from blocks_markdown import (
    markdown_to_blocks,
    markdown_block_type_code,
    markdown_block_type_quote,
    markdown_block_type_heading,
    markdown_block_type_paragraph,
    markdown_block_type_ordered_list,
    markdown_block_type_unordered_list,
    block_to_block_type
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# heading"), markdown_block_type_heading)
        self.assertEqual(block_to_block_type("## heading"), markdown_block_type_heading)
        self.assertEqual(block_to_block_type("### heading"), markdown_block_type_heading)
        self.assertEqual(block_to_block_type("#### heading"), markdown_block_type_heading)
        self.assertEqual(block_to_block_type("##### heading"), markdown_block_type_heading)
        self.assertEqual(block_to_block_type("###### heading"), markdown_block_type_heading)
        self.assertNotEqual(block_to_block_type("#     "), markdown_block_type_heading)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```code```"), markdown_block_type_code)
        self.assertEqual(block_to_block_type("""```
code
```"""), markdown_block_type_code)
        self.assertNotEqual(block_to_block_type("```code"), markdown_block_type_code)
        self.assertNotEqual(block_to_block_type("code```"), markdown_block_type_code)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> quote"), markdown_block_type_quote)
        self.assertEqual(block_to_block_type("""> quote
> quote
> quote
> quote"""), markdown_block_type_quote)
        self.assertNotEqual(block_to_block_type("""
> quote"""), markdown_block_type_quote)

    def test_block_to_block_type_ul(self):
        self.assertEqual(block_to_block_type("* ul"), markdown_block_type_unordered_list)
        self.assertEqual(block_to_block_type("""* ul
* ul
* ul"""), markdown_block_type_unordered_list)
        self.assertEqual(block_to_block_type("""* ul
- ul
- ul"""), markdown_block_type_unordered_list)
        self.assertNotEqual(block_to_block_type("*ul"), markdown_block_type_unordered_list)

    def test_block_to_block_type_ol(self):
        self.assertEqual(block_to_block_type("1. ol"), markdown_block_type_ordered_list)

    def test_block_to_block_type_p(self):
        self.assertEqual(block_to_block_type("hello world"), markdown_block_type_paragraph)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), markdown_block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), markdown_block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), markdown_block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), markdown_block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), markdown_block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), markdown_block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
