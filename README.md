# Markdown to PDF Converter

A professional-grade Python application for converting Markdown documents to beautifully formatted PDF files with customizable themes and styling options.

## Features

- ✅ **Multiple Themes**: Choose from default, minimal, academic, and modern themes
- ✅ **Custom Styling**: Add your own CSS for complete customization
- ✅ **Rich Markdown Support**: Tables, code blocks, task lists, footnotes, and more
- ✅ **Batch Processing**: Convert multiple files or entire directories
- ✅ **HTML Preview**: Generate HTML previews before PDF conversion
- ✅ **Command Line Interface**: Easy-to-use CLI with comprehensive options
- ✅ **Professional Output**: High-quality PDFs with proper page breaks and formatting
- ✅ **Cross-Platform**: Works on Windows, macOS, and Linux

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### System Dependencies (Required for WeasyPrint)

**For Windows (WeasyPrint 66.0):**
- Install MSYS2: https://www.msys2.org/
- In the "MSYS2 MINGW64" shell, install Pango:
  ```bash
  pacman -S --noconfirm --needed mingw-w64-x86_64-pango
  ```
- Make Pango’s DLLs discoverable to Python (PowerShell):
  ```powershell
  setx WEASYPRINT_DLL_DIRECTORIES "C:\\msys64\\mingw64\\bin"
  # For the current shell only:
  $env:WEASYPRINT_DLL_DIRECTORIES = "C:\\msys64\\mingw64\\bin"
  ```
- Ensure architecture matches (64‑bit Python → x86_64 package).

**For macOS:**
```bash
# Using Homebrew
brew install cairo pango gdk-pixbuf libffi
```

**For Linux (Ubuntu/Debian):**
```bash
sudo apt-get install build-essential python3-dev python3-pip
sudo apt-get install libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

### Install Python Dependencies

```bash
# From project root
pip install -r md-to-pdf-converter/requirements.txt
```

### Required Packages

- `markdown2==2.5.4`: Markdown parsing
- `weasyprint==66.0`: PDF generation engine
- `Pillow>=12.0.0`: Image processing
- `click==8.1.7`: Command-line interface
- `colorama==0.4.6`: Cross-platform colored terminal output

### Verify Installation

```bash
# From project root
cd md-to-pdf-converter
python main.py --help
```

## 📖 Quick Start Guide

### Basic Usage

```bash
# From project root
cd md-to-pdf-converter

# Convert a single markdown file
python main.py convert document.md

# Convert with custom output path
python main.py convert document.md -o output.pdf

# Convert with a specific theme
python main.py convert document.md -t academic

# Convert with custom CSS
python main.py convert document.md -c custom-style.css

# Generate HTML preview instead of PDF
python main.py convert document.md --preview
```

### Common Usage Examples

**Convert to same folder:**
```bash
# Convert single file to same folder
python main.py convert "g:\My Drive\Projects\Proply\docs\report.md"

# Convert all markdown files in a folder to same folder
python main.py batch "g:\My Drive\Projects\Proply\docs\markdowns"
```

**Convert to different folder:**
```bash
# Convert single file to specific folder
python main.py convert "input.md" -o "g:\output\folder\report.pdf"

# Convert all markdown files to specific folder
python main.py batch "g:\input\folder" -o "g:\output\folder"
```

**Themed conversion:**
```bash
# Convert with academic theme
python main.py convert "thesis.md" -t academic -o "thesis.pdf"

# Batch convert with modern theme
python main.py batch "docs/" -t modern -o "pdfs/"
```

**Custom styling:**
```bash
# Convert with custom CSS file
python main.py convert "document.md" -c "styles/custom.css" -o "styled.pdf"

# Convert with inline CSS
python main.py convert "document.md" --custom-css "body { font-family: Arial; }"
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

## 🎨 Command Line Interface Reference

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

#### `help` - Get help for commands

