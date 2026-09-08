# Next

Align the project Python version with the interpreter actually running the tests.

Requirements:
- run `python --version` inside the activated virtual environment
- compare it with `requires-python` in `pyproject.toml`
- decide whether the project should target Python 3.11 or Python 3.12+
- make exactly one of these true: either recreate the venv with a compatible Python version, or change `requires-python` to match the intended supported version
- do not change application code
- run `pytest` afterwards and make sure all tests still pass
- be ready to explain what `requires-python` means and why a mismatch matters
