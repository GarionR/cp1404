# Task 1
name = input("Your name: ")
name_file = open("name.txt", "w")
print(name, file=name_file)
name_file.close()

# Task 2
name_file = open("name.txt", "r")
name = name_file.read()
name_file.close()
print("Your name is {}".format(name))

# Task 3
number_file = open("numbers.txt", "r")
numbers = number_file.readlines()
number_file.close()
print(int(numbers[0]) + int(numbers[1]))

# Task 4
number_file = open("numbers.txt", "r")
numbers = number_file.readlines()
number_file.close()
total = 0
for number in numbers:
    total += int(number)

print(total)
