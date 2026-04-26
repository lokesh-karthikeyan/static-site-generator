def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    blocks = markdown.split("\n\n")
    return list(filter(lambda str: str.strip() != '', map(str.strip, blocks)))
