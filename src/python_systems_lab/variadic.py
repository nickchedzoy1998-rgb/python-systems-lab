def sum_numbers(*numbers: int) -> int:
    result = 0

    for num in numbers:
        result += num

    return result

def show_settings(**kwargs: object) -> None:
    print(kwargs)

def filter_settings(**settings: object) -> dict[str: object]:
    return {setting: obj for setting, obj in settings.items() if obj is not None}



# if __name__ == '__main__':
