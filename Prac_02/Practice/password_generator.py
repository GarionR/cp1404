

MAX_LENGTH = 100
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    pass


def is_valid_password(password, min_length):
    """Determine if the provided password is valid."""
    if not min_length < len(password) < MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if not count_lower or not count_upper or not count_digit:
        return False

    if not count_special and SPECIAL_CHARS_REQUIRED:
        return False

    return True


main()