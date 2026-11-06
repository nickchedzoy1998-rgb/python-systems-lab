from pathlib import Path

def read_text_file(path: Path) -> str:
    with open(path, encoding='utf-8') as file:
        contents = file.read()

    return contents

    


# - Open the file using a with statement.
# - Read its entire contents.
# - Use UTF-8 encoding.
# - Return the contents as a string.
# - Don't catch or suppress exceptions.
# - Ensure the file is closed when the function finishes.
# You can use either open() or Path.open().