import unittest
from markdownsplitter import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownSplitter(unittest.TestCase):

   def test_block_to_block_type_header(self):
        actual = block_to_block_type("# header")
        self.assertEqual(BlockType.HEADING, actual)
        actual = block_to_block_type("###### header")
        self.assertEqual(BlockType.HEADING, actual)

   def test_block_to_block_type_quote(self):
        actual = block_to_block_type("> header")
        self.assertEqual(BlockType.QUOTE, actual)
        actual = block_to_block_type(">line1\n>line2")
        self.assertEqual(BlockType.QUOTE, actual)
        actual = block_to_block_type(">line1\nline2")
        self.assertEqual(BlockType.PARAGRAPH, actual)

   def test_block_to_block_type_unordered_list(self):
        actual = block_to_block_type("- header")
        self.assertEqual(BlockType.UNORDERED_LIST, actual)
        actual = block_to_block_type("- line1\n- line2")
        self.assertEqual(BlockType.UNORDERED_LIST, actual)
        actual = block_to_block_type("- line1\nline2")
        self.assertEqual(BlockType.PARAGRAPH, actual)

   def test_block_to_block_type_ordered_list(self):
        actual = block_to_block_type("1. header")
        self.assertEqual(BlockType.ORDERED_LIST, actual)
        actual = block_to_block_type("1. line1\n2. line2")
        self.assertEqual(BlockType.ORDERED_LIST, actual)
        actual = block_to_block_type("1. line1\nline2")
        self.assertEqual(BlockType.PARAGRAPH, actual)
        actual = block_to_block_type("2. line1")
        self.assertEqual(BlockType.PARAGRAPH, actual)

   def test_block_to_block_type_code(self):
        actual = block_to_block_type("```header```")
        self.assertEqual(BlockType.CODE, actual)
        actual = block_to_block_type("```header\n after newline```")
        self.assertEqual(BlockType.CODE, actual)


   def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()
