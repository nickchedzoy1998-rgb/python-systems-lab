from pathlib import Path
import pytest
import logging

from python_systems_lab.exercises.file_processor import process_text_file

def test_successful_processor(tmp_path: Path) -> None:
    file_path = tmp_path / 'HelloWorld.txt'

    with file_path.open('w', encoding='utf-8') as f:
        content = 'Hello world'
        f.write(content)

    assert process_text_file(file_path) == 11

def test_non_existent_processor(tmp_path: Path) -> None:
    file_path = tmp_path / 'HelloWorld.txt'

    with pytest.raises(FileNotFoundError):
        process_text_file(file_path)

def test_process_text_file_logs_success(
    tmp_path: Path,
    caplog: pytest.LogCaptureFixture,
) -> None:
    file_path = tmp_path / 'HelloWorldFile.txt'

    with file_path.open('w', encoding='utf-8') as f:
        content = 'Hello world'
        f.write(content)

    caplog.set_level(logging.INFO)

    character_count = process_text_file(file_path)

    assert file_path.name in caplog.text
    assert str(character_count) in caplog.text



# Create a temporary file containing "Hello world".
# Set the capture level to logging.INFO.
# Call process_text_file().
# Assert that the captured logs contain the filename.
# Assert that the captured logs contain the character count (11).