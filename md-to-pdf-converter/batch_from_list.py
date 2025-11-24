from pathlib import Path
import glob
from core.converter import MarkdownToPDFConverter
from core.utils import is_markdown_file, find_markdown_files

LIST_FILE = Path(__file__).parent / 'md_paths.txt'
DEFAULT_THEME = 'default'
OUTPUT_DIR = None
RECURSIVE_DIRECTORIES = True
CUSTOM_CSS_FILE = None
CUSTOM_CSS = None

def iter_specs(list_file: Path):
    for raw in list_file.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        yield line

def expand_spec(spec: str, recursive: bool):
    if any(ch in spec for ch in ['*', '?']):
        paths = [Path(p) for p in glob.glob(spec, recursive=True)]
        return [p for p in paths if p.exists() and is_markdown_file(str(p))]
    p = Path(spec)
    if p.is_dir():
        return find_markdown_files(str(p), recursive=recursive)
    if p.is_file() and is_markdown_file(str(p)):
        return [p]
    return []

def main():
    converter = MarkdownToPDFConverter()
    collected = []
    for spec in iter_specs(LIST_FILE):
        collected.extend(expand_spec(spec, RECURSIVE_DIRECTORIES))
    unique = []
    seen = set()
    for f in collected:
        key = Path(f).resolve()
        if key not in seen:
            seen.add(key)
            unique.append(Path(f))
    success = 0
    fail = 0
    for md in unique:
        try:
            if OUTPUT_DIR:
                out = Path(OUTPUT_DIR) / md.name
                out = out.with_suffix('.pdf')
                out.parent.mkdir(parents=True, exist_ok=True)
                out_path = str(out)
            else:
                out_path = str(md.with_suffix('.pdf'))
            converter.convert_file(
                markdown_file_path=str(md),
                output_pdf_path=out_path,
                theme=DEFAULT_THEME,
                custom_css=CUSTOM_CSS,
                custom_css_file=CUSTOM_CSS_FILE,
            )
            success += 1
        except Exception:
            fail += 1
    print(f"Converted: {success}, Failed: {fail}")

if __name__ == '__main__':
    main()

