import unittest

from blocks import markdown_to_blocks, block_to_block_type

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


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        type = block_to_block_type("###### heading")
        expected_type = "heading"
        self.assertEqual(type, expected_type)
    
    def test_code(self):
        markdown = """```
some code
```
"""
        blocks = markdown_to_blocks(markdown)
        type = block_to_block_type(blocks[0])
        expected_type = "code"
        self.assertEqual(type, expected_type)

    def test_quote(self):
        markdown = """
> this
> is
> a 
> quote
"""
        blocks = markdown_to_blocks(markdown)
        type = block_to_block_type(blocks[0])
        expected_type = "quote"
        self.assertEqual(type, expected_type)

    def test_unordered_list_star(self):
        markdown = """
* 1
* 2
* 3 
"""
        blocks = markdown_to_blocks(markdown)
        type = block_to_block_type(blocks[0])
        expected_type = "unordered_list"
        self.assertEqual(type, expected_type)
    
    def test_unordered_list_dash(self):
        markdown = """
- 1
- 2
- 3 
"""
        blocks = markdown_to_blocks(markdown)
        type = block_to_block_type(blocks[0])
        expected_type = "unordered_list"
        self.assertEqual(type, expected_type)

    def test_ordered_list(self):
        markdown = """
1. one
2. two
3. three
"""
        blocks = markdown_to_blocks(markdown)
        type = block_to_block_type(blocks[0])
        expected_type = "ordered_list"
        self.assertEqual(type, expected_type)
    
    def test_paragraph(self):
        markdown = """
hello world
"""
        blocks = markdown_to_blocks(markdown)
        type = block_to_block_type(blocks[0])
        expected_type = "paragraph"
        self.assertEqual(type, expected_type)

                                
