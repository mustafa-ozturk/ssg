from leafnode import LeafNode

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type}, {self.url})"

def text_node_to_html_node(text_node) -> LeafNode:
    match (text_node.text_type):
        case ("text"):
            return LeafNode(text_node.text)
        case ("bold"):
            return LeafNode(text_node.text, "b")
        case ("italic"):
            return LeafNode(text_node.text, "i")
        case ("code"):
            return LeafNode(text_node.text, "code")
        case ("link"):
            return LeafNode(text_node.text, "a", {"href": ""})
        case ("image"):
            return LeafNode("", "img", {"src": text_node.url, "alt": text_node.text})
        case _:
           print(text_node.text_type)
           raise Exception("Invalid text type")
