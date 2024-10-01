import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_leafnode(self):
        node = ParentNode(
            [
                LeafNode("bold text", "b"),
                LeafNode("italic text", "i"),
                LeafNode("normal text")
            ],
            "p",
        )
        expected_html = "<p><b>bold text</b><i>italic text</i>normal text</p>"
        self.assertEqual(node.to_html(), expected_html)
    
    def test_to_html_with_parentnode(self):
        node = ParentNode(
            [
                ParentNode([LeafNode("bold text", "b")], "i"),
            ],
            "p",
        )
        expected_html = "<p><i><b>bold text</b></i></p>"
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
