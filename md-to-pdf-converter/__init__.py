"""Markdown to PDF Converter Package

A well-organized Python package for converting Markdown documents to PDF
with customizable styling and professional formatting.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .core.converter import MarkdownToPDFConverter
from .core.exceptions import ConverterError, FileNotFoundError, ConversionError

__all__ = [
    "MarkdownToPDFConverter",
    "ConverterError",
    "FileNotFoundError", 
    "ConversionError"
]