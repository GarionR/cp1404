"""
CP1404 - Task 3
using loops
"""

for i in range(1, 21, 2):
    print(i, end=" ")
print()

for i in range(0, 101, 10):
    print(i, end=" ")
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()

star_count = int(input("Number of stars: "))
for i in range(star_count):
    print("*", end="")
print()

star_count = int(input("Number of stars: "))
for i in range(star_count + 1):
    print("*" * i)


