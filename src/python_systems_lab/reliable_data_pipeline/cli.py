from argparse import ArgumentParser
from pathlib import Path

from python_systems_lab.reliable_data_pipeline.csv_reader import csv_writer, load_validated_csv

def main() -> str:
    parser = ArgumentParser(description='Process csv with CLI')
    parser.add_argument('file_path')
    args = parser.parse_args()

    filename = args.file_path
    file_path = Path(filename)

    validated_rows = load_validated_csv(path = file_path)
    validated_row_count = len(validated_rows)

    return f'Successfully validated and loaded {validated_row_count} rows.'

if __name__ == '__main__':
    transactions_data = [
    {"customer_id": "C1", "amount": "12.50"},
    {"customer_id": "C2", "amount": "9.00"},
    {"customer_id": "C3", "amount": "15.75"},
]

    csv_writer(folder_name='Test Files', file_name='transactions.csv', data=transactions_data)    

    print(main())