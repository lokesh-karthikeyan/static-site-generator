from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType

from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from textnode_to_html import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def create_paragraph_node(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    return ParentNode("p", children)

def create_heading_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    text = block[level:].strip()
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def create_code_node(block):
    lines = block.split("\n")

    code_text = "\n".join(lines[1:-1]) + "\n"

    text_node = TextNode(code_text, TextType.TEXT)
    code_child = text_node_to_html_node(text_node)

    code_node = ParentNode("code", [code_child])
    return ParentNode("pre", [code_node])


def create_blockquote_node(block):
    lines = block.split("\n")
    stripped = [line.lstrip("> ").strip() for line in lines]
    text = " ".join(stripped)

    children = text_to_children(text)
    return ParentNode("blockquote", children)


def create_ul_node(block):
    lines = block.split("\n")
    items = []

    for line in lines:
        text = line[2:].strip()
        children = text_to_children(text)
        items.append(ParentNode("li", children))

    return ParentNode("ul", items)


def create_ol_node(block):
    lines = block.split("\n")
    items = []

    for line in lines:
        parts = line.split(".", 1)
        text = parts[1].strip()

        children = text_to_children(text)
        items.append(ParentNode("li", children))

    return ParentNode("ol", items)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return create_paragraph_node(block)

    if block_type == BlockType.HEADING:
        return create_heading_node(block)

    if block_type == BlockType.CODE:
        return create_code_node(block)

    if block_type == BlockType.QUOTE:
        return create_blockquote_node(block)

    if block_type == BlockType.UNORDERED_LIST:
        return create_ul_node(block)

    if block_type == BlockType.ORDERED_LIST:
        return create_ol_node(block)

    raise ValueError(f"Unknown block type: {block_type}")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        node = block_to_html_node(block)
        children.append(node)

    return ParentNode("div", children)
