# Next

## Guided learning · CLI process testing

The current `python_systems_lab.guided_integrations.csv_cli` package is a
guided integration build. It is helping practise file handling, validation,
testing, CLI arguments, stdout, stderr and exit codes. It is **not P01 project
progress**.

**One ten-minute task:** create
`tests/guided_integrations/csv_cli/test_cli.py` and add a test function named
`test_cli_rejects_invalid_csv`.

Inside the test, use `subprocess.run()` to execute this module:

`python_systems_lab.guided_integrations.csv_cli.cli`

Run it against:

`examples/guided_csv_cli/invalid_transactions.csv`

Pass the command as a list, use `sys.executable`, `capture_output=True` and
`text=True`.

For this task, print only:

- `result.returncode`
- `result.stderr`

Run:

```bash
pytest -s tests/guided_integrations/csv_cli/test_cli.py
```

**Done when:** the test run shows exit code `1` and the validation message in
stderr. Stop before adding assertions; the purpose of this slice is to observe
the child-process boundary first.

After the remaining CLI/process-testing lessons and a short mixed readiness
check, P01 will begin as a separate program built from a written specification.
