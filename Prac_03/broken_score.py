"""
CP1404/CP5632 - Practical - Task 2
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    score = random.randint(0, 100)
    result = determine_result(score)
    print(result)


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
