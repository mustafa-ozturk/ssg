
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
