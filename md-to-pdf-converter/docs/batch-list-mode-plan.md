# Batch File-List Trigger Mode

## Goal

- Run a single Python file (no CLI args) that reads a plain text list of paths and converts all referenced Markdown files to PDF.
- Use the existing converter in `core.converter` to avoid duplicating logic.

## Feasibility

- Fully feasible with the current architecture.
- The `MarkdownToPDFConverter.convert_file` method handles per-file conversion (`md-to-pdf-converter/core/converter.py:32`).
- Existing batch logic in the CLI shows how to walk directories and maintain output structure (`md-to-pdf-converter/cli/main.py:164`).

## Proposed Design

- Files involved:
  - `md-to-pdf-converter/md_paths.txt` (plain text; you author this list).
  - `md-to-pdf-converter/batch_from_list.py` (trigger script you run).

- Behavior:
  - Reads `md_paths.txt` line-by-line.
  - Ignores blank lines and lines starting with `#`.
  - Supports:
    - Absolute or relative file paths to `.md`/`.markdown` files.
    - Directory paths (scan for markdown; optional recursive flag in script).
    - Glob patterns like `docs/**/*.md`.
  - Deduplicates discovered files and converts them.
  - Default output: PDF written next to each source file.
  - Optional constants at the top of the script to customize:
    - `DEFAULT_THEME` (e.g., `default`, `modern`, `academic`).
    - `OUTPUT_DIR` (write PDFs to a single directory while preserving structure).
    - `RECURSIVE_DIRECTORIES` (True/False when a listed path is a directory).
    - `CUSTOM_CSS_FILE` / `CUSTOM_CSS` (optional styling overrides).

## List File Format (`md_paths.txt`)

- One path per line; comments allowed with `#`.
- Examples:

```
# Absolute file path
g:\Documents\reports\q4\summary.md

# Relative file path (from md-to-pdf-converter/)
examples\technical.md

# Directory (non-recursive)
c:\Github Repos\Markdown-to-PDF-converter\md-to-pdf-converter\examples

# Directory (recursive — controlled by script constant)
c:\Docs\handbooks

# Glob pattern
c:\Docs\knowledge-base\**\*.md
```

## Script Outline (`batch_from_list.py`)

- High-level pseudocode:

```
from pathlib import Path
import glob
from core.converter import MarkdownToPDFConverter

LIST_FILE = Path(__file__).parent / 'md_paths.txt'
DEFAULT_THEME = 'default'
OUTPUT_DIR = None  # e.g., Path('pdfs') or None to write next to source
RECURSIVE_DIRECTORIES = True
CUSTOM_CSS_FILE = None
CUSTOM_CSS = None

def iter_paths(list_file):
    for raw in list_file.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        yield line

def expand_to_files(path_spec):
    p = Path(path_spec)
    # glob pattern
    if any(ch in path_spec for ch in ['*', '?']):
        return [Path(x) for x in glob.glob(path_spec, recursive=True)]
    # directory
    if p.is_dir():
        pattern = '**/*.md' if RECURSIVE_DIRECTORIES else '*.md'
        return list(p.rglob('*.md')) if RECURSIVE_DIRECTORIES else list(p.glob('*.md'))
    # file
    if p.is_file():
        return [p]
    return []

def main():
    conv = MarkdownToPDFConverter()
    files = []
    for spec in iter_paths(LIST_FILE):
        files.extend(expand_to_files(spec))
    # dedupe and filter markdown extensions
    unique = []
    seen = set()
    for f in files:
        if f.suffix.lower() in ('.md', '.markdown') and f.exists():
            key = f.resolve()
            if key not in seen:
                seen.add(key)
                unique.append(f)
    for md in unique:
        if OUTPUT_DIR:
            rel = md.name
            out = Path(OUTPUT_DIR) / Path(rel).with_suffix('.pdf')
            out.parent.mkdir(parents=True, exist_ok=True)
            out_path = str(out)
        else:
            out_path = str(md.with_suffix('.pdf'))
        conv.convert_file(
            markdown_file_path=str(md),
            output_pdf_path=out_path,
            theme=DEFAULT_THEME,
            custom_css=CUSTOM_CSS,
            custom_css_file=CUSTOM_CSS_FILE,
        )

if __name__ == '__main__':
    main()
```

## How To Run

- Prereqs:
  - Install system deps for WeasyPrint as per README.
  - `pip install -r requirements.txt` inside `md-to-pdf-converter/`.

- Steps:
  1) Create `md-to-pdf-converter/md_paths.txt` with the paths you want to convert.
  2) Place `batch_from_list.py` in `md-to-pdf-converter/`.
  3) From `md-to-pdf-converter/`, run:

```
python batch_from_list.py
```

- Result:
  - PDFs are created next to each source file, or under `OUTPUT_DIR` if set.

## Notes & Options

- Theme choices are listed by `python main.py themes`.
- You can reuse CLI features if needed:
  - Directory batch: `python main.py batch <dir> --recursive -o <out>`.
  - Single file: `python main.py convert <file> -t <theme>`.
- The plan above avoids any CLI args so your trigger file runs “as-is”.

## Validation Plan

- Smoke test with a small `md_paths.txt` that includes:
  - One absolute file path.
  - One directory with a couple of `.md` files.
  - One glob pattern.
- Verify PDFs appear and open correctly.
- If conversion fails, check:
  - Path correctness and file existence.
  - WeasyPrint system dependencies.
  - Python dependencies and versions.

