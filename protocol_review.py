from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

class Bird(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def fly(self):
        pass

class Swimable(Protocol):
    def swim(self):
        ...

class Walkable(Protocol):
    def walk(self):
        ...

class Penguin:
    def __init__(self, name):
        self.name = name
    def swim(self):
        return f"{self.name} can swim"
    def walk(self):
        return f"{self.name} can walk"

class Parrot(Bird):
    def fly(self):
        return f"{self.name} can fly"
    

def can_swim(animal: Swimable) -> None:
    print(animal.swim())

p = Penguin("Happy")

print(isinstance(p,Swimable))
can_swim(p)
