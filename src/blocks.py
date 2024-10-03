
def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split('\n\n')
    for line in lines:
        new_line = line.strip();
        if new_line != '':
            blocks.append(new_line)
    return blocks
