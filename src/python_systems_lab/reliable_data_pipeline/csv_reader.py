from pathlib import Path
from collections.abc import Iterable
import csv

def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(mode='r', encoding='utf-8', newline="") as f:
        reader = csv.DictReader(f)

        return [row for row in reader]