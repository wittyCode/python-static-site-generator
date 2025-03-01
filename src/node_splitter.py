from textnode import TextNode, TextType
from textextractor import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    return split_nodes_of_type(old_nodes, extract_markdown_images, TextType.IMAGE)

def split_nodes_link(old_nodes):
    return split_nodes_of_type(old_nodes, extract_markdown_links, TextType.LINK)

def split_nodes_of_type(old_nodes, split_function, node_type):
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        if original_text == "":
            continue
        link_tuples = split_function(original_text)
        if len(link_tuples) == 0:
            new_nodes.append(old_node)
        else:
            working_text = original_text
            for link_tuple in link_tuples:
                link_text = link_tuple[0]
                link_url = link_tuple[1]
                sections = []
                if node_type == TextType.LINK:
                    sections = working_text.split(f"[{link_text}]({link_url})", 1)
                elif node_type == TextType.IMAGE:
                    sections = working_text.split(f"![{link_text}]({link_url})", 1)
                else: 
                    raise Exception(f"unsupported TextType: {node_type}")

                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, node_type, link_url))
                if len(sections[1]) > 0:
                    working_text = sections[1]
                else:
                    working_text = ""
            if len(working_text) > 0:
                new_nodes.append(TextNode(working_text, TextType.TEXT))
    return new_nodes

