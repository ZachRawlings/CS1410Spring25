from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("meow")

d = Dog("buddy", 4)
c = Cat("kitty", 3)

print(d.name)
d.sound()
print(c.name)
c.sound()
