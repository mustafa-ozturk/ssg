import unittest


from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        tag = "a"
        value = "test"
        children = [ HTMLNode() ]
        props = { "href": "https://www.github.com" }
        node = HTMLNode(tag, value, children, props)
        node2 = HTMLNode(tag, value, children, props)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        tag = "a"
        value = "test"
        children = [ HTMLNode() ]
        props = { "href": "https://www.github.com" }
        node = HTMLNode(tag, value, children, props)
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)
    
    def test_tag(self):
        tag = "a"
        node = HTMLNode(tag)
        self.assertEqual(node.tag, tag)
    
    def test_props_to_html(self):
        tag = "a"
        value = "test"
        children = [ HTMLNode() ]
        props = { "href": "https://www.github.com",
                 "target": "_blank"}
        node = HTMLNode(tag, value, children, props)
        valid_props_to_html = "href=\"https://www.github.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), valid_props_to_html)

if __name__ == "__main__":
    unittest.main()
