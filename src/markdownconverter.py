from markdownsplitter import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode
from node_splitter import text_to_textnode
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_blocks = []
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children_blocks = text_to_children(block)
                children.append(ParentNode("p", children_blocks))
            case BlockType.QUOTE:
                list_lines = block.split("\n")
                list_elements = quote_elements_to_children(list_lines)
                children.append(ParentNode("blockquote", list_elements))
            case BlockType.HEADING:
                children_blocks = header_to_children(block)
                children.append(ParentNode("h1", children_blocks))
            case BlockType.UNORDERED_LIST:
                list_lines = block.split("\n")
                list_elements = list_elements_to_children(list_lines)
                children.append(ParentNode("ul", list_elements))
            case BlockType.ORDERED_LIST:
                list_lines = block.split("\n")
                list_elements = list_elements_to_children(list_lines)
                children.append(ParentNode("ol", list_elements))
            case BlockType.CODE:
                content = TextNode(block.strip("```"), TextType.TEXT)
                html_node = text_node_to_html_node(content)
                code_node = ParentNode("code", [html_node])
                children.append(ParentNode("pre", [code_node]))
            case _:
                pass
    parent = ParentNode("div", children)
    return parent

def header_to_children(block):
    content = block.lstrip("# ")
    return text_to_children(content)

def quote_elements_to_children(lines):
    children = []
    for index in range(len(lines)):
        line = lines[index]
        text_in_line = line[1: ]
        if index == 0:
            text_in_line = text_in_line.lstrip(" ")
        children.extend(text_to_children(text_in_line))
    return children

def list_elements_to_children(lines):
    children = []
    for line in lines:
        text_in_line = line[2:].lstrip(" ")
        children.append(ParentNode("li", text_to_children(text_in_line)))
    return children

def text_to_children(text):
    children = []
    text_nodes = text_to_textnode(text)
    leaf_nodes = list(map(text_node_to_html_node, text_nodes))
    children.extend(leaf_nodes)
    return children

