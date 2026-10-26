from src.python_systems_lab.value_normalizer import normalize_value

def test_normalize_value_int() -> None:
    assert normalize_value(42) == '42'

def test_normalize_value_float() -> None:
    assert normalize_value(3.5) == '3.5'

def test_normalize_value_str() -> None:
    assert normalize_value(" hello ") == 'hello'

def test_normalize_value_none() -> None:
    assert normalize_value(None) == ''

def test_normalize_value_true() -> None:
    assert normalize_value(True) == 'True'

def test_normalize_value_false() -> None:
    assert normalize_value(False) == "False"