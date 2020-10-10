from Prac_08.silver_service_taxi import SilverServiceTaxi

taxi_1 = SilverServiceTaxi("Hummer", 200, 4)
print(taxi_1)
taxi_2 = SilverServiceTaxi("My Taxi", 1000, 2)
print(taxi_2.drive(18))
print("Fare = ${:.2f}".format(taxi_2.get_fare()))
