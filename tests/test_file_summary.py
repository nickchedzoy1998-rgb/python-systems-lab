from pathlib import Path

from src.python_systems_lab.file_summary import count_files_by_extension


paths = (
    Path("sales.csv"),
    Path("customers.csv"),
    Path("settings.json"),
    Path("profiles.json"),
    Path("events.json"),
    Path("README"),
)


def test_count_files_by_extension() -> None:
    extension_counts = count_files_by_extension(paths)

    expected_result = {
        ".csv": 2,
        ".json": 3,
    }

    assert extension_counts == expected_result


def test_count_files_by_extension_empty_input() -> None:
    paths = ()
    extension_counts = count_files_by_extension(paths)

    expected_result = {}

    assert extension_counts == expected_result


def test_count_files_by_extension_generator():
    files = [
        ('file_1.csv'),
        ('file_2.csv'),
        ('file_3.json')
    ]
    
    paths = (Path(file) for file in files)

    expected_result = {".csv": 2, ".json": 1}

    assert expected_result == count_files_by_extension(paths)

