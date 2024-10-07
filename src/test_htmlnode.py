import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, markdown_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!", None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual( node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, props: {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_parent_to_html(self):
        node = ParentNode(
             "p",
             [
                 LeafNode("b", "Bold text"),
                 LeafNode(None, "Normal text"),
                 LeafNode("i", "italic text"),
                 LeafNode(None, "Normal text"),
             ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        markdown = "hello **world**!"
        node = markdown_to_html_node(markdown)
        expected_node = ParentNode("div", [
            ParentNode("p", [
                LeafNode(None, "hello "),
                LeafNode("b", "world"),
                LeafNode(None, "!")
            ])
        ])
        self.assertEqual(node.to_html(), expected_node.to_html())

    def test_heading(self):
        markdown = "# hello world!"
        node = markdown_to_html_node(markdown)
        expected_node = ParentNode("div", [
            ParentNode("h1", [
                LeafNode(None, "hello world!"),
            ])
        ])
        self.assertEqual(node.to_html(), expected_node.to_html())
        markdown = "###### hello world!"
        node = markdown_to_html_node(markdown)
        expected_node = ParentNode("div", [
            ParentNode("h6", [
                LeafNode(None, "hello world!"),
            ])
        ])
        self.assertEqual(node.to_html(), expected_node.to_html())
    
    def test_ul(self):
        markdown = "* hello\n* **great** world\n* !"
        node = markdown_to_html_node(markdown)
        expected_node = ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "hello") ]),
                ParentNode("li", [LeafNode("b", "great"), LeafNode(None, " world") ]),
                ParentNode("li", [LeafNode(None, "!") ]),
            ])
        ])
        self.assertEqual(node.to_html(), expected_node.to_html())

    def test_ol(self):
        markdown = "1. hello\n2. **great** world\n3. !"
        node = markdown_to_html_node(markdown)
        expected_node = ParentNode("div", [
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "hello") ]),
                ParentNode("li", [LeafNode("b", "great"), LeafNode(None, " world") ]),
                ParentNode("li", [LeafNode(None, "!") ]),
            ])
        ])
        self.assertEqual(node.to_html(), expected_node.to_html())
    
    def test_code(self):
        markdown = "```hello world```"
        node = markdown_to_html_node(markdown)
        expected_node = ParentNode("div", [
            ParentNode("pre", [
                LeafNode("code", "hello world"),
            ])
        ])
        self.assertEqual(node.to_html(), expected_node.to_html())

    def test_quote(self):
        markdown = "> hello\n> *world*\n> !"
        node = markdown_to_html_node(markdown)
        expected_node = ParentNode("div", [
            ParentNode("blockquote", [
                LeafNode(None, "hello "),
                LeafNode("i", "world"),
                LeafNode(None, " !"),
            ])
        ])
        self.assertEqual(node.to_html(), expected_node.to_html())

    def test_paragraph_2(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote2(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote(self):
        return
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()
