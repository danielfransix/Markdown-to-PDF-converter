# Markdown to PDF converter
# Markdown to PDF Converter - User Guide

**Created by Daniel Fransix (@danielfransix)**

A professional-grade tool for converting markdown documents to beautifully formatted PDFs with customizable themes and styling options.

## 🚀 System Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone or download the converter tool**
   ```bash
   # Navigate to your desired directory
   cd "path/to/your/directory"
   
   # If using git
   git clone <repository-url>
   cd md-to-pdf-converter
   ```

2. **Install Python dependencies**
   ```bash
   # Install all required packages
   pip install -r requirements.txt
   ```

3. **Install system dependencies (WeasyPrint requirement)**
   
   **For Windows:**
   ```bash
   # Install GTK3 runtime (required for WeasyPrint)
   # Download from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer
   # Run the installer and follow the setup wizard
   ```
   
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

4. **Verify installation**
   ```bash
   python main.py --help
   ```

## 📖 Available Commands

### 1. Single File Conversion

Convert a single markdown file to PDF:

```bash
python main.py convert input.md
```

**With custom output location:**
```bash
python main.py convert input.md -o output.pdf
```

**With custom theme:**
```bash
python main.py convert input.md -t modern
```

**With custom CSS:**
```bash
python main.py convert input.md -c custom.css
```

**Generate HTML preview instead:**
```bash
python main.py convert input.md --preview
```

### 2. Batch Conversion

Convert all markdown files in a directory:

```bash
python main.py batch directory/
```

**With custom output directory:**
```bash
python main.py batch directory/ -o output_directory/
```

**Recursive processing (include subdirectories):**
```bash
python main.py batch directory/ --recursive
```

**With custom theme:**
```bash
python main.py batch directory/ -t academic
```

### 3. Utility Commands

**List available themes:**
```bash
python main.py themes
```

**List available markdown extras:**
```bash
python main.py extras
```

**Get help:**
```bash
python main.py --help
python main.py convert --help
python main.py batch --help
```

## 🎨 Command Options Reference

### Convert Command Options
- `-o, --output`: Output PDF file path (optional)
- `-t, --theme`: Theme name (optional, defaults to 'default')
- `-c, --css`: Path to custom CSS file (optional)
- `--custom-css`: Custom CSS as string (optional)
- `-v, --verbose`: Enable verbose output
- `--preview`: Generate HTML preview instead of PDF

### Batch Command Options
- `-o, --output-dir`: Output directory for PDFs (optional)
- `-t, --theme`: Theme name (optional)
- `-c, --css`: Path to custom CSS file (optional)
- `--custom-css`: Custom CSS as string (optional)
- `-v, --verbose`: Enable verbose output
- `--recursive`: Process subdirectories recursively

## 💡 Common Usage Examples

### Example 1: Convert to same folder
```bash
# Convert single file to same folder
python main.py convert "g:\My Drive\Projects\Proply\docs\report.md"

# Convert all markdown files in a folder to same folder
python main.py batch "g:\My Drive\Projects\Proply\docs\markdowns"
```

### Example 2: Convert to different folder
```bash
# Convert single file to specific folder
python main.py convert "input.md" -o "g:\output\folder\report.pdf"

# Convert all markdown files to specific folder
python main.py batch "g:\input\folder" -o "g:\output\folder"
```

### Example 3: Themed conversion
```bash
# Convert with academic theme
python main.py convert "thesis.md" -t academic -o "thesis.pdf"

# Batch convert with modern theme
python main.py batch "docs/" -t modern -o "pdfs/"
```

### Example 4: Custom styling
```bash
# Convert with custom CSS file
python main.py convert "document.md" -c "styles/custom.css" -o "styled.pdf"

# Convert with inline CSS
python main.py convert "document.md" --custom-css "body { font-family: Arial; }"
```

## 🔧 Troubleshooting

### Common Issues

1. **"GTK3 runtime not found" error**
   - Solution: Install GTK3 runtime for Windows (see installation steps)

2. **"Permission denied" errors**
   - Solution: Run terminal as administrator or check file permissions

3. **"Module not found" errors**
   - Solution: Ensure all dependencies are installed with `pip install -r requirements.txt`

4. **PDF generation fails**
   - Solution: Check that input markdown files are valid and not corrupted

5. **Styling issues**
   - Solution: Use verbose mode (`-v`) to see detailed error messages

### Getting Help
- Use `--help` flag for command-specific help
- Check the verbose output with `-v` flag for detailed error information
- Ensure all system dependencies are properly installed

## 📋 Requirements File

The `requirements.txt` includes all necessary dependencies:
- `markdown2>=2.4.0` - Markdown parsing
- `weasyprint>=52.5` - PDF generation engine
- `Pillow>=8.0.0` - Image processing
- `click>=8.0.0` - Command-line interface
- `colorama>=0.4.4` - Cross-platform colored terminal output

## 🎯 Quick Start Checklist

- [ ] Python 3.7+ installed
- [ ] All pip dependencies installed
- [ ] System dependencies installed (GTK3, cairo, pango)
- [ ] Test with `python main.py --help`
- [ ] Try converting a sample file
- [ ] Explore available themes with `python main.py themes`

---

**Need more help?** Check the built-in help system or refer to the examples in the `examples/` directory.