```bash
python main.py --help
python main.py convert --help
python main.py batch --help
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

## 📋 Examples

### Example Files

The `examples/` directory contains various Markdown examples to demonstrate the converter's capabilities:

#### Basic Examples
- `basic.md` - Simple document with basic formatting
- `formatting.md` - Text formatting examples (bold, italic, strikethrough, etc.)
- `lists.md` - Different types of lists (ordered, unordered, nested)
- `links_images.md` - Links and image examples

#### Advanced Examples
- `tables.md` - Table formatting examples
- `code.md` - Code blocks and syntax highlighting
- `math.md` - Mathematical equations and formulas
- `academic.md` - Academic paper style document
- `technical.md` - Technical documentation example

#### Special Features
- `footnotes.md` - Footnotes and references
- `toc.md` - Table of contents example
- `custom_styling.md` - Custom CSS styling examples

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

### Test Different Themes

```bash
# Try different themes with the same document
python main.py convert formatting.md --theme default --output formatting_default.pdf
python main.py convert formatting.md --theme minimal --output formatting_minimal.pdf
python main.py convert formatting.md --theme modern --output formatting_modern.pdf
python main.py convert formatting.md --theme academic --output formatting_academic.pdf
```

### Convert All Examples

```bash
# Convert all markdown files in examples directory
python main.py batch examples/*.md --output-dir output/
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

## 🔧 Troubleshooting

### Common Issues

1. **"Pango/GLib runtime not found" error (Windows)**
   - Solution: Install MSYS2 and `mingw-w64-x86_64-pango`, then set `WEASYPRINT_DLL_DIRECTORIES` to `C:\msys64\mingw64\bin`.

2. **"Permission denied" errors**
   - Solution: Run terminal as administrator or check file permissions

3. **"Module not found" errors**
   - Solution: Ensure all dependencies are installed with `pip install -r requirements.txt`

4. **PDF generation fails**
   - Solution: Check that input markdown files are valid and not corrupted

5. **Styling issues**
   - Solution: Use verbose mode (`-v`) to see detailed error messages

6. **WeasyPrint installation issues on Windows**:
   - Ensure MSYS2 + Pango are installed and environment is configured (`WEASYPRINT_DLL_DIRECTORIES`).
   - Optionally install the Microsoft Visual C++ Redistributable if DLL errors mention `vcruntime`.
   - Upgrade pip: `pip install --upgrade pip`.

7. **Font rendering issues**:
   - Ensure fonts referenced in CSS are installed or bundled via `@font-face`.
   - For variable fonts, prefer pre‑instantiated static fonts to avoid deprecation warnings.

8. **Deprecation warning about `instantiateVariableFont`**:
   - Cause: FontTools deprecated older instancing API; WeasyPrint surfaces a `UserWarning`.
   - Impact: Conversion continues (safe to ignore). To silence: set `PYTHONWARNINGS=ignore::UserWarning` or filter in Python.

8. **Large file processing**:
   - For very large markdown files, consider splitting them
   - Increase system memory if needed

### Images and File Paths

1. **Images not displaying**
   - Place images in the same directory or use relative paths
   - Ensure image files exist and are accessible

2. **Math equations not rendering**
   - For math equations, ensure proper LaTeX syntax

3. **Custom fonts not working**
   - For custom fonts, make sure they are installed on your system

### Getting Help

- Check the verbose output with `-v` flag
- Review error messages for specific guidance
- Ensure all dependencies are properly installed
- Verify input file encoding (should be UTF-8)
- Use `--help` flag for command-specific help

## ✅ Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] All pip dependencies installed (`pip install -r md-to-pdf-converter/requirements.txt`)
- [ ] System dependencies installed (Windows: MSYS2 + Pango; macOS/Linux: cairo, pango, gdk-pixbuf)
- [ ] Test with `cd md-to-pdf-converter && python main.py --help`
- [ ] Try converting a sample file
- [ ] Explore available themes with `python main.py themes`

## Version History

- **v1.0.0**: Initial release with core functionality
  - Basic markdown to PDF conversion
  - Multiple themes support
  - Custom CSS support
  - Command-line interface
  - Batch processing
  - HTML preview generation

---

**Need more help?** Check the built-in help system (`--help` flag) or explore the examples in the `examples/` directory.
