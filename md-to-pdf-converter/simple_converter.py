#!/usr/bin/env python3
"""Simple markdown to PDF converter using ReportLab instead of WeasyPrint."""

import os
import sys
from pathlib import Path
import markdown2
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import re


class SimpleMarkdownToPDF:
    """Simple markdown to PDF converter using ReportLab."""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom styles for better formatting."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor='#2c3e50'
        ))
        
        # Heading 1
        self.styles.add(ParagraphStyle(
            name='CustomHeading1',
            parent=self.styles['Heading1'],
            fontSize=18,
            spaceAfter=12,
            spaceBefore=18,
            textColor='#2c3e50',
            fontName='Helvetica-Bold'
        ))
        
        # Heading 2
        self.styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=10,
            spaceBefore=16,
            textColor='#34495e',
            fontName='Helvetica-Bold'
        ))
        
        # Heading 3
        self.styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=self.styles['Heading3'],
            fontSize=14,
            spaceAfter=8,
            spaceBefore=14,
            textColor='#34495e',
            fontName='Helvetica-Bold'
        ))
        
        # Normal text
        self.styles.add(ParagraphStyle(
            name='CustomNormal',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            fontName='Helvetica'
        ))
        
        # Bullet points
        self.styles.add(ParagraphStyle(
            name='CustomBullet',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=4,
            leftIndent=20,
            bulletIndent=10,
            fontName='Helvetica'
        ))
    
    def convert_markdown_to_pdf(self, markdown_file, output_pdf):
        """Convert markdown file to PDF."""
        # Read markdown content
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'tables'])
        
        # Create PDF document
        doc = SimpleDocTemplate(
            output_pdf,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Build story (content)
        story = []
        
        # Process the HTML content line by line
        lines = html_content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Process headings
            if line.startswith('<h1>'):
                text = re.sub(r'<[^>]+>', '', line)
                story.append(Paragraph(text, self.styles['CustomHeading1']))
                story.append(Spacer(1, 12))
            elif line.startswith('<h2>'):
                text = re.sub(r'<[^>]+>', '', line)
                story.append(Paragraph(text, self.styles['CustomHeading2']))
                story.append(Spacer(1, 10))
            elif line.startswith('<h3>'):
                text = re.sub(r'<[^>]+>', '', line)
                story.append(Paragraph(text, self.styles['CustomHeading3']))
                story.append(Spacer(1, 8))
            elif line.startswith('<p>'):
                text = re.sub(r'<[^>]+>', '', line)
                if text:
                    # Handle bold and italic text
                    text = self._format_text(text)
                    story.append(Paragraph(text, self.styles['CustomNormal']))
                    story.append(Spacer(1, 6))
            elif line.startswith('<ul>'):
                # Process list items
                list_items = re.findall(r'<li>(.*?)</li>', line)
                for item in list_items:
                    item = self._format_text(item)
                    story.append(Paragraph(f'• {item}', self.styles['CustomBullet']))
                    story.append(Spacer(1, 4))
            elif line.startswith('<strong>'):
                text = re.sub(r'<[^>]+>', '', line)
                formatted_text = f'<b>{text}</b>'
                story.append(Paragraph(formatted_text, self.styles['CustomNormal']))
                story.append(Spacer(1, 6))
        
        # Build PDF
        doc.build(story)
        return output_pdf
    
    def _format_text(self, text):
        """Format text with basic HTML tags for ReportLab."""
        # Convert basic markdown-like formatting to HTML
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)  # Bold
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)      # Italic
        return text


def main():
    """Main function to run the converter."""
    if len(sys.argv) < 2:
        print("Usage: python simple_converter.py <input_markdown_file> [output_pdf_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        # Generate output filename from input
        input_path = Path(input_file)
        output_file = input_path.parent / f"{input_path.stem}.pdf"
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    try:
        converter = SimpleMarkdownToPDF()
        result = converter.convert_markdown_to_pdf(input_file, str(output_file))
        print(f"✅ PDF generated successfully: {result}")
    except Exception as e:
        print(f"❌ Error converting file: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()