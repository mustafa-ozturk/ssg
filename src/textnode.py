import htmlnode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

# represents inline text with above text types
class TextNode():
    # text content of the node, type of the node "bold/italic", url of an imagore or link
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
                self.text == other.text 
                and self.text_type == other.text_type 
                and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# converts a textnode to a leafnode
def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return htmlnode.LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return htmlnode.LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return htmlnode.LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return htmlnode.LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return htmlnode.LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return htmlnode.LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise Exception(f"invalid text type: {text_node.text_type}")
