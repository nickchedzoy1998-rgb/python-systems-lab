from pathlib import Path
from typing import Literal
import pytest

from python_systems_lab.file_discovery import discover_csv_files, discover_json_files, discover_files

file_names = [
    'file_1.txt', 'file_2.csv', 'file_3', 'file_4.csv', 'file_5.xlsx', 'file_6.csv', 'file_7.csv', 'file_8.xlsx', 'file_9.csv', 'file_10.pdf',
    'file_11.json', 'file_12.json'
    ]

allowed_file_types = set([Path(file).suffix for file in file_names if len(str(file).split(".")) > 1])

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

def test_prove_file_discovery_non_recursive(tmp_path: Path) -> None:
    nested_dir = tmp_path / nested_dir_name

    nested_dir.mkdir()
    csv_filepath = nested_dir / csv_filename
    csv_filepath.touch()

    discovery_result = discover_csv_files(tmp_path)

    assert csv_filepath not in discovery_result


def test_discover_json_files(tmp_path: Path) -> None:
    expected_files = [j for j in file_names if Path(j).suffix == '.json']

    for f in file_names:
        f_path = tmp_path / f

        f_path.touch()

    result = discover_json_files(tmp_path)

    result_file_names = [f.name for f in result]

    assert set(expected_files) == set(result_file_names)


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

@pytest.mark.parametrize("file_type", list(allowed_file_types))
def test_discover_files(tmp_path: Path, file_type: 'str') -> None:
    expected_files = [file for file in file_names if Path(file).suffix == file_type]

    for file in file_names:
        file_path = tmp_path / file
        file_path.touch()

    found_files = discover_files(tmp_path, file_type=file_type)

    found_file_names = [file.name for file in found_files]

    assert set(expected_files) == set(found_file_names) and file_type in allowed_file_types



