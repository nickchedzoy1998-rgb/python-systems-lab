def sum_numbers(*numbers: int) -> int:
    result = 0

    for num in numbers:
        result += num

    return result

def show_settings(**kwargs: object) -> None:
    print(kwargs)

def filter_settings(**settings: object) -> dict[str, object]:
    return {setting: value for setting, value in settings.items() if value is not None}



if __name__ == '__main__':
    settings = {
        "host": "localhost",
        "port": 5432,
    }

    # print(filter_settings(settings))
    print(filter_settings(**settings))
