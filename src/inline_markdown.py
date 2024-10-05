import re

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

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extracted_links = extract_markdown_links(old_node.text)
        if len(extracted_links) == 0:
            return old_nodes
        old_node_text = old_node.text
        for extracted_link in extracted_links:
            link = f"[{extracted_link[0]}]({extracted_link[1]})"
            sections = old_node_text.split(link, 1)
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(extracted_link[0], text_type_link, extracted_link[1]))

            if len(extract_markdown_links(sections[1])) == 0 and sections[1] != "":
                new_nodes.append(TextNode(sections[1], text_type_text))

            # remove the first link from the string if there is any
            old_node_text = old_node_text[len(sections[0]) + len(link):]
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        extracted_links = extract_markdown_images(old_node.text)
        if len(extracted_links) == 0:
            return old_nodes
        old_node_text = old_node.text
        for extracted_link in extracted_links:
            image = f"![{extracted_link[0]}]({extracted_link[1]})"
            sections = old_node_text.split(image, 1)
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(extracted_link[0], text_type_image, extracted_link[1]))
            
            if len(extract_markdown_images(sections[1])) == 0 and sections[1] != "":
                new_nodes.append(TextNode(sections[1], text_type_text))

            # remove the first image from the string if there is any
            old_node_text = old_node_text[len(sections[0]) + len(image):]
    return new_nodes
