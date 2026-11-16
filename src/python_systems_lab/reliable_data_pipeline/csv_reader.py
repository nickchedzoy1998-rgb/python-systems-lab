from pathlib import Path
from collections.abc import Iterable
import csv
import logging
from decimal import Decimal, InvalidOperation

def csv_writer(folder_name: str, file_name: str, data: list[dict[str, str]]) -> None:
    folder_path = Path(folder_name)

    if not folder_path.exists():
        folder_path.mkdir(parents=True, exist_ok=True)

    file_path = folder_path / file_name
    headers = [key for key in data[0].keys()]

    with file_path.open(mode='w', encoding='utf-8', newline="") as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(data)

def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(mode='r', encoding='utf-8', newline="") as f:
        reader = csv.DictReader(f)

        return [row for row in reader]

def validate_csv_row(row: dict) -> None:
    customer_id = row.get('customer_id', None)
    amount = row.get('amount', None)
    
    if customer_id is None:
        raise KeyError('Missing Key: customer_id')

    if amount is None:
        raise KeyError('Missing Key: amount')

    if not isinstance(customer_id, str):
        raise ValueError('Customer ID must be string')
    
    if customer_id.strip() == '':
        raise ValueError('Customer must be non-empty')
    
    try:
        converted_amount = Decimal(amount)
    except InvalidOperation:
        raise ValueError("Amount must be a valid decimal number")

    if converted_amount < 0:
        raise ValueError('Amount must be non negative')

def load_validated_csv(path: Path) -> list[dict[str, str]]:
    read_rows = read_csv(path=path)

    for row in read_rows:
        validate_csv_row(row=row)

    return read_rows

    