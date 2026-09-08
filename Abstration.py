#program for use of abstraction in python
from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def eat(self):
        pass
class dog(animal):
    def eat(self):
        print("Dog is eating")

class cat(animal):
    def eat(self):
        print("Cat is eating")

d = dog()
d.eat()  

c = cat()
c.eat()  