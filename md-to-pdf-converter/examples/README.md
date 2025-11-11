# Examples

This directory contains various Markdown examples to demonstrate the capabilities of the Markdown to PDF converter.

## Available Examples

### Basic Examples
- `basic.md` - Simple document with basic formatting
- `formatting.md` - Text formatting examples (bold, italic, strikethrough, etc.)
- `lists.md` - Different types of lists (ordered, unordered, nested)
- `links_images.md` - Links and image examples

### Advanced Examples
- `tables.md` - Table formatting examples
- `code.md` - Code blocks and syntax highlighting
- `math.md` - Mathematical equations and formulas
- `academic.md` - Academic paper style document
- `technical.md` - Technical documentation example

### Special Features
- `footnotes.md` - Footnotes and references
- `toc.md` - Table of contents example
- `custom_styling.md` - Custom CSS styling examples

## How to Use

### Convert Single File
```bash
# Convert with default theme
python ../main.py convert basic.md

# Convert with specific theme
python ../main.py convert academic.md --theme academic

# Convert with custom output name
python ../main.py convert technical.md --output technical_doc.pdf
```

### Convert All Examples
```bash
# Convert all markdown files in this directory
python ../main.py batch *.md --output-dir output/
```

### Test Different Themes
```bash
# Try different themes with the same document
python ../main.py convert formatting.md --theme default --output formatting_default.pdf
python ../main.py convert formatting.md --theme minimal --output formatting_minimal.pdf
python ../main.py convert formatting.md --theme modern --output formatting_modern.pdf
python ../main.py convert formatting.md --theme academic --output formatting_academic.pdf
```

## Output

By default, PDF files will be created in the same directory as the source Markdown files. Use the `--output-dir` option to specify a different output directory.

## Tips

1. **Images**: Place images in the same directory or use relative paths
2. **Themes**: Different themes work better for different document types
3. **Custom CSS**: You can add custom CSS files for advanced styling
4. **File Size**: Complex documents with many images may take longer to process

## Troubleshooting

If you encounter issues:

1. Make sure all dependencies are installed: `pip install -r ../requirements.txt`
2. Check that image files exist and are accessible
3. For math equations, ensure proper LaTeX syntax
4. For custom fonts, make sure they are installed on your system