from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__()
        self.value = value
        self.tag = tag
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        
        propstr = ""
        if self.props != None:
            for k, v in self.props.items():
                propstr += f"{k}=\"{v}\" "
            propstr = propstr.strip(' ')

        return f"<{self.tag} {propstr}>{self.value}</{self.tag}>"

