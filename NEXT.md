# Next

Tighten the non-recursive discovery test.

Requirements:
- change the test return annotation from `-> bool` to `-> None` (or remove it)
- assert directly that `csv_filepath` is not in `discovery_result`
- run `pytest` and make sure all tests pass
- write the changes manually

Do not change `discover_csv_files()`.
