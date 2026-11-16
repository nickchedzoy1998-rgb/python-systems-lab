from pathlib import Path
import csv
import pytest

from python_systems_lab.reliable_data_pipeline.csv_reader import read_csv, validate_csv_row

def test_read_csv(tmp_path: Path) -> None:
    file_path = tmp_path / 'TestFile.csv'

    data = [
        {"customer_id": "C1", "amount": "12.50"},
        {"customer_id": "C2", "amount": "9.00"}
    ]

    headers = [key for key in data[0].keys()]

    with file_path.open(mode='w', encoding='utf-8', newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    assert read_csv(file_path) == data

def test_read_non_existent_csv(tmp_path: Path) -> None:
    file_path = tmp_path / 'TestFile.csv'

    with pytest.raises(FileNotFoundError):
        read_csv(file_path)

def test_read_csv_field_has_quoted_comma(tmp_path: Path) -> None:
    file_path = tmp_path / 'TestFile.csv'

    data = [
        {"customer_id": "C1", "amount": "12.50"},
        {"customer_id": "C2", "amount": "9.00"},
        {"customer_id": "C3, C4", "amount": "9,00"},
    ]

    headers = [key for key in data[0].keys()]

    with file_path.open(mode='w', encoding='utf-8', newline="") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(data)

    rows = read_csv(file_path)

    assert rows[2]['customer_id'] == "C3, C4"
    assert rows[2]['amount'] == "9,00"

def test_validate_csv_row_accepts_valid_amount() -> None:
    row = {"customer_id": "C1", "amount": "12.50"}

    assert validate_csv_row(row=row) == None

def test_validate_csv_row_rejects_negative_amount() -> None:
    row = {"customer_id": "C1", "amount": "-5.00"}

    with pytest.raises(ValueError):
        validate_csv_row(row=row)




