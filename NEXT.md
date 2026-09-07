# Next

Finish the file-discovery refactor without expanding the public API.

Requirements:
- turn the generalized `discover_files()` idea into a private helper (leading underscore)
- make both `discover_csv_files()` and `discover_json_files()` delegate to that helper
- remove the new public `discover_files()` API
- remove the parametrized test and any imports/data added only for testing that public generalized function
- keep the existing CSV/JSON behaviour tests unchanged
- run `pytest` and make sure all tests pass
- write the refactor manually

Before coding, be able to state: what is shared, and what single value varies between CSV and JSON discovery?
