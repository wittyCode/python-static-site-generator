from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_eq(self):
        input = HTMLNode(props = {"href": "www.mylink.de", "target": "_blank"})
        expected = ' href="www.mylink.de" target="_blank"'
        
        actual = input.props_to_html()
        self.assertEqual(expected, actual)

    def test_props_to_html_empty_props(self):
        input = HTMLNode()
        expected = ''
        
        actual = input.props_to_html()
        self.assertEqual(expected, actual)

    def test_props_to_html_only_one_prop(self):
        input = HTMLNode(props = {"href": "www.mylink.de"})
        expected = ' href="www.mylink.de"'
        
        actual = input.props_to_html()
        self.assertEqual(expected, actual)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        input = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"

        actual = input.to_html()
        self.assertEqual(expected, actual)

    def test_leaf_to_html_p_with_props(self):
        input = LeafNode("p", "Hello, world!", {"href": "www.mylink.de"})
        expected = '<p href="www.mylink.de">Hello, world!</p>'

        actual = input.to_html()
        self.assertEqual(expected, actual)

    def test_leaf_to_html_div_with_props(self):
        input = LeafNode("div", "Hello, world!", {"href": "www.mylink.de"})
        expected = '<div href="www.mylink.de">Hello, world!</div>'

        actual = input.to_html()
        self.assertEqual(expected, actual)

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child", {"target": "_blank"})
        parent_node = ParentNode("div", [child_node], {"href": "www.mylink.de"})
        self.assertEqual(parent_node.to_html(), '<div href="www.mylink.de"><span target="_blank">child</span></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("div", "grandchild")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><div>grandchild</div></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
