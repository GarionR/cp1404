from Prac_08.unreliable_car import UnreliableCar

car_1 = UnreliableCar("My Car", 1000, 50)
print(car_1.drive(100))

car_2 = UnreliableCar(fuel=1000, reliability=10)
print(car_2.drive(10))
