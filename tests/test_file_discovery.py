from collections.abc import Callable
from pathlib import Path
import pytest

from python_systems_lab.file_discovery import discover_csv_files, discover_json_files

file_names = [
    'file_1.txt', 'file_2.csv', 'file_3', 'file_4.csv', 'file_5.xlsx', 'file_6.csv', 'file_7.csv', 'file_8.xlsx', 'file_9.csv', 'file_10.pdf',
    'file_11.json', 'file_12.json'
    ]


def test_discover_csv_files(tmp_path: Path) -> None:
    expected_files = [csv_f for csv_f in file_names if Path(csv_f).suffix == '.csv']

    for f in file_names:
        file = tmp_path / f

        file.touch()

    result = discover_csv_files(tmp_path)

    result_file_names = [f.name for f in result]

    assert set(result_file_names) == set(expected_files)

nested_dir_name = 'sub_folder' 
csv_filename = 'csv_file_1.csv'

def test_exclude_directory_named_json(tmp_path: Path) -> None:
    directory_name = 'folder_.json'
    json_directory = tmp_path / directory_name

    json_directory.mkdir()

    expected_files = [file for file in file_names if Path(file).suffix == '.json']
    
    for f in file_names:
        f_path = tmp_path / f

        f_path.touch()

    result = discover_json_files(tmp_path)

    result_file_names = [f.name for f in result]

    assert set(expected_files) == set(result_file_names) and directory_name not in result_file_names

@pytest.mark.parametrize(
        'discover_function, extension',
        [(discover_csv_files, '.csv'), (discover_json_files, '.json')])
def test_discover_files(
    discover_function: Callable[[Path], list[Path]], 
    tmp_path: Path, 
    extension: str
) -> None:

    expected_file_names = [file for file in file_names if Path(file).suffix == extension]

    for f in file_names:
        file_path = tmp_path / f
        file_path.touch()
    
    result_file_names = [result_file.name for result_file in discover_function(tmp_path)]

    assert set(expected_file_names) == set(result_file_names)