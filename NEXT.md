# Next

Refactor the duplicated CSV/JSON discovery logic without changing behaviour.

Requirements:
- identify what is identical between `discover_csv_files()` and `discover_json_files()` and what varies
- extract the shared logic into one private helper in `file_discovery.py`
- choose the helper name and parameter names yourself
- keep `discover_csv_files()` and `discover_json_files()` as the public functions
- do not change the tests except if needed for import formatting
- run `pytest` and make sure all tests pass
- write the refactor manually
