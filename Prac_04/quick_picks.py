import random
LOWEST_NUMBER = 1
HIGHEST_NUMBER = 45
NUMBER_OF_NUMBERS_IN_QUICK_PICK = 6


quick_pick_count = int(input("How many quick picks? "))
for i in range(quick_pick_count):
    quick_pick = []
    while len(quick_pick) < NUMBER_OF_NUMBERS_IN_QUICK_PICK:
        number = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    for number in quick_pick:
        print("{:>2} ".format(number), end="")
    print()
