"""Main converter class for markdown to PDF conversion."""

import os
from pathlib import Path
from typing import Optional, Dict, Any
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

from .html_processor import HTMLProcessor
from .styling import StyleManager, ThemeManager
from .exceptions import (
    ConversionError, 
    FileNotFoundError as ConverterFileNotFoundError,
    StyleError
)


class MarkdownToPDFConverter:
    """Main converter class for converting markdown documents to PDF."""
    
    def __init__(self, markdown_extras: Optional[list] = None):
        """Initialize the converter.
        
        Args:
            markdown_extras: List of markdown2 extras to enable
        """
        self.html_processor = HTMLProcessor(markdown_extras)
        self.style_manager = StyleManager()
        self.theme_manager = ThemeManager(self.style_manager)
        self.font_config = FontConfiguration()
    
    def convert_file(self, 
                    markdown_file_path: str, 
                    output_pdf_path: Optional[str] = None,
                    theme: str = 'default',
                    custom_css: Optional[str] = None,
                    custom_css_file: Optional[str] = None,
                    meta_tags: Optional[Dict[str, str]] = None) -> str:
        """Convert a markdown file to PDF.
        
        Args:
            markdown_file_path: Path to the markdown file
            output_pdf_path: Path for the output PDF (optional)
            theme: Theme name to use for styling
            custom_css: Custom CSS content as string
            custom_css_file: Path to custom CSS file
            meta_tags: Additional meta tags for the HTML document
            
        Returns:
            Path to the generated PDF file
            
        Raises:
            ConverterFileNotFoundError: If markdown file is not found
            ConversionError: If conversion fails
        """
        # Validate input file
        if not os.path.exists(markdown_file_path):
            raise ConverterFileNotFoundError(markdown_file_path)
        
        try:
            # Process markdown to HTML
            html_content = self.html_processor.process_markdown_file(markdown_file_path)
            
            # Extract title from markdown for the document
            with open(markdown_file_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
            title = self.html_processor.extract_title_from_markdown(markdown_content)
            
            # Create complete HTML document
            full_html = self.html_processor.create_complete_html_document(
                html_content, title, meta_tags
            )
            
            # Determine output path
            if output_pdf_path is None:
                base_name = Path(markdown_file_path).stem
                output_pdf_path = str(Path(markdown_file_path).parent / f"{base_name}.pdf")
            
            # Generate CSS
            css_content = self._prepare_css(theme, custom_css, custom_css_file)
            
            # Convert to PDF
            self._generate_pdf(full_html, css_content, output_pdf_path)
            
            return output_pdf_path
            
        except Exception as e:
            if isinstance(e, (ConverterFileNotFoundError, ConversionError, StyleError)):
                raise
            raise ConversionError(f"Unexpected error during conversion", e)
    
    def convert_string(self,
                      markdown_content: str,
                      output_pdf_path: str,
                      title: str = "Markdown Document",
                      theme: str = 'default',
                      custom_css: Optional[str] = None,
                      custom_css_file: Optional[str] = None,
                      meta_tags: Optional[Dict[str, str]] = None) -> str:
        """Convert markdown content string to PDF.
        
        Args:
            markdown_content: Raw markdown content
            output_pdf_path: Path for the output PDF
            title: Document title
            theme: Theme name to use for styling
            custom_css: Custom CSS content as string
            custom_css_file: Path to custom CSS file
            meta_tags: Additional meta tags for the HTML document
            
        Returns:
            Path to the generated PDF file
            
        Raises:
            ConversionError: If conversion fails
        """
        try:
            # Process markdown to HTML
            html_content = self.html_processor.convert_markdown_to_html(markdown_content)
            
            # Create complete HTML document
            full_html = self.html_processor.create_complete_html_document(
                html_content, title, meta_tags
            )
            
            # Generate CSS
            css_content = self._prepare_css(theme, custom_css, custom_css_file)
            
            # Convert to PDF
            self._generate_pdf(full_html, css_content, output_pdf_path)
            
            return output_pdf_path
            
        except Exception as e:
            if isinstance(e, (ConversionError, StyleError)):
                raise
            raise ConversionError(f"Unexpected error during conversion", e)
    
    def _prepare_css(self, 
                    theme: str, 
                    custom_css: Optional[str] = None,
                    custom_css_file: Optional[str] = None) -> str:
        """Prepare the final CSS content for PDF generation.
        
        Args:
            theme: Theme name
            custom_css: Custom CSS content
            custom_css_file: Path to custom CSS file
            
        Returns:
            Final CSS content
            
        Raises:
            StyleError: If CSS preparation fails
        """
        try:
            # Get base theme CSS
            css_content = self.theme_manager.get_theme_css(theme)
            
            # Add custom CSS from file if provided
            if custom_css_file:
                file_css = self.style_manager.load_custom_css(custom_css_file)
                css_content = self.style_manager.merge_css(css_content, file_css)
            
            # Add custom CSS string if provided
            if custom_css:
                css_content = self.style_manager.merge_css(css_content, custom_css)
            
            return css_content
            
        except Exception as e:
            if isinstance(e, StyleError):
                raise
            raise StyleError(f"Error preparing CSS: {e}")
    
    def _generate_pdf(self, html_content: str, css_content: str, output_path: str) -> None:
        """Generate PDF from HTML and CSS content.
        
        Args:
            html_content: Complete HTML document
            css_content: CSS styling
            output_path: Output PDF file path
            
        Raises:
            ConversionError: If PDF generation fails
        """
        try:
            # Create HTML and CSS objects
            html_doc = HTML(string=html_content)
            css_doc = CSS(string=css_content, font_config=self.font_config)
            
            # Ensure output directory exists
            output_dir = Path(output_path).parent
            output_dir.mkdir(parents=True, exist_ok=True)
            
            html_doc.write_pdf(output_path, stylesheets=[css_doc], font_config=self.font_config)
            
        except Exception as e:
            raise ConversionError(f"Failed to generate PDF: {e}", e)
    
    def get_available_themes(self) -> Dict[str, str]:
        """Get available themes.
        
        Returns:
            Dictionary mapping theme names to descriptions
        """
        return self.theme_manager.list_themes()
    
    def get_available_markdown_extras(self) -> Dict[str, str]:
        """Get available markdown extras.
        
        Returns:
            Dictionary mapping extra names to descriptions
        """
        return self.html_processor.get_available_extras()
    
    def configure_markdown_extras(self, extras: list) -> None:
        """Configure markdown extras to use.
        
        Args:
            extras: List of extra names to enable
        """
        self.html_processor.configure_extras(extras)
    
    def preview_html(self, markdown_content: str, theme: str = 'default') -> str:
        """Generate HTML preview of markdown content.
        
        Args:
            markdown_content: Raw markdown content
            theme: Theme to use for styling
            
        Returns:
            Complete HTML document with inline CSS
        """
        try:
            # Convert markdown to HTML
            html_content = self.html_processor.convert_markdown_to_html(markdown_content)
            
            # Get theme CSS
            css_content = self.theme_manager.get_theme_css(theme)
            
            # Create HTML with inline CSS
            title = self.html_processor.extract_title_from_markdown(markdown_content)
            
            return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{css_content}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
            """.strip()
            
        except Exception as e:
            raise ConversionError(f"Failed to generate HTML preview: {e}", e)