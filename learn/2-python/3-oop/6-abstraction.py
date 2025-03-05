# abstraction: hiding the implementation details of a class and showing
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# car has to implement start_engine, otherwise it will raise an error
class Car(Vehicle): 
    def start_engine(self):
        print("Car engine started")

my_car = Car()
my_car.start_engine()
