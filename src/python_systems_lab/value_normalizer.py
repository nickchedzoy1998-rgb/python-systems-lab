def normalize_value(value: int | float | str | None) -> str:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)

    if isinstance(value, str):
        return value.strip()

    if value == None:
        return ""

    if value == True:
        return "True"