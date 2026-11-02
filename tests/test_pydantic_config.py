import pytest

from src.python_systems_lab.pydantic_config import DatabaseConfig

def test_valid_integer() -> None:
    with pytest.raises(ValueError):
        DatabaseConfig(
            host='host',
            port=5432,
            database='database'
    )

def test_valid_integer() -> None:
    with pytest.raises(ValueError):
        DatabaseConfig(
            host='host',
            port=5432,
            database='database'
    )

def test_numeric_string() -> None:
    with pytest.raises(ValueError):
        DatabaseConfig(
            host='host',
            port="5432",
            database='database'
    )

def test_invalid_string() -> None:
    with pytest.raises(ValueError):
        DatabaseConfig(
            host='host',
            port="notanumber",
            database='database'
    )