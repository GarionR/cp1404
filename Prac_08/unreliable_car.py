"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from Prac_08.car import Car
import random


class UnreliableCar(Car):
    """Represent UnreliableCar Object"""

    def __init__(self, name="", fuel=0, reliability=50.0):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the UnreliableCar a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        If a random number between 0 and 100 is above reliability UnreliableCar
        drives a distance of 0
        """
        if self.reliability > random.randint(0, 100):
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
