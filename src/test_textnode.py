import unittest

from textnode import TextNode, text_node_to_html_node
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("", "")
        self.assertNotEqual(node, node2)

    def test_text(self):
        text = "test"
        node = TextNode(text, "bold")
        self.assertEqual(node.text, text)

    def test_text_type(self):
        text_type = "bold"
        node = TextNode("test", "bold")
        self.assertEqual(node.text_type, text_type)


    def test_url(self):
        url = "test"
        node = TextNode("test", "bold", url)
        self.assertEqual(node.url, url)

    def test_url_none(self):
        node = TextNode("test", "bold")
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type(self):
        node = TextNode("test", "text")
        node1 = LeafNode("test")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), node1.to_html())
    
    def test_text_bold(self):
        node = TextNode("test", "bold")
        node1 = LeafNode("test", "b")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), node1.to_html())

    def test_text_italic(self):
        node = TextNode("test", "italic")
        node1 = LeafNode("test", "i")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), node1.to_html())

    def test_text_code(self):
        node = TextNode("test", "code")
        node1 = LeafNode("test", "code")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), node1.to_html())

    def test_text_link(self):
        node = TextNode("test", "link", "urltest")
        node1 = LeafNode("test", "a", {"href": ""})
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), node1.to_html())

    def test_text_image(self):
        node = TextNode("test", "image", "urltest")
        node1 = LeafNode("", "img", {"src": "urltest", "alt": "test"})
        converted_node = text_node_to_html_node(node)
        self.assertEqual(converted_node.to_html(), node1.to_html())
