
from htmlnode import HTMLNode
from inline_md import text_to_textnodes, split_nodes_delimiter

def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split('\n\n')
    for line in lines:
        new_line = line.strip();
        if new_line != '':
            blocks.append(new_line)
    return blocks

def block_to_block_type(block):
    lines = block.split('\n\n')
    if lines[0][0] == '#':
        count = 1
        for c in lines[0][1:]:
            if c == ' ':
                return "heading"
            elif c == '#':
                count += 1
    elif lines[0][0] == '`':
        if len(lines[0].split("```")) == 3:
            return "code"
    elif lines[0][0] == '>':
        count = 1
        for line in lines[1:]:
            if line[0] == '>':
                count += 1
            else:
                count = -1
        if count  > 0:
            return "quote"
    elif lines[0][0] == '*' and lines[0][1] == ' ':
        count = 1
        for line in lines[1:]:
            if line[0] == '*' and line[1] == ' ':
                count += 1
            else:
                count = -1
        if count > 0:
            return "unordered_list"
    elif lines[0][0] == '-' and lines[0][1] == ' ':
        count = 1
        for line in lines[1:]:
            if line[0] == '-' and line[1] == ' ':
                count += 1
            else:
                count = -1
        if count  > 0:
            return "unordered_list"
    elif lines[0][0] == '1' and lines[0][1] == '.' and lines[0][2] == ' ':
        count = 1
        for line in lines[1:]:
            if line[0] == str(count + 1) and line[1] == '.' and line[2] == ' ':
                count += 1
            else:
                count = -1
        if count  > 0:
            return "ordered_list"
    else:
        return "paragraph"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        print("block type", block_type)
        if block_type == "paragraph":
            children_of_children = text_to_textnodes(block)
            children.append(HTMLNode('p', None, children_of_children, None))
        if block_type == "heading":
            children_of_children =text_to_textnodes(block)
            children.append(HTMLNode('h1', None, children_of_children, None))

    print("children------->", children)
    return HTMLNode('div', None, children, None)
