import pytest 
from pathlib import Path

from src.python_systems_lab.file_discovery import discover_csv_files

file_names = [
    'file_1.txt', 'file_2.csv', 'file_3', 'file_4.csv', 'file_5.xlsx', 'file_6.csv', 'file_7.csv', 'file_8.xlsx', 'file_9.csv', 'file_10.pdf'
    ]

def create_test_files(tmp_path: Path, filename: str) -> Path:
    if tmp_path.suffix == '.csv':
        return tmp_path / filename

def main():
    folder_name = 'data'

    for f in file_names:
        f_path = Path(f)

        create_test_files(f_path, f)

    discover_csv_files()