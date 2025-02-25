from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("bark")
class Cat(Animal):
    def sound(self):
        print("meow")

a = Animal()
d = Dog()
c = Cat()