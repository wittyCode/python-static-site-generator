from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            split_until_delimiter = old_node.text.split(delimiter, 1)
            first_part = TextNode(split_until_delimiter[0], TextType.TEXT)
            split_until_delimiter = split_until_delimiter[1].split(delimiter)
            if len(split_until_delimiter) != 2:
                raise Exception(f"no closing delimiter found for opening delimiter '{delimiter}' in text {old_node.text}")
            content = TextNode(split_until_delimiter[0], text_type)
            last_part = TextNode(split_until_delimiter[1], TextType.TEXT)
            new_nodes.extend([first_part, content, last_part])
    return new_nodes

