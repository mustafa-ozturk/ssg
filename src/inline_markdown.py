from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image,
        text_node_to_html_node,
)
# we can render htmlnodes as html
# we need to be able to convert a raw markdown string into a list of textnode objects
# for simplicity we will only support a single level of nesting
# which means you cant have a word that is both italic and bold

# takes a list of nodes and returns a new list of nodes 
# where any text type nodes are potentially split into multiple nodes
# based on the syntax
# eg. given (TextNode("hello `world`", text_type_text), "`", text_type_code)
# you will get [ TextNode("hello ", text_type_text), TextNode("world", text_type_code) ]
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
