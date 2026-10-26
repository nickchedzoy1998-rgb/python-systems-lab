from collections.abc import Callable, Iterable

def double(number: int) -> int:
    return number * 2

def square(number: int) -> int:
    return number * number

def add_ten(number: int) -> int:
    return number + 10

def transform_numbers(
    numbers: Iterable[int],
    transform: Callable[[int], int],
) -> list[int]:
    
    return [transform(num) for num in numbers]
    

