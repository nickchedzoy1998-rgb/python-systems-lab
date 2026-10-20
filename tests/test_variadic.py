from src.python_systems_lab.variadic import sum_numbers

def test_sum_numbers_1(*numbers: int) -> None:
    assert sum_numbers(2,3) == 5

def test_sum_numbers_2(*numbers: int) -> None:
    assert sum_numbers(1,2,3,4) == 10

def test_sum_numbers_3(*numbers: int) -> None:
    assert sum_numbers() == 0

def test_sum_numbers_4(*numbers: int) -> None:
    assert sum_numbers(-5,2,1) == -2

