import unittest
from textnode import TextNode, TextType
from node_splitter import split_nodes_delimiter

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

    def test_multipl_bold_splitter(self):
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

if __name__ == "__main__":
    unittest.main()
