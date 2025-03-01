import re

def extract_markdown_images(text):
    found_links = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return found_links

def extract_markdown_links(text):
    found_links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return found_links
