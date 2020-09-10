from Prac_06.guitar import Guitar

guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar_2 = Guitar("Another Guitar", 2013)

print("{} get_age() - Expected 98. Got {}".format(guitar_1.name, guitar_1.get_age()))
print("{} get_age() - Expected 7. Got {}".format(guitar_2.name, guitar_2.get_age()))

print("{} is_vintage() - Expected True. Got {}".format(guitar_1.name, guitar_1.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(guitar_2.name, guitar_2.is_vintage()))
