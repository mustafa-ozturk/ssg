import unittest

from blocks import markdown_to_blocks

class TestMarkdownToBlovks(unittest.TestCase):
    def test_common_case(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(markdown)
        expected_blocks = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", """* This is the first list item in a list block
* This is a list item
* This is another list item"""]
        for i in range(len(blocks)):
            self.assertEqual(blocks[i], expected_blocks[i])
    
    def test_empty_blocks(self):
        markdown = """



# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item




"""
        blocks = markdown_to_blocks(markdown)
        expected_blocks = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", """* This is the first list item in a list block
* This is a list item
* This is another list item"""]
        for i in range(len(blocks)):
            self.assertEqual(blocks[i], expected_blocks[i])
    
    def test_empty_markdown(self):
        markdown = ""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 0)
