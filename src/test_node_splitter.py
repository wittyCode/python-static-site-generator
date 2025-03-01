import unittest
from textnode import TextNode, TextType
from node_splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnode

class TestNodeSplitter(unittest.TestCase):

    def test_code_splitter(self):
        node = TextNode("This is text with a `code block` inside", TextType.TEXT)
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" inside", TextType.TEXT)
            ],
            actual
        )

    def test_italic_splitter(self):
        node = TextNode("This is a text with a _italic block_ inside", TextType.TEXT)
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("italic block", TextType.ITALIC),
                TextNode(" inside", TextType.TEXT)
            ],
            actual
        )

    def test_bold_splitter(self):
        node = TextNode("This is a text with a **bold block** inside", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" inside", TextType.TEXT)
            ],
            actual
        )

    def test_multiple_bold_splitter(self):
        node = TextNode("This is a text with a **bold block** inside", TextType.TEXT)
        node2 = TextNode("This is a second text with a **bold block** inside too", TextType.TEXT)
        actual = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" inside", TextType.TEXT),
                TextNode("This is a second text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" inside too", TextType.TEXT)
            ],
            actual
        )

    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
        "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_link_at_start(self):
        node = TextNode(
        "[image](https://i.imgur.com/zjjcJKZ.png) at the beginning of the text",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the beginning of the text", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_images_image_at_start(self):
        node = TextNode(
        "![image](https://i.imgur.com/zjjcJKZ.png) at the beginning of the text",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the beginning of the text", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_images_only_text(self):
        node = TextNode(
        "no image here",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("no image here", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_links_only_text(self):
        node = TextNode(
        "no link here",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("no link here", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_links_empty_text(self):
        node = TextNode(
        "",
        TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([], new_nodes,)

    def test_split_images_empty_text(self):
        node = TextNode(
        "",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([], new_nodes,)

    def test_text_to_textnode(self):
        actual = text_to_textnode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev) at the end")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" at the end", TextType.TEXT),
        ]
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
