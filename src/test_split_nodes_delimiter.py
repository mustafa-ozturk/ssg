import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        node1 = TextNode("This is text with a ", "text")
        node2 = TextNode("code block", "code")
        node3 = TextNode(" word", "text")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)


    def test_italic(self):
        node = TextNode("This is text with a *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        node1 = TextNode("This is text with a ", "text")
        node2 = TextNode("italic", "italic")
        node3 = TextNode(" word", "text")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        node1 = TextNode("This is text with a ", "text")
        node2 = TextNode("bold", "bold")
        node3 = TextNode(" word", "text")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)

if __name__ == "__main__":
    unittest.main()
