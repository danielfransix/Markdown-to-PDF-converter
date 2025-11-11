"""CSS styling management for PDF generation."""

from typing import Optional
from .exceptions import StyleError


class StyleManager:
    """Manages CSS styling for PDF generation."""
    
    def __init__(self):
        self._default_css = self._load_default_css()
    
    def get_default_css(self) -> str:
        """Get the default CSS styling."""
        return self._default_css
    
    def load_custom_css(self, css_file_path: str) -> str:
        """Load custom CSS from a file.
        
        Args:
            css_file_path: Path to the CSS file
            
        Returns:
            CSS content as string
            
        Raises:
            StyleError: If CSS file cannot be read
        """
        try:
            with open(css_file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise StyleError(f"CSS file not found: {css_file_path}")
        except Exception as e:
            raise StyleError(f"Error reading CSS file: {e}")
    
    def merge_css(self, base_css: str, custom_css: str) -> str:
        """Merge base CSS with custom CSS.
        
        Args:
            base_css: Base CSS content
            custom_css: Custom CSS to override/extend base
            
        Returns:
            Merged CSS content
        """
        return f"{base_css}\n\n/* Custom Styles */\n{custom_css}"
    
    def _load_default_css(self) -> str:
        """Load the default CSS styling."""
        return """
        @page {
            size: A4;
            margin: 2cm;
            @bottom-right {
                content: counter(page) " / " counter(pages);
                font-size: 10pt;
                color: #666;
                font-family: 'JetBrains Mono', 'Monaco', 'Consolas', monospace;
            }
        }
        
        /* Universal JetBrains Mono font override */
        * {
            font-family: 'JetBrains Mono', 'Monaco', 'Consolas', monospace !important;
        }
        
        body {
            font-family: 'JetBrains Mono', 'Monaco', 'Consolas', monospace;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
            font-size: 11pt;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #2c3e50;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-weight: bold;
            page-break-after: avoid;
        }
        
        h1 {
            font-size: 2.2em;
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.3em;
            page-break-before: always;
        }
        
        h1:first-child {
            page-break-before: avoid;
        }
        
        h2 {
            font-size: 1.8em;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.2em;
        }
        
        h3 {
            font-size: 1.4em;
            color: #34495e;
        }
        
        h4 {
            font-size: 1.2em;
            color: #34495e;
        }
        
        h5, h6 {
            font-size: 1em;
            color: #7f8c8d;
        }
        
        p {
            margin-bottom: 1em;
            text-align: justify;
            orphans: 2;
            widows: 2;
        }
        
        strong, b {
            font-weight: bold;
        }
        
        em, i {
            font-style: italic;
        }
        
        code {
            background-color: #f8f9fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'JetBrains Mono', 'Monaco', 'Consolas', monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }
        
        pre {
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
            margin: 1em 0;
            page-break-inside: avoid;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: #333;
        }
        
        blockquote {
            border-left: 4px solid #3498db;
            margin: 1em 0;
            padding-left: 1em;
            color: #666;
            font-style: italic;
            background-color: #f9f9f9;
            padding: 0.5em 1em;
            border-radius: 0 5px 5px 0;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
            page-break-inside: avoid;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 0.5em;
            text-align: left;
        }
        
        th {
            background-color: #f2f2f2;
            font-weight: bold;
            color: #2c3e50;
        }
        
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        
        ul, ol {
            margin: 1em 0;
            padding-left: 2em;
        }
        
        li {
            margin-bottom: 0.5em;
        }
        
        ul li {
            list-style-type: disc;
        }
        
        ol li {
            list-style-type: decimal;
        }
        
        a {
            color: #3498db;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1em auto;
            page-break-inside: avoid;
        }
        
        hr {
            border: none;
            border-top: 2px solid #eee;
            margin: 2em 0;
            page-break-after: avoid;
        }
        
        /* Task list styling */
        .task-list-item {
            list-style-type: none;
        }
        
        .task-list-item input[type="checkbox"] {
            margin-right: 0.5em;
        }
        
        /* Footnotes */
        .footnote {
            font-size: 0.9em;
            color: #666;
        }
        
        /* Table of contents */
        .toc {
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 5px;
            margin: 1em 0;
        }
        
        .toc h2 {
            margin-top: 0;
            border-bottom: none;
        }
        
        /* Print optimizations */
        @media print {
            body {
                font-size: 10pt;
            }
            
            h1 {
                font-size: 18pt;
            }
            
            h2 {
                font-size: 16pt;
            }
            
            h3 {
                font-size: 14pt;
            }
        }
        """


class ThemeManager:
    """Manages predefined themes for PDF styling."""
    
    THEMES = {
        'default': 'Default professional theme',
        'minimal': 'Clean minimal theme',
        'academic': 'Academic paper theme',
        'modern': 'Modern colorful theme'
    }
    
    def __init__(self, style_manager: StyleManager):
        self.style_manager = style_manager
    
    def get_theme_css(self, theme_name: str) -> str:
        """Get CSS for a specific theme.
        
        Args:
            theme_name: Name of the theme
            
        Returns:
            CSS content for the theme
            
        Raises:
            StyleError: If theme is not found
        """
        if theme_name not in self.THEMES:
            raise StyleError(f"Theme '{theme_name}' not found. Available themes: {list(self.THEMES.keys())}")
        
        if theme_name == 'default':
            return self.style_manager.get_default_css()
        elif theme_name == 'minimal':
            return self._get_minimal_theme()
        elif theme_name == 'academic':
            return self._get_academic_theme()
        elif theme_name == 'modern':
            return self._get_modern_theme()
    
    def list_themes(self) -> dict:
        """List all available themes."""
        return self.THEMES.copy()
    
    def _get_minimal_theme(self) -> str:
        """Get minimal theme CSS."""
        base_css = self.style_manager.get_default_css()
        minimal_overrides = """
        h1, h2, h3, h4, h5, h6 {
            color: #000;
            border-bottom: none;
        }
        
        h1 {
            font-size: 1.8em;
            margin-bottom: 1em;
        }
        
        h2 {
            font-size: 1.5em;
        }
        
        blockquote {
            border-left: 2px solid #ccc;
            background-color: transparent;
        }
        
        pre {
            border-left: none;
            background-color: #f5f5f5;
        }
        """
        return self.style_manager.merge_css(base_css, minimal_overrides)
    
    def _get_academic_theme(self) -> str:
        """Get academic theme CSS."""
        base_css = self.style_manager.get_default_css()
        academic_overrides = """
        body {
            font-family: 'Times New Roman', 'Times', serif;
            font-size: 12pt;
            line-height: 1.8;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Times New Roman', 'Times', serif;
            color: #000;
        }
        
        h1 {
            text-align: center;
            border-bottom: none;
            font-size: 1.5em;
        }
        
        h2 {
            border-bottom: none;
            font-size: 1.3em;
        }
        
        p {
            text-indent: 1.5em;
        }
        
        blockquote {
            font-style: normal;
            margin-left: 2em;
            margin-right: 2em;
        }
        """
        return self.style_manager.merge_css(base_css, academic_overrides)
    
    def _get_modern_theme(self) -> str:
        """Get modern theme CSS."""
        base_css = self.style_manager.get_default_css()
        modern_overrides = """
        body {
            font-family: 'Segoe UI', 'Roboto', sans-serif;
        }
        
        h1 {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1em;
            border-radius: 10px;
            border-bottom: none;
        }
        
        h2 {
            color: #667eea;
            border-bottom: 2px solid #667eea;
        }
        
        h3 {
            color: #764ba2;
        }
        
        blockquote {
            border-left: 4px solid #667eea;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
        }
        
        pre {
            border-left: 4px solid #764ba2;
        }
        
        code {
            background-color: #667eea;
            color: white;
        }
        """
        return self.style_manager.merge_css(base_css, modern_overrides)