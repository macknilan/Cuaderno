# abstract base classes

import abc

class Vehicle(abc.ABC):
    """
    Declaracion de la clase abstracta
    """
    @abc.abstractmethod
    def go(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    """
    Clase heredada de -Vehicle-
    """
    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")


class Motorcycle(Vehicle):
    """
    Clase heredada de -Vehicle-
    """
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()
