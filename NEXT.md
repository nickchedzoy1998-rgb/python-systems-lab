# Next

Clean up `tests/test_file_discovery.py` without changing behaviour.

Requirements:
- remove the unused `pytest` import
- import `discover_csv_files` from `python_systems_lab.file_discovery` rather than through `src`
- add `-> None` return annotations to both test functions
- keep the existing test logic unchanged
- run `pytest` and make sure all tests pass
- write the changes manually
