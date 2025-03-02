from textnode import TextNode, TextType, text_node_to_html_node
from file_copy import copy_static_to_public, generate_pages_recursive

def main():
    copy_static_to_public()
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()
