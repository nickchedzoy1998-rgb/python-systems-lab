from collections.abc import Sequence
from pathlib import Path
from collections import Counter

def count_files_by_extension(paths: Sequence[Path]) -> dict[str, int]:
    suffix_list = []

    for path in paths:
        suffix_list.extend(item.suffix for item in path.iterdir() if item.is_file())

    return dict(Counter(suffix_list))