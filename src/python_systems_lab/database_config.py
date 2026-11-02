from typing import TypedDict
from collections.abc import Mapping

class DatabaseConfig(TypedDict):
    host: str
    port: int
    database: str

def parse_database_config(
    raw: Mapping[str, object],
) -> DatabaseConfig:
    
    host = raw.get('host')
    port = raw.get('port')
    database = raw.get('database')

    if not all(isinstance(key, str) and key.strip() != '' for key in (host, database)):
        raise ValueError("Host and database must be non-empty strings!")

    if not isinstance(port, int) or port < 1 or port > 65535:
        raise ValueError('Port must be an integer between 1 and 65535')

    if isinstance(port, bool):
        raise TypeError('Port must not be boolean')

    return DatabaseConfig(
        host=host,
        port=port,
        database=database
    )

if __name__ == '__main__':
    print(parse_database_config({
    "host": "localhost",
    "port": 5432,
    "database": "app",
}))