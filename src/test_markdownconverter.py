import unittest
from markdownconverter import markdown_to_html_node
from markdownsplitter import BlockType

class TestMarkdownConverter(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading(self):
        md = """
### This is **bolded** heading

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is <b>bolded</b> heading</h1><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_quote(self):
        md = """
> This is **bolded** paragraph
> text in a li
> tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph text in a li tag here</blockquote></div>"
        )

    def test_ordered_list(self):
        md = """
1. This is **bolded** paragraph
2. text in a li
3. tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is <b>bolded</b> paragraph</li><li>text in a li</li><li>tag here</li></ol></div>",
        )

    def test_unordered_list(self):
        md = """
- This is **bolded** paragraph
- text in a li
- tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>bolded</b> paragraph</li><li>text in a li</li><li>tag here</li></ul></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code> This is text that _should_ remain the **same** even with inline stuff </code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()
