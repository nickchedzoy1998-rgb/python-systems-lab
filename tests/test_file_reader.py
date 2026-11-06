from pathlib import Path
import pytest

from src.python_systems_lab.file_reader import read_text_file

def test_existing_file(tmp_path: Path) -> None:
    file_path = tmp_path / 'example_file.txt'

    with file_path.open('w', encoding='utf-8') as f:
        content = 'Welcome to my file.'
        f.write(content)

    assert read_text_file(file_path) == content

def test_non_existing_path(tmp_path: Path) -> None:
    file_path = tmp_path / 'example_file.txt'

    with pytest.raises(FileNotFoundError):
        read_text_file(file_path)

def test_file_closed_after_with(tmp_path: Path) -> None:
    file_path = tmp_path / 'example_file.txt'

    with file_path.open('w', encoding='utf-8') as f:
        content = 'My File'
        f.write(content)
        assert not f.closed

    assert f.closed
