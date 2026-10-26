def normalize_value(value: int | float | str | bool | None) -> str:
    if value is None:
        return ""
    
    if isinstance(value, (bool, int, float)):
        return str(value)

    return value.strip()