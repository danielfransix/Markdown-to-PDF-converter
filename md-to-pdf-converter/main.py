#!/usr/bin/env python3
"""Entry point for the markdown to PDF converter CLI."""

import sys
from pathlib import Path

# Add the current directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from cli.main import cli

if __name__ == '__main__':
    cli()