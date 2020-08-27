"""
CP1404 - Task 4
"""

item_count = int(input("Number of items: "))
while item_count < 0:
    print("Invalid number of items!")
    item_count = int(input("Number of items: "))

total = 0
for item in range(item_count):
    total += float(input("Price of item: "))

if total > 100:
    total *= 0.9

print(f"Total price for {item_count} items is ${total:.2f}")
