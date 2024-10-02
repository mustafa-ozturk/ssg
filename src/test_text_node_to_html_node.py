import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode
from leafnode import LeafNode

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
