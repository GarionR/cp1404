from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
current_taxi = None
bill = 0.0

print("Let's drive!")
print(MENU)
user_choice = input(">>> ").lower()
while user_choice != "q":
    if user_choice == "c":
        print("Taxis available:")
        for index, taxi in enumerate(taxis):
            print("{} - {}".format(index, taxi))

        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    elif user_choice == "d":
        if current_taxi is None:
            print("Choose a taxi first")
        else:
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            new_bill = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, new_bill))
            bill += new_bill
    else:
        print("Invalid choice")

    print("Bill to date: ${:.2f}".format(bill))
    print(MENU)
    user_choice = input(">>> ").lower()

print("Total trip cost: ${:.2f}".format(bill))
print("Taxis are now:")
for index, taxi in enumerate(taxis):
    print("{} - {}".format(index, taxi))
