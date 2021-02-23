def transform(legacy_data):
    return {char.lower(): value for value, chars in legacy_data.items() for char in chars}
