UPPER_LIMIT = 127
LOWER_LIMIT = 33

char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
ascii_value = int(input("Enter a number between {} and {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))
while not LOWER_LIMIT < ascii_value < UPPER_LIMIT:
    print("Invalid!")
    ascii_value = int(input("Enter a number between {} and {}: ".format(LOWER_LIMIT, UPPER_LIMIT)))

print("The character for {} is {}".format(ascii_value, chr(ascii_value)))

for ascii_value in range(LOWER_LIMIT, UPPER_LIMIT):
    print(f"{ascii_value:>3} {chr(ascii_value):>2}")

number_of_columns = int(input("How many columns? "))

for ascii_value in range(LOWER_LIMIT, UPPER_LIMIT, number_of_columns):
    for i in range(number_of_columns):
        print_value = ascii_value + i
        print(f"{print_value:>3} {chr(print_value):>2}", end="\t\t")
    print()
