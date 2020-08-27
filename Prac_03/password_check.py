MINIMUM_LENGTH = 5


def main():
    password = get_password()

    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password


main()
