"""Command-line interface for the markdown to PDF converter."""

import click
import os
import sys
from pathlib import Path
from typing import Optional
from colorama import init, Fore, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Add the parent directory to the path to import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.converter import MarkdownToPDFConverter
from core.exceptions import (
    ConverterError,
    FileNotFoundError as ConverterFileNotFoundError,
    ConversionError,
    StyleError
)


def print_success(message: str) -> None:
    """Print success message in green."""
    click.echo(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")


def print_error(message: str) -> None:
    """Print error message in red."""
    click.echo(f"{Fore.RED}❌ {message}{Style.RESET_ALL}")


def print_warning(message: str) -> None:
    """Print warning message in yellow."""
    click.echo(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")


def print_info(message: str) -> None:
    """Print info message in blue."""
    click.echo(f"{Fore.BLUE}ℹ️  {message}{Style.RESET_ALL}")


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Markdown to PDF Converter - Convert markdown documents to beautifully formatted PDFs."""
    pass


@cli.command()
@click.argument('input_file', type=click.Path(exists=True, dir_okay=False))
@click.option('-o', '--output', type=click.Path(), help='Output PDF file path')
@click.option('-t', '--theme', help='Theme to use for styling (optional, defaults to Manrope)')
@click.option('-c', '--css', type=click.Path(exists=True), help='Custom CSS file')
@click.option('--custom-css', help='Custom CSS as string')
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose output')
@click.option('--preview', is_flag=True, help='Generate HTML preview instead of PDF')
def convert(input_file: str, output: Optional[str], theme: Optional[str], css: Optional[str], 
           custom_css: Optional[str], verbose: bool, preview: bool):
    """Convert a markdown file to PDF.
    
    INPUT_FILE: Path to the markdown file to convert
    """
    try:
        converter = MarkdownToPDFConverter()
        
        if verbose:
            print_info(f"Converting: {input_file}")
            if theme:
                print_info(f"Theme: {theme}")
            else:
                print_info("Theme: Default (Manrope)")
            if css:
                print_info(f"Custom CSS file: {css}")
            if custom_css:
                print_info("Custom CSS provided")
        
        if preview:
            # Generate HTML preview
            with open(input_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            html_content = converter.preview_html(markdown_content, theme or 'default')
            
            # Determine output path for HTML
            if output:
                html_output = str(Path(output).with_suffix('.html'))
            else:
                html_output = str(Path(input_file).with_suffix('.html'))
            
            with open(html_output, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print_success(f"HTML preview generated: {html_output}")
        else:
            # Convert to PDF
            output_path = converter.convert_file(
                markdown_file_path=input_file,
                output_pdf_path=output,
                theme=theme or 'default',
                custom_css=custom_css,
                custom_css_file=css
            )
            
            print_success(f"PDF generated successfully: {output_path}")
            
            if verbose:
                file_size = os.path.getsize(output_path)
                print_info(f"File size: {file_size:,} bytes")
    
    except ConverterFileNotFoundError as e:
        print_error(f"File not found: {e.file_path}")
        sys.exit(1)
    except StyleError as e:
        print_error(f"Style error: {e}")
        sys.exit(1)
    except ConversionError as e:
        print_error(f"Conversion error: {e}")
        if verbose and e.original_error:
            print_error(f"Original error: {e.original_error}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


@cli.command()
def themes():
    """List available themes."""
    try:
        converter = MarkdownToPDFConverter()
        available_themes = converter.get_available_themes()
        
        print_info("Available themes:")
        for theme_name, description in available_themes.items():
            click.echo(f"  {Fore.CYAN}{theme_name:<12}{Style.RESET_ALL} - {description}")
    
    except Exception as e:
        print_error(f"Error listing themes: {e}")
        sys.exit(1)


@cli.command()
def extras():
    """List available markdown extras."""
    try:
        converter = MarkdownToPDFConverter()
        available_extras = converter.get_available_markdown_extras()
        
        print_info("Available markdown extras:")
        for extra_name, description in available_extras.items():
            click.echo(f"  {Fore.CYAN}{extra_name:<20}{Style.RESET_ALL} - {description}")
    
    except Exception as e:
        print_error(f"Error listing extras: {e}")
        sys.exit(1)


@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False))
@click.option('-o', '--output-dir', type=click.Path(), help='Output directory for PDFs')
@click.option('-t', '--theme', help='Theme to use for styling (optional, defaults to Manrope)')
@click.option('-c', '--css', type=click.Path(exists=True), help='Custom CSS file')
@click.option('--custom-css', help='Custom CSS as string')
@click.option('-v', '--verbose', is_flag=True, help='Enable verbose output')
@click.option('--recursive', is_flag=True, help='Process subdirectories recursively')
def batch(directory: str, output_dir: Optional[str], theme: Optional[str], css: Optional[str],
         custom_css: Optional[str], verbose: bool, recursive: bool):
    """Convert all markdown files in a directory to PDF.
    
    DIRECTORY: Directory containing markdown files
    """
    try:
        converter = MarkdownToPDFConverter()
        
        # Find all markdown files
        directory_path = Path(directory)
        if recursive:
            md_files = list(directory_path.rglob('*.md')) + list(directory_path.rglob('*.markdown'))
        else:
            md_files = list(directory_path.glob('*.md')) + list(directory_path.glob('*.markdown'))
        
        if not md_files:
            print_warning(f"No markdown files found in {directory}")
            return
        
        print_info(f"Found {len(md_files)} markdown file(s)")
        
        # Determine output directory
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
        else:
            output_path = directory_path
        
        successful_conversions = 0
        failed_conversions = 0
        
        for md_file in md_files:
            try:
                if verbose:
                    print_info(f"Processing: {md_file.name}")
                
                # Maintain directory structure in output
                relative_path = md_file.relative_to(directory_path)
                output_file = output_path / relative_path.with_suffix('.pdf')
                
                # Ensure output subdirectory exists
                output_file.parent.mkdir(parents=True, exist_ok=True)
                
                converter.convert_file(
                    markdown_file_path=str(md_file),
                    output_pdf_path=str(output_file),
                    theme=theme or 'default',
                    custom_css=custom_css,
                    custom_css_file=css
                )
                
                successful_conversions += 1
                if verbose:
                    print_success(f"Converted: {md_file.name} -> {output_file.name}")
            
            except Exception as e:
                failed_conversions += 1
                print_error(f"Failed to convert {md_file.name}: {e}")
        
        # Summary
        print_info(f"Conversion complete: {successful_conversions} successful, {failed_conversions} failed")
        
        if failed_conversions > 0:
            sys.exit(1)
    
    except Exception as e:
        print_error(f"Batch conversion error: {e}")
        sys.exit(1)


@cli.command()
@click.argument('markdown_file', type=click.Path(exists=True, dir_okay=False))
@click.option('-t', '--theme', help='Theme to use for preview (optional, defaults to Manrope)')
def preview(markdown_file: str, theme: Optional[str]):
    """Generate an HTML preview of a markdown file.
    
    MARKDOWN_FILE: Path to the markdown file to preview
    """
    try:
        converter = MarkdownToPDFConverter()
        
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = converter.preview_html(markdown_content, theme)
        
        # Generate output path
        output_path = str(Path(markdown_file).with_suffix('.html'))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print_success(f"HTML preview generated: {output_path}")
        print_info("Open the HTML file in your browser to preview the styling")
    
    except Exception as e:
        print_error(f"Preview generation error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    cli()
