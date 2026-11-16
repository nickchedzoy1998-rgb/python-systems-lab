from pathlib import Path
from collections.abc import Iterable
import csv
import logging
from decimal import Decimal, InvalidOperation


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

