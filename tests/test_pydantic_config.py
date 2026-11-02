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

def test_zero_port() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host='localhost',
            port=0,
            database="app",
        )

def test_one_port() -> None:
    config = DatabaseConfig(
        host='localhost',
        port=1,
        database="app",
    )

    assert config.port == 1

def test_65535_port() -> None:
    config = DatabaseConfig(
        host='localhost',
        port=65535,
        database="app",
    )

    assert config.port == 65535

def test_high_port() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host='localhost',
            port=65536,
            database="app",
        )