#!/usr/bin/env python3
"""Installation and testing script for the Markdown to PDF converter."""

import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible."""
    print("Checking Python version...")
    version = sys.version_info
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python {version.major}.{version.minor} is not supported.")
        print("   This package requires Python 3.7 or higher.")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible.")
    return True


def install_dependencies():
    """Install required dependencies."""
    print("\nInstalling dependencies...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print(f"❌ Requirements file not found: {requirements_file}")
        return False
    
    try:
        # Install dependencies
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
            capture_output=True,
            text=True,
            check=True
        )
        
        print("✅ Dependencies installed successfully.")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies:")
        print(f"   Error: {e}")
        if e.stdout:
            print(f"   Output: {e.stdout}")
        if e.stderr:
            print(f"   Error output: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during installation: {e}")
        return False


def check_dependencies():
    """Check if all required dependencies are available."""
    print("\nChecking dependencies...")
    
    required_packages = [
        "markdown2",
        "weasyprint",
        "click",
        "colorama",
        "PIL"  # Pillow
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == "PIL":
                import PIL
            else:
                __import__(package)
            print(f"✅ {package} is available")
        except ImportError:
            print(f"❌ {package} is missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        return False
    
    print("\n✅ All dependencies are available.")
    return True


def test_weasyprint():
    """Test WeasyPrint specifically as it can have platform-specific issues."""
    print("\nTesting WeasyPrint...")
    
    try:
        from weasyprint import HTML, CSS
        
        # Create a simple test HTML
        test_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test</title>
        </head>
        <body>
            <h1>WeasyPrint Test</h1>
            <p>This is a test document.</p>
        </body>
        </html>
        """
        
        # Try to create a PDF
        html_doc = HTML(string=test_html)
        pdf_bytes = html_doc.write_pdf()
        
        if pdf_bytes:
            print("✅ WeasyPrint is working correctly.")
            return True
        else:
            print("❌ WeasyPrint failed to generate PDF.")
            return False
            
    except Exception as e:
        print(f"❌ WeasyPrint test failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("   - On Windows, you might need to install GTK+ libraries")
        print("   - Try: pip install --upgrade weasyprint")
        print("   - Check WeasyPrint documentation for platform-specific requirements")
        return False


def run_converter_tests():
    """Run the converter test suite."""
    print("\nRunning converter tests...")
    
    test_script = Path(__file__).parent / "test_converter.py"
    
    if not test_script.exists():
        print(f"❌ Test script not found: {test_script}")
        return False
    
    try:
        result = subprocess.run(
            [sys.executable, str(test_script)],
            cwd=str(Path(__file__).parent),
            input="n\n",  # Don't clean up files automatically
            text=True,
            capture_output=True
        )
        
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("✅ All converter tests passed!")
            return True
        else:
            print(f"❌ Some converter tests failed (exit code: {result.returncode})")
            return False
            
    except Exception as e:
        print(f"❌ Failed to run converter tests: {e}")
        return False


def show_usage_examples():
    """Show usage examples."""
    print("\n" + "="*50)
    print("USAGE EXAMPLES")
    print("="*50)
    
    print("\n1. Command Line Interface:")
    print("   python main.py convert sample.md")
    print("   python main.py convert sample.md --output my_document.pdf")
    print("   python main.py convert sample.md --theme modern")
    print("   python main.py batch *.md --output-dir output/")
    
    print("\n2. Python API:")
    print("""
   from core.converter import MarkdownToPDFConverter
   
   converter = MarkdownToPDFConverter()
   
   # Convert file
   converter.convert_file('document.md', 'output.pdf')
   
   # Convert string
   markdown_text = "# Hello\\nThis is **bold** text."
   converter.convert_string(markdown_text, 'output.pdf')
   
   # Use custom theme
   converter.convert_file('doc.md', 'out.pdf', theme='academic')
   """)
    
    print("\n3. Available Commands:")
    print("   python main.py --help")
    print("   python main.py themes")
    print("   python main.py extras")
    
    print("\n4. Available Themes:")
    print("   - default: Clean and professional")
    print("   - minimal: Simple and clean")
    print("   - academic: Suitable for academic papers")
    print("   - modern: Contemporary design")


def main():
    """Main installation and testing routine."""
    print("Markdown to PDF Converter - Installation & Test")
    print("=" * 50)
    
    # Step 1: Check Python version
    if not check_python_version():
        return False
    
    # Step 2: Install dependencies
    print("\nWould you like to install/update dependencies? (y/n): ", end="")
    try:
        response = input().lower().strip()
        if response in ['y', 'yes']:
            if not install_dependencies():
                print("\n⚠️  Installation failed. You can try manually:")
                print("   pip install -r requirements.txt")
                return False
    except KeyboardInterrupt:
        print("\nInstallation cancelled.")
        return False
    
    # Step 3: Check dependencies
    if not check_dependencies():
        print("\n⚠️  Some dependencies are missing. Please install them first.")
        return False
    
    # Step 4: Test WeasyPrint specifically
    if not test_weasyprint():
        print("\n⚠️  WeasyPrint is not working properly.")
        return False
    
    # Step 5: Run converter tests
    print("\nWould you like to run the test suite? (y/n): ", end="")
    try:
        response = input().lower().strip()
        if response in ['y', 'yes']:
            if not run_converter_tests():
                print("\n⚠️  Some tests failed. The converter might not work properly.")
                return False
    except KeyboardInterrupt:
        print("\nTests skipped.")
    
    # Step 6: Show usage examples
    show_usage_examples()
    
    print("\n" + "="*50)
    print("🎉 INSTALLATION COMPLETE!")
    print("="*50)
    print("\nThe Markdown to PDF converter is ready to use.")
    print("\nQuick start:")
    print("  python main.py convert sample.md")
    print("\nFor help:")
    print("  python main.py --help")
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        if not success:
            print("\n❌ Installation/testing completed with issues.")
            print("Please check the errors above and try again.")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)