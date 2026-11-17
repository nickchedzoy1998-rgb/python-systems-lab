from collections.abc import Iterable
from pathlib import Path
from collections import Counter

def count_files_by_extension(paths: Iterable[Path]) -> dict[str, int]:

    suffixes = [path.suffix for path in paths if path.suffix]

    return dict(Counter(suffixes))