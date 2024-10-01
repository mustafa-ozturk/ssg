import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_no_tag(self):
        node = LeafNode("test")
        expected_html = "test"
        self.assertEqual(node.to_html(), expected_html)


    def test_to_htlm(self):
        tag = "a"
        value = "test"
        props = { 
            "href": "https://www.github.com",
            "target": "_blank"
        }

        node = LeafNode(value, tag, props)
        expected_html = "<a href=\"https://www.github.com\" target=\"_blank\">test</a>"
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()
