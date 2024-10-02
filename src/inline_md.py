from textnode import TextNode
from extract_markdown import extract_markdown_links, extract_markdown_images
"""
node = TextNode("This is text with a `code block` word", text_type_text)
new_nodes = split_nodes_delimiter([node], "`", text_type_code)

will return:
[
    TextNode("This is text with a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" word", text_type_text),
]
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text.find(delimiter) < 0:
            new_nodes.append(node)
            continue
        delimited_strings = node.text.split(delimiter) 
        str_to_split_start = node.text.index(delimiter) + len(delimiter)
        str_to_split_end = str_to_split_start + node.text[str_to_split_start:].index(delimiter)
        str_to_split = node.text[str_to_split_start:str_to_split_end]

        for string in delimited_strings:
            if string == str_to_split:
                new_nodes.append(TextNode(string, text_type))
            else:
                new_nodes.append(TextNode(string, "text"))

    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        sections = []
        for image in images:

            link_str = f"![{image[0]}]({image[1]})"
            split_text = node.text.split(link_str)
            node.text = split_text[1]
            old_nodes.append(TextNode(split_text[1], "text"))

            sections.append(split_text[0])
            sections.append(image)
        for section in sections:
            if isinstance(section, tuple):
                new_nodes.append(TextNode(section[0], "image", section[1]))
            elif section != '':
                new_nodes.append(TextNode(section, "text"))
    return new_nodes

"""
node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    text_type_text,
)
new_nodes = split_nodes_link([node])
[
    TextNode("This is text with a link ", text_type_text),
    TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
    TextNode(" and ", text_type_text),
    TextNode(
        "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
    ),
]
"""
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        sections = []
        for link in links:
            link_str = f"[{link[0]}]({link[1]})"
            split_text = node.text.split(link_str)
            node.text = split_text[1]
            old_nodes.append(TextNode(split_text[1], "text"))

            sections.append(split_text[0])
            sections.append(link)
        for section in sections:
            if isinstance(section, tuple):
                new_nodes.append(TextNode(section[0], "link", section[1]))
            elif section != '':
                new_nodes.append(TextNode(section, "text"))
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, "text")
    code_nodes = split_nodes_delimiter([node], "`", "code")
    bold_nodes = split_nodes_delimiter(code_nodes, "**", "bold")
    italic_nodes = split_nodes_delimiter(bold_nodes, "*", "italic")
    images_nodes = split_nodes_images(italic_nodes)
    link_nodes = split_nodes_link(images_nodes)
    return link_nodes









