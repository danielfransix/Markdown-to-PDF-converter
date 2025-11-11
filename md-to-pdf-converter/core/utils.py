"""Utility functions for the markdown to PDF converter."""

import os
import sys
from pathlib import Path
from typing import Optional, List, Dict, Any


def ensure_directory_exists(directory_path: str) -> None:
    """Ensure a directory exists, creating it if necessary.
    
    Args:
        directory_path: Path to the directory
    """
    Path(directory_path).mkdir(parents=True, exist_ok=True)


def get_file_size_formatted(file_path: str) -> str:
    """Get formatted file size (KB, MB, etc.).
    
    Args:
        file_path: Path to the file
        
    Returns:
        Formatted file size string
    """
    size_bytes = os.path.getsize(file_path)
    
    # Format size
    for unit in ['bytes', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0 or unit == 'GB':
            break
        size_bytes /= 1024.0
    
    return f"{size_bytes:.2f} {unit}"


def get_file_extension(file_path: str) -> str:
    """Get file extension without the dot.
    
    Args:
        file_path: Path to the file
        
    Returns:
        File extension without the dot
    """
    return Path(file_path).suffix.lstrip('.')


def is_markdown_file(file_path: str) -> bool:
    """Check if a file is a markdown file based on extension.
    
    Args:
        file_path: Path to the file
        
    Returns:
        True if file is a markdown file, False otherwise
    """
    extension = get_file_extension(file_path).lower()
    return extension in ['md', 'markdown']


def find_markdown_files(directory: str, recursive: bool = False) -> List[Path]:
    """Find all markdown files in a directory.
    
    Args:
        directory: Directory to search
        recursive: Whether to search recursively
        
    Returns:
        List of Path objects for markdown files
    """
    directory_path = Path(directory)
    
    if recursive:
        md_files = list(directory_path.rglob('*.md')) + list(directory_path.rglob('*.markdown'))
    else:
        md_files = list(directory_path.glob('*.md')) + list(directory_path.glob('*.markdown'))
    
    return md_files


def get_relative_path(file_path: str, base_path: str) -> str:
    """Get path relative to a base path.
    
    Args:
        file_path: Absolute file path
        base_path: Base path to make relative to
        
    Returns:
        Relative path
    """
    return str(Path(file_path).relative_to(Path(base_path)))


def sanitize_filename(filename: str) -> str:
    """Sanitize a filename by removing invalid characters.
    
    Args:
        filename: Original filename
        
    Returns:
        Sanitized filename
    """
    # Replace invalid characters with underscore
    invalid_chars = '<>:"\\/|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


def extract_metadata(markdown_content: str) -> Dict[str, Any]:
    """Extract metadata from markdown content.
    
    Args:
        markdown_content: Raw markdown content
        
    Returns:
        Dictionary of metadata
    """
    metadata = {}
    lines = markdown_content.split('\n')
    
    # Check for YAML frontmatter
    if lines and lines[0].strip() == '---':
        frontmatter_end = -1
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                frontmatter_end = i
                break
        
        if frontmatter_end > 0:
            frontmatter_lines = lines[1:frontmatter_end]
            for line in frontmatter_lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
    
    return metadata


def get_default_output_path(input_path: str, output_extension: str = 'pdf') -> str:
    """Generate default output path based on input path.
    
    Args:
        input_path: Input file path
        output_extension: Output file extension
        
    Returns:
        Default output path
    """
    return str(Path(input_path).with_suffix(f'.{output_extension}'))