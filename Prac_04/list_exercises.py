def main():
    # basic_list_operations()
    woefully_inadequate_security_checker()


def basic_list_operations():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Number: ")))
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))


def woefully_inadequate_security_checker():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
