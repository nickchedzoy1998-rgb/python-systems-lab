from collections.abc import Sequence
from pathlib import Path
from collections import Counter

def count_files_by_extension(paths: Sequence[Path]) -> dict[str, int]:

    sfxs = [pth.suffix for pth in paths if pth.suffix]

    return dict(Counter(sfxs))