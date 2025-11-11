#!/usr/bin/env python3
"""Test script for the markdown to PDF converter."""

import os
import sys
from pathlib import Path

# Add the current directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from core.converter import MarkdownToPDFConverter
from core.exceptions import ConverterError


def test_basic_conversion():
    """Test basic markdown to PDF conversion."""
    print("Testing basic conversion...")
    
    converter = MarkdownToPDFConverter()
    
    # Test markdown content
    test_markdown = """
# Test Document

This is a **test** document with *italic* text.

## Features

- Lists work
- Code blocks work:

```python
print("Hello, world!")
```

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |

> This is a blockquote.

That's all!
    """
    
    try:
        output_path = converter.convert_string(
            markdown_content=test_markdown,
            output_pdf_path="test_output.pdf",
            title="Test Document"
        )
        
        if os.path.exists(output_path):
            print(f"✅ Basic conversion successful: {output_path}")
            file_size = os.path.getsize(output_path)
            print(f"   File size: {file_size:,} bytes")
            return True
        else:
            print("❌ Basic conversion failed: Output file not created")
            return False
            
    except Exception as e:
        print(f"❌ Basic conversion failed: {e}")
        return False


def test_themes():
    """Test different themes."""
    print("\nTesting themes...")
    
    converter = MarkdownToPDFConverter()
    themes = converter.get_available_themes()
    
    print(f"Available themes: {list(themes.keys())}")
    
    test_markdown = "# Theme Test\n\nThis tests the **theme** styling."
    
    success_count = 0
    for theme_name in themes.keys():
        try:
            output_path = f"test_theme_{theme_name}.pdf"
            converter.convert_string(
                markdown_content=test_markdown,
                output_pdf_path=output_path,
                title=f"Theme Test - {theme_name}",
                theme=theme_name
            )
            
            if os.path.exists(output_path):
                print(f"✅ Theme '{theme_name}' works")
                success_count += 1
            else:
                print(f"❌ Theme '{theme_name}' failed: No output file")
                
        except Exception as e:
            print(f"❌ Theme '{theme_name}' failed: {e}")
    
    return success_count == len(themes)


def test_file_conversion():
    """Test file-based conversion using the sample file."""
    print("\nTesting file conversion...")
    
    sample_file = "sample.md"
    if not os.path.exists(sample_file):
        print(f"❌ Sample file not found: {sample_file}")
        return False
    
    converter = MarkdownToPDFConverter()
    
    try:
        output_path = converter.convert_file(
            markdown_file_path=sample_file,
            output_pdf_path="sample_output.pdf",
            theme="default"
        )
        
        if os.path.exists(output_path):
            print(f"✅ File conversion successful: {output_path}")
            file_size = os.path.getsize(output_path)
            print(f"   File size: {file_size:,} bytes")
            return True
        else:
            print("❌ File conversion failed: Output file not created")
            return False
            
    except Exception as e:
        print(f"❌ File conversion failed: {e}")
        return False


def test_html_preview():
    """Test HTML preview generation."""
    print("\nTesting HTML preview...")
    
    converter = MarkdownToPDFConverter()
    
    test_markdown = """
# Preview Test

This is a **preview** test with *formatting*.

## Code Example

```python
print("Hello from preview!")
```
    """
    
    try:
        html_content = converter.preview_html(test_markdown, theme="modern")
        
        # Save HTML preview
        with open("test_preview.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        if os.path.exists("test_preview.html"):
            print("✅ HTML preview generation successful: test_preview.html")
            return True
        else:
            print("❌ HTML preview failed: Output file not created")
            return False
            
    except Exception as e:
        print(f"❌ HTML preview failed: {e}")
        return False


def test_custom_css():
    """Test custom CSS functionality."""
    print("\nTesting custom CSS...")
    
    converter = MarkdownToPDFConverter()
    
    custom_css = """
    h1 {
        color: red;
        text-align: center;
    }
    
    body {
        background-color: #f0f0f0;
    }
    """
    
    test_markdown = "# Custom CSS Test\n\nThis should have **red centered** heading."
    
    try:
        output_path = converter.convert_string(
            markdown_content=test_markdown,
            output_pdf_path="test_custom_css.pdf",
            title="Custom CSS Test",
            custom_css=custom_css
        )
        
        if os.path.exists(output_path):
            print(f"✅ Custom CSS test successful: {output_path}")
            return True
        else:
            print("❌ Custom CSS test failed: Output file not created")
            return False
            
    except Exception as e:
        print(f"❌ Custom CSS test failed: {e}")
        return False


def cleanup_test_files():
    """Clean up test output files."""
    test_files = [
        "test_output.pdf",
        "test_preview.html",
        "test_custom_css.pdf",
        "sample_output.pdf"
    ]
    
    # Add theme test files
    converter = MarkdownToPDFConverter()
    themes = converter.get_available_themes()
    for theme_name in themes.keys():
        test_files.append(f"test_theme_{theme_name}.pdf")
    
    print("\nCleaning up test files...")
    for file_path in test_files:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"   Removed: {file_path}")
            except Exception as e:
                print(f"   Failed to remove {file_path}: {e}")


def main():
    """Run all tests."""
    print("Markdown to PDF Converter - Test Suite")
    print("=" * 40)
    
    tests = [
        ("Basic Conversion", test_basic_conversion),
        ("Themes", test_themes),
        ("File Conversion", test_file_conversion),
        ("HTML Preview", test_html_preview),
        ("Custom CSS", test_custom_css),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        if test_func():
            passed += 1
    
    print(f"\n{'='*40}")
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The converter is working correctly.")
    else:
        print(f"⚠️  {total - passed} test(s) failed. Please check the errors above.")
    
    # Ask user if they want to clean up test files
    try:
        response = input("\nClean up test files? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            cleanup_test_files()
    except KeyboardInterrupt:
        print("\nTest completed.")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)