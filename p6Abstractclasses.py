from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def fuel_type(self):
        print("My vehicle uses petrol.")

class Car(Vehicle):

    def start(self):
        print("Car starts with a key.")

if __name__=="__main__":
    v = Car()
    v.start()
    v.fuel_type()
