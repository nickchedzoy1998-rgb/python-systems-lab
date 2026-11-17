from argparse import ArgumentParser
from pathlib import Path
import sys

from python_systems_lab.guided_integrations.csv_cli.csv_reader import load_validated_csv

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
    try:
        print(main())
        
    except ValueError as e:
        print(e, file=sys.stderr)
        raise SystemExit(1)