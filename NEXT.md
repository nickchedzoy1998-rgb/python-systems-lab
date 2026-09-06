# Next

Add JSON file discovery test-first.

Requirements:
- in `tests/test_file_discovery.py`, write one new test for a future `discover_json_files(directory: Path) -> list[Path]`
- create a mix of files in `tmp_path`, including at least two `.json` files and at least two non-JSON files
- assert that only the top-level `.json` files are returned
- do not implement `discover_json_files()` yet
- run `pytest` and confirm the new test fails for the expected reason
- write the test manually
