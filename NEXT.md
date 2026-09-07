# Next

Add one test proving `discover_json_files()` excludes directories whose names end in `.json`.

Requirements:
- create a real top-level JSON file in `tmp_path`
- create a directory in `tmp_path` whose name also ends in `.json`
- call `discover_json_files(tmp_path)`
- assert the real JSON file is returned
- assert the `.json` directory is not returned
- do not change `discover_json_files()` unless the test reveals a bug
- run `pytest` and make sure all tests pass
- write the test manually
