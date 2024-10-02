import unittest

from inline_md import split_nodes_delimiter, split_nodes_link, split_nodes_images, text_to_textnodes
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

class TestTextToTextnodes(unittest.TestCase):
        def test_with_mixed_text(self):
            text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
            nodes = text_to_textnodes(text)
            expected_nodes = [
                TextNode("This is ", "text"),
                TextNode("text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ]
            for i in range(len(nodes) - 1):
                self.assertEqual(nodes[i], expected_nodes[i])

        def test_with_links_only(self):
            text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) [link](https://boot.dev)"
            nodes = text_to_textnodes(text)
            expected_nodes = [
                TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ]
            for i in range(len(nodes) - 1):
                self.assertEqual(nodes[i], expected_nodes[i])
        
        def test_with_text_only(self):
            text = "test text"
            nodes = text_to_textnodes(text)
            expected_nodes = [
                TextNode("test text", "text"),
            ]
            for i in range(len(nodes) - 1):
                self.assertEqual(nodes[i], expected_nodes[i])

if __name__ == "__main__":
    unittest.main()
