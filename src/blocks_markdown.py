
markdown_block_type_paragraph = "paragraph"
markdown_block_type_heading = "heading"
markdown_block_type_code = "code"
markdown_block_type_quote = "quote"
markdown_block_type_unordered_list = "unordered_list"
markdown_block_type_ordered_list = "ordered_list"


# note: solution used .startswith
def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"): 
        block = block.strip()
        if block == "":
            continue
        blocks.append(block)
    return blocks


def block_to_block_type(block):
    if block[0] == "#" and block[1] == " " and (block[2] != " " and block[2] != ""):
        return markdown_block_type_heading
    if block[:2] == "##" and block[2] == " " and (block[4] != " " and block[4] != ""):
        return markdown_block_type_heading
    if block[:3] == "###" and block[3] == " " and (block[5] != " " and block[5] != ""):
        return markdown_block_type_heading
    if block[:4] == "####" and block[4] == " " and (block[6] != " " and block[6] != ""):
        return markdown_block_type_heading
    if block[:5] == "#####" and block[5] == " " and (block[7] != " " and block[7] != ""):
        return markdown_block_type_heading
    if block[:6] == "######" and block[6] == " " and (block[8] != " " and block[8] != ""):
        return markdown_block_type_heading

    if block[:3] == "```" and block[-3:] == "```":
        return markdown_block_type_code

    lines = block.split('\n')
    quote_count = 0
    ul_count = 0
    for line in lines:
        if len(line) > 0 and line[0] == ">":
            quote_count += 1
        if len(line) > 1 and (line[0] == "*" or line[0] == "-") and line[1] == " ":
            ul_count += 1
    

    if quote_count == len(lines):
        return markdown_block_type_quote
    
    if ul_count == len(lines):
        return markdown_block_type_unordered_list

    ol_count = 0
    for i in range(len(lines)):
        if len(lines[i]) > 2 and lines[i][0] == str(i + 1) and lines[i][1] == '.' and lines[i][2] == ' ':
            ol_count += 1
    
    if ol_count == len(lines):
        return markdown_block_type_ordered_list

    return markdown_block_type_paragraph
