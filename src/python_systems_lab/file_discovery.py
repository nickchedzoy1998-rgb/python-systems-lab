from pathlib import Path

def discover_csv_files(directory: Path) -> list[Path]:
    return _discover_files(directory=directory, extension='.csv')

def discover_json_files(directory: Path) -> list[Path]:
    return _discover_files(directory=directory, extension='.json')

def _discover_files(directory: Path, extension: str) -> list[Path]:
    return [path for path in directory.glob(f'*{extension}') if path.is_file()]
    