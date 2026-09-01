from pathlib import Path

def discover_csv_files(directory: Path) -> list[Path]:
    return [path for path in directory.glob('*.csv') if path.is_file()]