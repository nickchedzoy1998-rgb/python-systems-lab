import pytest

from python_systems_lab.exercises.database_config import parse_database_config

def test_parse_database_config() -> None:
    assert parse_database_config({
        "host": "localhost",
        "port": 5432,
        "database": "app",
    }) == {
        "host": "localhost",
        "port": 5432,
        "database": "app"}

def test_parse_database_config_missing_host() -> None:
    with pytest.raises(ValueError):
        parse_database_config({
            "port": 5432,
            "database": "app",
        })

def test_parse_database_config_port_low() -> None:
    with pytest.raises(ValueError):
        parse_database_config({
        "host": "localhost",
        "port": '5432',
        "database": "app"
    })

def test_parse_database_config_port_bool() -> None:
    with pytest.raises(TypeError):
        parse_database_config({
        "host": "localhost",
        "port": True,
        "database": "app"
    })

def test_parse_database_config_port_zero() -> None:
    with pytest.raises(ValueError):
        parse_database_config({
        "host": "localhost",
        "port": 0,
        "database": "app"
    })

def test_parse_database_config_port_high() -> None:
    with pytest.raises(ValueError):
        parse_database_config({
        "host": "localhost",
        "port": 65536,
        "database": "app"
    })

def test_parse_database_config_blank_database() -> None:
    with pytest.raises(ValueError):
        parse_database_config({
        "host": "localhost",
        "port": 65535,
        "database": " "
    })

def test_unmodified_parser() -> None:
    config = {
            "host": "localhost",
            "port": 5432,
            "database": "app"
        }

    original_config = config.copy()

    database_config = parse_database_config(original_config)

    assert original_config is not database_config 
    assert config == original_config



