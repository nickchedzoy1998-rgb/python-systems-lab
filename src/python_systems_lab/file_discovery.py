from pathlib import Path

def discover_csv_files(directory: Path):
    folder = Path(directory)

    return list(folder.glob('*.csv'))