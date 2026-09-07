# Next

Refactor the duplicated CSV/JSON happy-path tests using `pytest.mark.parametrize` and a typed callable.

Requirements:
- combine `test_discover_csv_files()` and `test_discover_json_files()` into one parametrized test
- parameterize over the discovery function and expected extension
- annotate the discovery-function parameter with `Callable[[Path], list[Path]]`
- import `Callable` from `collections.abc`
- keep the non-recursive and `.json`-directory edge-case tests separate
- do not change production code
- run `pytest` and make sure all tests pass
- write the refactor manually
