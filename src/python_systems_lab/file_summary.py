from collections.abc import Sequence
from pathlib import Path
from collections import Counter

def count_files_by_extension(paths: Sequence[Path]) -> dict[str, int]:

    suffixes = [path.suffix for path in paths if path.suffix]

    return dict(Counter(suffixes))