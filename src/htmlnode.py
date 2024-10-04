
# represents a node in an html document tree: <p>, <a>, etc
# its purpose is to render itself as HTML
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implement")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"

# a type of HTMLNode that represents a single HTML tag with no children 
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node value can't be none")
        if self.tag is None:
            return self.value
        props_html = self.props_to_html()
        return f'<{self.tag}{props_html}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, props: {self.props}"

# handles the nesting of HTML nodes inside of one another
# any htmlnode that is not a leafnode (i.e. it has childrens) is a parentnode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parentnode tag can't be none")
        if self.children is None:
            raise ValueError("parentnode childrent can't be none")

        child_htmls = ""

        for child in self.children:
            child_htmls += child.to_html()
        
        return f'<{self.tag}>{child_htmls}</{self.tag}>'
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, props: {self.props}"
