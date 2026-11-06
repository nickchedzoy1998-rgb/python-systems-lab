from pathlib import Path
import pytest

from src.python_systems_lab.file_reader import read_text_file

def test_existing_file(tmp_path: Path) -> None:

    with tmp_path.open('w', encoding='utf-8') as f:
        content = 'Welcome to my file.'
        f.write(content)

    assert read_text_file(tmp_path) == 'Welcome to my file.'

def test_non_existing_path() -> None:
    tmp_path = Path('My Documents')

    with pytest.raises(FileNotFoundError):
        read_text_file(tmp_path)





# Existing file: Use tmp_path to create a UTF-8 file and verify that your function returns its contents exactly.
# Missing file: Pass a nonexistent path and verify that FileNotFoundError is raised.
def test_create_utf8_file_with_open(tmp_path):
    file_path = tmp_path / "example.txt"
    
    with file_path.open("w", encoding="utf-8") as f:
        f.write("Line 1: 🌟\n")
        f.write("Line 2: ñoñó\n")
        
    assert file_path.exists()