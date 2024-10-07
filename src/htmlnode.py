from blocks_markdown import (
    markdown_to_blocks, 
    block_to_block_type,
    markdown_block_type_code,
    markdown_block_type_quote,
    markdown_block_type_heading,
    markdown_block_type_paragraph,
    markdown_block_type_ordered_list,
    markdown_block_type_unordered_list,
)

from textnode import text_node_to_html_node

from inline_markdown import text_to_textnodes

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
        return f"LeafNode({self.tag}, {self.value}, props: {self.props})"

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


# converts a full markdown document into a single HTMLNode with many children
def markdown_to_html_node(markdown):
    # split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == markdown_block_type_paragraph:
            lines = block.split('\n')
            paragraph = " ".join(lines)
            text_nodes = text_to_textnodes(paragraph)
            leaf_nodes = []
            for text_node in text_nodes:
                leaf_nodes.append(text_node_to_html_node(text_node))
            child_nodes.append(ParentNode("p", leaf_nodes))


        if block_type == markdown_block_type_heading:
            h_size = 0
            for c in block:
                if c == '#':
                    h_size += 1

            heading = block[h_size + 1:]
            text_nodes = text_to_textnodes(heading)
            leaf_nodes = []
            for text_node in text_nodes:
                leaf_nodes.append(text_node_to_html_node(text_node))
            child_nodes.append(ParentNode(f"h{h_size}", leaf_nodes))


            #                                                        + 1 to remove the space
            # child_nodes.append(ParentNode(f"h{h_size}", [LeafNode(None, block[h_size + 1:])]))

        if block_type == markdown_block_type_unordered_list:
            list_items = block.split('\n')

            li_nodes = []
            for list_item in list_items:
                # get textnodes, split into bold/italic/etc
                text_nodes = text_to_textnodes(list_item[2:])
                # turn each textnode to leafnodes

                # list item text nodes turned into leaf nodes
                leaf_nodes = []
                for text_node in text_nodes:
                    leaf_nodes.append(text_node_to_html_node(text_node))

                # turn leaf_nodes into li parentnodes
                li_nodes.append(ParentNode("li", leaf_nodes))
            # put li inside ul parent node
            child_nodes.append(ParentNode("ul", li_nodes))
        
        if block_type == markdown_block_type_ordered_list:
            list_items = block.split('\n')

            li_nodes = []
            for list_item in list_items:
                # get textnodes, split into bold/italic/etc
                # 3: to skip the "1. "
                text_nodes = text_to_textnodes(list_item[3:])
                # turn each textnode to leafnodes

                # list item text nodes turned into leaf nodes
                leaf_nodes = []
                for text_node in text_nodes:
                    leaf_nodes.append(text_node_to_html_node(text_node))

                # turn leaf_nodes into li parentnodes
                li_nodes.append(ParentNode("li", leaf_nodes))
            # put li inside ul parent node
            child_nodes.append(ParentNode("ol", li_nodes))

        if block_type == markdown_block_type_code:
            code_text = block[3:-3]
            code_text = code_text.strip()
            child_nodes.append(ParentNode("pre", [LeafNode("code", code_text)]))
        
        if block_type == markdown_block_type_quote:
            lines = block.split('\n')

            new_lines = []
            for line in lines:
                new_lines.append(line.lstrip(">").strip())
            content = " ".join(new_lines)
            text_nodes = text_to_textnodes(content)

            children = []
            for text_node in text_nodes:
                children.append(text_node_to_html_node(text_node))
            child_nodes.append(ParentNode("blockquote", children))


    return ParentNode("div", child_nodes)
