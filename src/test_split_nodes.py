import unittest

from split_nodes import split_nodes_delimiter, split_nodes_link, split_nodes_images
from textnode import TextNode


class TestSplitNodes(unittest.TestCase):
    def test_delimiter_code_block(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        node1 = TextNode("This is text with a ", "text")
        node2 = TextNode("code block", "code")
        node3 = TextNode(" word", "text")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)


    def test_delimiter_italic(self):
        node = TextNode("This is text with a *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        node1 = TextNode("This is text with a ", "text")
        node2 = TextNode("italic", "italic")
        node3 = TextNode(" word", "text")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)

    def test_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", "text") 
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        node1 = TextNode("This is text with a ", "text")
        node2 = TextNode("bold", "bold")
        node3 = TextNode(" word", "text")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)

    def test_link(self):
        node = TextNode(
            "[github](https://www.github.com) This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        new_nodes = split_nodes_link([node])
        node1 = TextNode("github", "link", "https://www.github.com")
        node2 = TextNode(" This is text with a link ", "text")
        node3 = TextNode("to boot dev", "link", "https://www.boot.dev")
        node4 = TextNode(" and ", "text")
        node5 = TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)
        self.assertEqual(new_nodes[3], node4)
        self.assertEqual(new_nodes[4], node5)
    
    def test_images(self):
        node = TextNode(
            "![github](https://www.github.com) This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        new_nodes = split_nodes_images([node])
        node1 = TextNode("github", "image", "https://www.github.com")
        node2 = TextNode(" This is text with an image ", "text")
        node3 = TextNode("to boot dev", "image", "https://www.boot.dev")
        node4 = TextNode(" and ", "text")
        node5 = TextNode("to youtube", "image", "https://www.youtube.com/@bootdotdev")
        self.assertEqual(new_nodes[0], node1)
        self.assertEqual(new_nodes[1], node2)
        self.assertEqual(new_nodes[2], node3)
        self.assertEqual(new_nodes[3], node4)
        self.assertEqual(new_nodes[4], node5)

if __name__ == "__main__":
    unittest.main()
