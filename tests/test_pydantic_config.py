import pytest
from pydantic import ValidationError
import json

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

def test_max_port() -> None:
    config = DatabaseConfig(
        host='localhost',
        port=65535,
        database="app",
    )

    assert config.port == 65535

def test_over_max_port() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host='localhost',
            port=65536,
            database="app",
        )

def test_empty_host() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host = "",
            port = 87,
            database="app",
        )

def test_whitespace() -> None:
    with pytest.raises(ValidationError):
        DatabaseConfig(
            host = "host",
            port = 87,
            database="   ",
        )

def test_preserve_whitespace() -> None:
    config = DatabaseConfig(
        host = "Host Name is Local Host",
        port = 87,
        database="app",
    )

    assert config.host == "Host Name is Local Host"

raw = {
    "host":"localhost",
    "port":5432,
    "database":"app",
}

config = DatabaseConfig.model_validate(raw)

def test_model_dump_returns_expected_dictionary() -> None:
    dumped = config.model_dump()

    assert dumped == raw

def test_config_json() -> None:
    dumped = config.model_dump_json()
    parsed = json.loads(dumped)

    assert parsed == raw

