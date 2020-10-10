"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from Prac_08.car import Car
import random


class UnreliableCar(Car):
    """Represent UnreliableCar Object"""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability > random.randint(0, 100):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
