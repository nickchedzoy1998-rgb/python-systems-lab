import sys
import subprocess
import os
from pathlib import Path

result = subprocess.run(
    [sys.executable, "-m", "python_systems_lab.guided_integrations.csv_cli.cli", "TestFiles/transactions.csv"],
    capture_output=True,
    text=True
)

print(f'stderr: {result.stdout}')
print(f'stdout: {result.stderr}')
print(f'return code: {result.returncode}')

print("Parent working directory:", Path.cwd())
print("Resolved CSV path:", Path("TestFiles/transactions.csv").resolve())
print("CSV exists:", Path("TestFiles/transactions.csv").is_file())