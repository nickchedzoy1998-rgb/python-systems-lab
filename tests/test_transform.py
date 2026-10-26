from src.python_systems_lab.transform import transform_numbers, double, square, add_ten

def test_transform_double_list() -> None:
    assert transform_numbers([1,2,3], double) == [2,4,6]

def test_transform_square_tuple() -> None:
    assert transform_numbers((1, 2, 3), square) == [1, 4, 9]

def test_transform_double_empty_list() -> None:
    assert transform_numbers([], double) == []

def test_add_10() -> None:
    def generate_123():
        yield 1
        yield 2
        yield 3

    assert(transform_numbers(generate_123(), add_ten)) == [11, 12, 13]
