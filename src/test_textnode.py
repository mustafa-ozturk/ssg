import unittest

from textnode import TextNode


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
