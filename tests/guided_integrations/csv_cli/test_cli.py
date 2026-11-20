import subprocess
import sys
from pathlib import Path

from src.python_systems_lab.guided_integrations.csv_cli.cli import main
from src.python_systems_lab.guided_integrations.csv_cli.csv_reader import csv_writer

def test_cli_invalid_csv_error_exit(tmp_path: Path) -> None:
    file_path = tmp_path / 'example_file.csv'

    data = [
        {"customer_id": "C1", "amount": "12.50"},
        {"customer_id": "C2", "amount": "9.00"},
        {"customer_id": "C3", "amount": "not_a_number"}, 
    ]

    # Create the csv:
    csv_writer(folder_name=tmp_path.name, file_name='example_file.csv', data=data)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "python_systems_lab.guided_integrations.csv_cli.cli",
            str(file_path),
        ],
        capture_output=True,
        text=True
    )


    