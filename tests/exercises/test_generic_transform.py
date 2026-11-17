from python_systems_lab.exercises.generic_transform import transform_items

# Helper Functions:
def convert_int_to_str(num: int) -> str:
    return str(num)

def calc_str_length(word: str) -> int:
    return len(word)

def divide_by_two(num: int) -> float:
    return num / 2

# Tests
def test_transform_items_int_to_str() -> None:
    assert transform_items([1,2,3], convert_int_to_str) == ["1", "2", "3"]

def test_transform_string_length() -> None:
    assert transform_items(["cat", "elephant"], calc_str_length) == [3, 8]

def test_transform_div_two() -> None:
    assert transform_items([2,4,6], divide_by_two) == [1.0, 2.0, 3.0]

def test_transform_items_empty_input() -> None:
    assert transform_items([], calc_str_length) == []   
