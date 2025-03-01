from textnode import TextNode, TextType, text_node_to_html_node

def main():
    dummy = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(dummy)

if __name__ == "__main__":
    main()
