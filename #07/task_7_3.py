from __future__ import annotations
from abc import ABC, abstractmethod


'''
    goal1: make incompatible objects adaptable to each other
    goal2: return the compatible object == object
    goal3: set it to adaptee
'''

# Adaptee1


class MotorCycle:

    def __init__(self):
        self.name = "MotorCycle"

    def TwoWheeler(self):
        return "TwoWheeler"


# Adptee2
class Truck:

    def __init__(self):
        self.name = "Truck"

    def EightWheeler(self):
        return "EightWheeler"

 # Adptee3


class Car:

    def __init__(self):
        self.name = 'Car'

    def FourWheeler(self):
        return 'FourWheeler'


class Adapter():

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


""" main method """
if __name__ == "__main__":

    """list to store objects"""
    objects = []

    motorCycle = MotorCycle()
    objects.append(Adapter(motorCycle, wheels=motorCycle.TwoWheeler))

    truck = Truck()
    objects.append(Adapter(truck, wheels=truck.EightWheeler))

    car = Car()
    objects.append(Adapter(car, wheels=car.FourWheeler))

    for obj in objects:
        print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))
