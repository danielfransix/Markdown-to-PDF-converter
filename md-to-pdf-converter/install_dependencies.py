#!/usr/bin/env python3
"""
Installation helper script for md-to-pdf-converter.
This script installs Python dependencies and provides guidance for system dependencies.
"""

import subprocess
import sys
import platform
from pathlib import Path

def install_python_dependencies():
    """Install all Python dependencies from requirements.txt."""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Python dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Python dependencies: {e}")
        return False

def check_system_dependencies():
    """Check and provide guidance for system dependencies."""
    system = platform.system()
    print(f"🔍 Detected operating system: {system}")
    
    if system == "Windows":
        print("\n⚠️  Windows users need to install GTK3 runtime:")
        print("   1. Download from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer")
        print("   2. Run the installer and follow the setup wizard")
        print("   3. Restart your terminal after installation")
        
    elif system == "Darwin":  # macOS
        print("\n⚠️  macOS users need to install system libraries:")
        print("   brew install cairo pango gdk-pixbuf libffi")
        
    elif system == "Linux":
        print("\n⚠️  Linux users need to install system libraries:")
        print("   Ubuntu/Debian:")
        print("   sudo apt-get install build-essential python3-dev python3-pip")
        print("   sudo apt-get install libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info")
        print("\n   Fedora/RHEL:")
        print("   sudo dnf install cairo pango gdk-pixbuf2 libffi")
        print("\n   Arch Linux:")
        print("   sudo pacman -S cairo pango gdk-pixbuf2 libffi")

def verify_installation():
    """Verify that the converter is ready to use."""
    print("\n🔍 Verifying installation...")
    try:
        # Test importing key modules
        import markdown2
        import weasyprint
        import PIL
        import click
        import colorama
        
        print("✅ All Python modules imported successfully!")
        
        # Test basic converter functionality
        from core.converter import MarkdownToPDFConverter
        converter = MarkdownToPDFConverter()
        print("✅ Converter initialized successfully!")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return False

def main():
    """Main installation process."""
    print("🚀 MD-to-PDF Converter Setup Assistant")
    print("=" * 40)
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found in current directory!")
        print("   Please run this script from the md-to-pdf-converter directory.")
        sys.exit(1)
    
    # Install Python dependencies
    if not install_python_dependencies():
        print("\n❌ Setup failed during Python dependency installation.")
        sys.exit(1)
    
    # Check system dependencies
    check_system_dependencies()
    
    # Verify installation
    if verify_installation():
        print("\n🎉 Setup completed successfully!")
        print("\n📋 Next steps:")
        print("   1. Install system dependencies (see instructions above)")
        print("   2. Restart your terminal")
        print("   3. Test with: python main.py --help")
        print("\n📖 For detailed usage instructions, see USER_GUIDE.md")
    else:
        print("\n⚠️  Setup completed but verification failed.")
        print("   Please check the error messages above and install any missing dependencies.")

if __name__ == "__main__":
    main()