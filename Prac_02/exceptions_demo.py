"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? when a value that can't be converted to int is input
2. When will a ZeroDivisionError occur? when the denominator is zero in the math
3. Could you change the code to avoid the possibility of a ZeroDivisionError? yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while not denominator:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
