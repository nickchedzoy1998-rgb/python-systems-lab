from src.python_systems_lab.variadic import sum_numbers, filter_settings

def test_sum_numbers_1() -> None:
    assert sum_numbers(2,3) == 5

def test_sum_numbers_2() -> None:
    assert sum_numbers(1,2,3,4) == 10

def test_sum_numbers_3() -> None:
    assert sum_numbers() == 0

def test_sum_numbers_4() -> None:
    assert sum_numbers(-5,2,1) == -2

def test_filter_settings() -> None:
    assert filter_settings(
        host="localhost",
        port=5432,
        password=None,
        debug=False,
    ) == {
        "host": "localhost",
        "port": 5432,
        "debug": False,
    }

def test_filter_settings_empty_input() -> None:
    assert filter_settings() == {}

def test_filter_settings_preserves_falsy_values() -> None:
        assert filter_settings(
        host=False,
        port=0,
        password="",
        debug=True,
    ) == {
        "host": False,
        "port": 0,
        "password": "",
        "debug": True,
    }