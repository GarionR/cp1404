from Prac_06.guitar import Guitar

guitars = []

print("My guitars!")

name = input("Name: ")
while name:
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print("{} ({}) : ${:,.2f} added.".format(name, year, cost))

    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))  # for testing purposes
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))  # for testing purposes

print()

print("These are my guitars:")
longest_name = ""
for guitar in guitars:
    if len(guitar.name) > len(longest_name):
        longest_name = guitar.name

for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print("Guitar {}: {:<{}} ({}), worth ${:10,.2f}{}".format(i, guitar.name, len(longest_name), guitar.year,
                                                              guitar.cost, vintage_string))
