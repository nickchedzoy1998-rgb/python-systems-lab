import pytest

from src.python_systems_lab.database_config import parse_database_config

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
        "port": 65536,
        "database": " "
    })


# with pytest.raises(ValueError):
    
# Write tests for the following scenarios:
# Scenario	Expected
# All three fields valid	Return the validated dictionary
# host missing	ValueError
# port is "5432"	ValueError
# port is True	ValueError
# port is 0	ValueError
# port is 65536	ValueError
# database is "   "	ValueError

# For invalid inputs, use: