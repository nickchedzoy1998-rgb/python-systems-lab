# Next

Add a small typed file-summary function using `Sequence`.

Implement `count_files_by_extension(paths: Sequence[Path]) -> dict[str, int]` in a new `src/python_systems_lab/file_summary.py` module.

Requirements:
- write the test first in `tests/test_file_summary.py`
- make the test pass a tuple of `Path` objects, not a list
- include repeated `.csv` and `.json` suffixes plus one path with no suffix
- expect suffixes such as `.csv` and `.json` to map to their counts
- ignore paths with no suffix
- import `Sequence` from `collections.abc`
- do not mutate the input
- run the test once before implementation to see the expected red state, then implement manually and run `pytest` again
- be ready to explain why `Sequence[Path]` is a more flexible input type here than `list[Path]`
