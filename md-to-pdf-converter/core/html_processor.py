"""HTML processing and generation from markdown content."""

import markdown2
from typing import Dict, Any, Optional
from .exceptions import InvalidMarkdownError


class HTMLProcessor:
    """Processes markdown content and converts it to HTML."""
    
    def __init__(self, markdown_extras: Optional[list] = None):
        """Initialize the HTML processor.
        
        Args:
            markdown_extras: List of markdown2 extras to enable
        """
        self.markdown_extras = markdown_extras or self._get_default_extras()
    
    def convert_markdown_to_html(self, markdown_content: str) -> str:
        """Convert markdown content to HTML.
        
        Args:
            markdown_content: Raw markdown content
            
        Returns:
            HTML content
            
        Raises:
            InvalidMarkdownError: If markdown conversion fails
        """
        try:
            # Check if metadata extra is enabled but no metadata section exists
            if 'metadata' in self.markdown_extras and not self._has_metadata_section(markdown_content):
                # Temporarily disable metadata extra to avoid heading stripping
                original_extras = self.markdown_extras.copy()
                filtered_extras = [extra for extra in self.markdown_extras if extra != 'metadata']
                
                html_content = markdown2.markdown(
                    markdown_content,
                    extras=filtered_extras
                )
                
                # Restore original extras
                self.markdown_extras = original_extras
                return html_content
            else:
                html_content = markdown2.markdown(
                    markdown_content,
                    extras=self.markdown_extras
                )
                return html_content
        except Exception as e:
            raise InvalidMarkdownError(f"Failed to convert markdown to HTML: {e}")
    
    def create_complete_html_document(self, body_content: str, title: str = "Markdown Document", 
                                    meta_tags: Optional[Dict[str, str]] = None) -> str:
        """Create a complete HTML document with proper structure.
        
        Args:
            body_content: HTML content for the body
            title: Document title
            meta_tags: Additional meta tags
            
        Returns:
            Complete HTML document
        """
        meta_html = self._generate_meta_tags(meta_tags or {})
        
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {meta_html}
</head>
<body>
    {body_content}
</body>
</html>
        """.strip()
    
    def process_markdown_file(self, file_path: str) -> str:
        """Process a markdown file and return HTML content.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            HTML content
            
        Raises:
            InvalidMarkdownError: If file cannot be read or processed
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
            return self.convert_markdown_to_html(markdown_content)
        except FileNotFoundError:
            raise InvalidMarkdownError(f"Markdown file not found: {file_path}")
        except UnicodeDecodeError as e:
            raise InvalidMarkdownError(f"Error reading file {file_path}: {e}")
        except Exception as e:
            raise InvalidMarkdownError(f"Error processing markdown file {file_path}: {e}")
    
    def extract_title_from_markdown(self, markdown_content: str) -> str:
        """Extract title from markdown content (first heading of any level).
        
        Args:
            markdown_content: Raw markdown content
            
        Returns:
            Extracted title or default title
        """
        lines = markdown_content.split('\n')
        for line in lines:
            line = line.strip()
            # Check for any heading level (H1-H6)
            if line.startswith('#'):
                # Remove the heading markers and return the text
                title = line.lstrip('#').strip()
                if title:  # Only return if there's actual text
                    return title
        return "Markdown Document"
    
    def _get_default_extras(self) -> list:
        """Get default markdown2 extras."""
        return [
            'fenced-code-blocks',
            'tables',
            'strike',
            'task_list',
            'footnotes',
            'header-ids',
            'toc',
            'code-friendly',
            'cuddled-lists',
            'metadata',
            'smarty-pants'
        ]
    
    def _has_metadata_section(self, markdown_content: str) -> bool:
        """Check if markdown content contains a metadata section.
        
        Args:
            markdown_content: Raw markdown content
            
        Returns:
            True if metadata section exists, False otherwise
        """
        content = markdown_content.strip()
        return content.startswith('---\n') or content.startswith('---\r\n')

    def _generate_meta_tags(self, meta_tags: Dict[str, str]) -> str:
        """Generate HTML meta tags.
        
        Args:
            meta_tags: Dictionary of meta tag name-content pairs
            
        Returns:
            HTML meta tags string
        """
        meta_html = []
        for name, content in meta_tags.items():
            meta_html.append(f'    <meta name="{name}" content="{content}">')
        return '\n'.join(meta_html)
    
    def get_available_extras(self) -> Dict[str, str]:
        """Get information about available markdown extras.
        
        Returns:
            Dictionary mapping extra names to descriptions
        """
        return {
            'fenced-code-blocks': 'Support for fenced code blocks with syntax highlighting',
            'tables': 'Support for tables',
            'strike': 'Support for strikethrough text',
            'task_list': 'Support for GitHub-style task lists',
            'footnotes': 'Support for footnotes',
            'header-ids': 'Automatic generation of header IDs',
            'toc': 'Table of contents generation',
            'code-friendly': 'Better handling of code in lists',
            'cuddled-lists': 'Allow lists to be cuddled to preceding paragraph',
            'metadata': 'Support for metadata in markdown files',
            'smarty-pants': 'Smart quotes and other typographic improvements'
        }
    
    def configure_extras(self, extras: list) -> None:
        """Configure markdown extras to use.
        
        Args:
            extras: List of extra names to enable
        """
        available_extras = set(self.get_available_extras().keys())
        invalid_extras = set(extras) - available_extras
        
        if invalid_extras:
            raise InvalidMarkdownError(
                f"Invalid markdown extras: {invalid_extras}. "
                f"Available extras: {available_extras}"
            )
        
        self.markdown_extras = extras