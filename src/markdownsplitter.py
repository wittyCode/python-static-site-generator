from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    heading_regex = r"(#{1,6}).+"
    if re.search(heading_regex, block):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    if check_lines_in_block_start_for_sequence(block, ">"):
        return BlockType.QUOTE
    if check_lines_in_block_start_for_sequence(block, "- "):
        return BlockType.UNORDERED_LIST
    if check_lines_for_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def check_lines_in_block_start_for_sequence(block, seq):
    matching = True
    for line in block.split("\n"):
        matching = matching and line.startswith(seq)
    return matching

def check_lines_for_ordered_list(block):
    is_list = True
    lines = block.split("\n")
    for i in range(len(lines)):
        is_list = is_list and lines[i].startswith(f"{i + 1}. ")
    return is_list

def _markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    no_empty_lines = list(filter(lambda x: x.strip(" ") != "", lines))
    result = []
    for line in no_empty_lines:
        inner_lines_without_new_line = line.split("\n")
        inner_lines = []
        for inner_line in inner_lines_without_new_line:
            inner_lines.append(inner_line.strip(" "))
            no_empty_inner_lines = list(filter(lambda x: x != "", inner_lines))
        if len(no_empty_inner_lines) > 1:
            result.append("\n".join(no_empty_inner_lines))
        else:
            result.append(no_empty_inner_lines[0])

    return result
