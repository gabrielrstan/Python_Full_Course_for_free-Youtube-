from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("Voce dirige o carro")

    def stop(self):
        print("Esse carro parou")


class Motocycle(Vehicle):
    
    def go(self):
        print("Voce dirige a moto")

    def stop(self):
        print("Essa moto parou")

#vehicle = Vehicle()
car = Car()
motocycle = Motocycle()

#vehicle.go()
car.go()
motocycle.go()
car.stop()
motocycle.stop()