from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag):
        super().__init__()
        self.children = children
        self.tag = tag

    def to_html(self):
        if self.tag == None:
            raise Exception("A tag is required")
        if len(self.children) == 0:
            raise Exception("Children is required")

        child_html = []
        for child in self.children:
            child_html.append(child.to_html())
        
        return f"<{self.tag}>{"".join(child_html)}</{self.tag}>"
