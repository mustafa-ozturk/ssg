from textnode import TextNode
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


