# Markdown to PDF Converter

A professional, well-organized Python application for converting Markdown documents to beautifully formatted PDF files with customizable themes and styling.

## Features

- ✅ **Multiple Themes**: Choose from default, minimal, academic, and modern themes
- ✅ **Custom Styling**: Add your own CSS for complete customization
- ✅ **Rich Markdown Support**: Tables, code blocks, task lists, footnotes, and more
- ✅ **Batch Processing**: Convert multiple files or entire directories
- ✅ **HTML Preview**: Generate HTML previews before PDF conversion
- ✅ **Command Line Interface**: Easy-to-use CLI with comprehensive options
- ✅ **Professional Output**: High-quality PDFs with proper page breaks and formatting
- ✅ **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Packages

- `markdown2`: Markdown to HTML conversion
- `weasyprint`: HTML to PDF conversion
- `Pillow`: Image processing support
- `click`: Command-line interface framework
- `colorama`: Cross-platform colored terminal output

## Quick Start

### Basic Usage

```bash
# Convert a single markdown file
python main.py convert document.md

# Convert with custom output path
python main.py convert document.md -o output.pdf

# Convert with a specific theme
python main.py convert document.md -t academic

# Convert with custom CSS
python main.py convert document.md -c custom-style.css
```

### Programmatic Usage

```python
from core.converter import MarkdownToPDFConverter

# Initialize converter
converter = MarkdownToPDFConverter()

# Convert a file
output_path = converter.convert_file(
    markdown_file_path="document.md",
    output_pdf_path="output.pdf",
    theme="modern"
)

# Convert markdown string
markdown_content = "# Hello World\n\nThis is **bold** text."
converter.convert_string(
    markdown_content=markdown_content,
    output_pdf_path="string_output.pdf",
    title="My Document"
)
```

## Command Line Interface

### Available Commands

#### `convert` - Convert a markdown file to PDF

```bash
python main.py convert [OPTIONS] INPUT_FILE

Options:
  -o, --output PATH     Output PDF file path
  -t, --theme TEXT      Theme to use for styling (default: default)
  -c, --css PATH        Custom CSS file
  --custom-css TEXT     Custom CSS as string
  -v, --verbose         Enable verbose output
  --preview             Generate HTML preview instead of PDF
```

#### `batch` - Convert multiple markdown files

```bash
python main.py batch [OPTIONS] DIRECTORY

Options:
  -o, --output-dir PATH  Output directory for PDFs
  -t, --theme TEXT       Theme to use for styling
  -c, --css PATH         Custom CSS file
  --custom-css TEXT      Custom CSS as string
  -v, --verbose          Enable verbose output
  --recursive            Process subdirectories recursively
```

#### `themes` - List available themes

```bash
python main.py themes
```

#### `extras` - List available markdown extras

```bash
python main.py extras
```

#### `preview` - Generate HTML preview

```bash
python main.py preview [OPTIONS] MARKDOWN_FILE

Options:
  -t, --theme TEXT  Theme to use for preview
```

## Available Themes

### Default Theme
Professional styling with blue accents, perfect for business documents and reports.

### Minimal Theme
Clean, simple styling with minimal colors and decorations.

### Academic Theme
Traditional academic paper styling with serif fonts and formal formatting.

### Modern Theme
Contemporary design with gradients and modern typography.

## Supported Markdown Features

- **Headers** (H1-H6) with automatic IDs
- **Text formatting** (bold, italic, strikethrough)
- **Code blocks** with syntax highlighting
- **Inline code** with distinctive styling
- **Tables** with alternating row colors
- **Lists** (ordered, unordered, nested)
- **Task lists** with checkboxes
- **Links** with hover effects
- **Images** with responsive sizing
- **Blockquotes** with left border styling
- **Horizontal rules**
- **Footnotes**
- **Table of contents** generation
- **Metadata** support

## Custom Styling

### Using Custom CSS Files

```bash
python main.py convert document.md -c my-styles.css
```

### Using Inline CSS

```bash
python main.py convert document.md --custom-css "h1 { color: red; }"
```

### CSS Structure

The converter uses CSS for styling. You can override any default styles:

```css
/* Page settings */
@page {
    size: A4;
    margin: 2cm;
}

/* Typography */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Headers */
h1 {
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
}

/* Code blocks */
pre {
    background-color: #f8f9fa;
    padding: 1em;
    border-radius: 5px;
}
```

## Examples

### Convert Single File

```bash
# Basic conversion
python main.py convert README.md

# With custom output and theme
python main.py convert README.md -o documentation.pdf -t academic

# With verbose output
python main.py convert README.md -v
```

### Batch Convert Directory

```bash
# Convert all markdown files in current directory
python main.py batch .

# Convert recursively with custom output directory
python main.py batch ./docs -o ./pdfs --recursive

# Convert with modern theme
python main.py batch ./docs -t modern
```

### Generate Preview

```bash
# Generate HTML preview
python main.py preview document.md

# Preview with specific theme
python main.py preview document.md -t minimal
```

## Project Structure

```
md-to-pdf-converter/
├── core/
│   ├── __init__.py
│   ├── converter.py      # Main converter class
│   ├── html_processor.py # Markdown to HTML processing
│   ├── styling.py        # CSS and theme management
│   └── exceptions.py     # Custom exceptions
├── cli/
│   ├── __init__.py
│   └── main.py          # Command-line interface
├── main.py              # Entry point
├── requirements.txt     # Dependencies
└── README.md           # This file
```

## Architecture

The application follows a clean, modular architecture:

- **Core Module**: Contains the main conversion logic
  - `converter.py`: Orchestrates the conversion process
  - `html_processor.py`: Handles markdown to HTML conversion
  - `styling.py`: Manages CSS themes and custom styling
  - `exceptions.py`: Custom exception classes

- **CLI Module**: Provides command-line interface
  - `main.py`: Click-based CLI with comprehensive commands

- **No Circular Dependencies**: Clean separation of concerns
- **Error Handling**: Comprehensive exception handling
- **Extensible**: Easy to add new themes and features

## Error Handling

The application provides detailed error messages for common issues:

- **File not found**: Clear indication of missing files
- **Invalid markdown**: Helpful messages for syntax issues
- **CSS errors**: Specific styling-related error information
- **Conversion failures**: Detailed error reporting with original exceptions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Troubleshooting

### Common Issues

1. **WeasyPrint installation issues on Windows**:
   - Install Visual C++ Build Tools
   - Use `pip install --upgrade pip` before installing dependencies

2. **Font rendering issues**:
   - Ensure system fonts are accessible
   - Consider using web-safe fonts in custom CSS

3. **Large file processing**:
   - For very large markdown files, consider splitting them
   - Increase system memory if needed

### Getting Help

- Check the verbose output with `-v` flag
- Review error messages for specific guidance
- Ensure all dependencies are properly installed
- Verify input file encoding (should be UTF-8)

## Version History

- **v1.0.0**: Initial release with core functionality
  - Basic markdown to PDF conversion
  - Multiple themes support
  - Custom CSS support
  - Command-line interface
  - Batch processing
  - HTML preview generation