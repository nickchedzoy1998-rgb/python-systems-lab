from pathlib import Path

from src.python_systems_lab.file_discovery import discover_csv_files

file_names = [
    'file_1.txt', 'file_2.csv', 'file_3', 'file_4.csv', 'file_5.xlsx', 'file_6.csv', 'file_7.csv', 'file_8.xlsx', 'file_9.csv', 'file_10.pdf'
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

def test_prove_file_discovery_non_recursive(tmp_path: Path) -> None:
    nested_dir = tmp_path / nested_dir_name

    nested_dir.mkdir()
    csv_filepath = nested_dir / csv_filename
    csv_filepath.touch()

    discovery_result = discover_csv_files(tmp_path)

    assert csv_filepath not in discovery_result    