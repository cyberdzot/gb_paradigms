def contains_char_in_digits(string):
    """Проверка строки на то, что в ней по мимо цифр есть символы."""
    for char in string:
        if not char.isdigit():
            return True
    return False
