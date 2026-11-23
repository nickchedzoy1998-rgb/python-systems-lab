import subprocess
import sys

def test_cli_rejects_invalid_csv() -> None:
    # Execute CLI
    result = subprocess.run(
        [sys.executable, "-m", "python_systems_lab.guided_integrations.csv_cli.cli", "TestFiles/test_file.csv"],
        capture_output=True,
        text=True
    )

    assert result.stdout == ''
    assert result.stderr == 'Amount must be a valid decimal number\n'
    assert result.returncode == 1
    print(repr(result.stderr))