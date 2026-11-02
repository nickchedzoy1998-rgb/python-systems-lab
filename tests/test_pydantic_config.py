import pytest
from pydantic import ValidationError

from src.python_systems_lab.pydantic_config import DatabaseConfig

def test_valid_integer() -> None:
    config = DatabaseConfig(
        host='host',
        port=5432,
        database='database'
)
    assert isinstance(config, DatabaseConfig)
    assert config.port == 5432

def test_numeric_string() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host='host',
            port="5432",
            database='database'
    )

def test_invalid_string() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host='host',
            port="notanumber",
            database='database'
    )

def test_boolean_port_true() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host="localhost",
            port=True,
            database="app",
        )

def test_boolean_port_false() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host="localhost",
            port=False,
            database="app",
        )
