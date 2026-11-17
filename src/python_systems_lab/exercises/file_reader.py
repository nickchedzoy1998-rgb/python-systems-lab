from pathlib import Path

def read_text_file(path: Path) -> str:
    with open(path, encoding='utf-8') as file:
        contents = file.read()

    return contents