# Next

Extract the repeated mixed-file setup into your own pytest fixture.

Requirements:
- create a fixture in `tests/test_file_discovery.py` that creates every entry in `file_names` inside `tmp_path`
- have the fixture return the populated `tmp_path`
- annotate the fixture return type as `Path`
- use the fixture in the parametrized happy-path test and the `.json`-directory exclusion test instead of repeating the file-creation loop
- keep the non-recursive test independent
- remove the now-unused `nested_dir_name` and `csv_filename` globals
- do not change production code
- run `pytest` and make sure all tests pass
- write the refactor manually
