import math

TITLE = "Number Sequences"
MENU = "(E)ven number from x to y\n(O)dd numbers from x to y\n(S)quares from x to y\n(Q)uit"

print(TITLE)
print(MENU)
menu_choice = input(">>>").lower()
while menu_choice != "q":
    if menu_choice in "eos":
        start_number = int(input("x = "))
        end_number = int(input("y = "))
        if menu_choice == "e":
            if (start_number % 2) != 0:
                start_number += 1
            for number in range(start_number, end_number, 2):
                print(number)
        elif menu_choice == "o":
            if (start_number % 2) == 0:
                start_number += 1
            for number in range(start_number, end_number, 2):
                print(number)
        elif menu_choice == "s":
            for number in range(start_number, end_number):
                root = math.sqrt(number)
                if int(root + 0.5) ** 2 == number:
                    print(number)
    else:
        print("Invalid choice")

    print(MENU)
    menu_choice = input(">>>").lower()
print("Goodbye!")