## Future Enhancements (Optional)

- Add `batch_config.json` to centralize theme/output settings without editing code.
- Preserve directory structure under `OUTPUT_DIR` using paths relative to each listed directory root.
- Integrate this mode as a first-class CLI command (e.g., `python main.py list md_paths.txt`).
 
---

## Directory List Trigger Mode

### Goal

- Run a second Python trigger file (no CLI args) that reads a list of directory paths and recursively converts every Markdown file in those directories and all subfolders.

### Feasibility

- Directly supported by current code. The CLI `batch` command already demonstrates recursive directory traversal (`md-to-pdf-converter/cli/main.py:164`).
- We can reuse `MarkdownToPDFConverter.convert_file` for conversions (`md-to-pdf-converter/core/converter.py:32`).
- Optional helper exists to find markdown files: `find_markdown_files(directory, recursive=True)` (`md-to-pdf-converter/core/utils.py:46`).

### Files Involved

- `md-to-pdf-converter/md_dirs.txt` — plain text list of directory paths.
- `md-to-pdf-converter/batch_from_dirs.py` — trigger script to run.

### List File Format (`md_dirs.txt`)

- One directory path per line; comments allowed with `#`.
- Supports absolute or relative paths.
- Example:

```
# Company docs
c:\Docs\handbooks

# Project docs
c:\Github Repos\Markdown-to-PDF-converter\md-to-pdf-converter\examples

# Another repo
g:\KnowledgeBase\articles
```

### Behavior

- Reads `md_dirs.txt` line-by-line, skips blanks and comments.
- For each valid directory, recursively finds `.md` and `.markdown` files in all subfolders.
- Deduplicates files across directories.
- Converts each file using configured theme and optional CSS.
- Default output: write PDFs next to each source file.
- Optional `OUTPUT_DIR`: write all PDFs under a single directory, preserving structure relative to each listed directory root.

### Script Outline (`batch_from_dirs.py`)

```
from pathlib import Path
from core.converter import MarkdownToPDFConverter
from core.utils import find_markdown_files

LIST_FILE = Path(__file__).parent / 'md_dirs.txt'
DEFAULT_THEME = 'default'
OUTPUT_DIR = None  # e.g., Path('pdfs') to centralize output; None = next to source
CUSTOM_CSS_FILE = None
CUSTOM_CSS = None

def iter_dirs(list_file):
    for raw in list_file.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        yield Path(line)

def main():
    conv = MarkdownToPDFConverter()
    all_files = []
    for d in iter_dirs(LIST_FILE):
        if d.is_dir():
            files = find_markdown_files(str(d), recursive=True)
            all_files.extend(files)
        else:
            # ignore non-directories; you may log or collect errors here
            pass

    # dedupe using resolved absolute paths
    unique = []
    seen = set()
    for f in all_files:
        key = Path(f).resolve()
        if key not in seen:
            seen.add(key)
            unique.append(Path(f))

    for md in unique:
        if OUTPUT_DIR:
            # preserve structure relative to the first matching root directory
            # simplest approach: use source file name under OUTPUT_DIR
            out = Path(OUTPUT_DIR) / md.name
            out = out.with_suffix('.pdf')
            out.parent.mkdir(parents=True, exist_ok=True)
            out_path = str(out)
        else:
            out_path = str(md.with_suffix('.pdf'))

        conv.convert_file(
            markdown_file_path=str(md),
            output_pdf_path=out_path,
            theme=DEFAULT_THEME,
            custom_css=CUSTOM_CSS,
            custom_css_file=CUSTOM_CSS_FILE,
        )

if __name__ == '__main__':
    main()
```

### Step-by-Step Plan

- Preparation
  - Ensure system dependencies for WeasyPrint are installed (see README).
  - Run `pip install -r requirements.txt` in `md-to-pdf-converter`.

- Author Inputs
  - Create `md-to-pdf-converter/md_dirs.txt` and add one directory path per line.
  - Use `#` for comments; keep lines empty to ignore.

- Script Setup
  - Create `md-to-pdf-converter/batch_from_dirs.py` with the outline above.
  - Optionally set `DEFAULT_THEME`, `OUTPUT_DIR`, `CUSTOM_CSS_FILE`, `CUSTOM_CSS` at the top.

- Execution
  - From `md-to-pdf-converter/`, run `python batch_from_dirs.py`.
  - The script scans all listed directories recursively and converts every `.md` and `.markdown` file found.

- Output
  - PDFs are written next to source files by default.
  - If `OUTPUT_DIR` is set, PDFs are centralized under that directory. To preserve full relative structure, extend the script to compute each file’s path relative to its listed directory root and join it under `OUTPUT_DIR` before converting.

- Validation
  - Start with a small `md_dirs.txt` listing one directory containing a few markdown files.
  - Confirm PDFs are produced and open correctly.
  - If issues occur, verify directory paths, WeasyPrint system setup, and Python dependencies.

### Notes

- For more advanced structure preservation, replace the simple filename-based output with:
  - Compute `relative_path = md.relative_to(dir_root)` for each listed root.
  - Then `output_file = Path(OUTPUT_DIR) / relative_path.with_suffix('.pdf')` and ensure `output_file.parent.mkdir(parents=True, exist_ok=True)`.
- Themes available can be listed with `python main.py themes`.
- You can adapt this into a CLI command later (e.g., `python main.py list-dirs md_dirs.txt`).
