from collections.abc import Callable, Iterable

def transform_numbers(
    numbers: Iterable[int],
    transform: Callable[[int], int],
) -> list[int]:
    
    return [transform(num) for num in numbers]
    

