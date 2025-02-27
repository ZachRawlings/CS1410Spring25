from typing import Protocol

class Flyable(Protocol):
    def fly(self):
        ...

class Swimmable(Protocol):
    def swim(self):
        ...

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} can fly!"
    
class Airplane:
    def fly(self):
        return "Airplanes can fly!"
    
b = Bird("Sparrow")
#print(b.fly())
a = Airplane()
#print(a.fly())

class Fish:
    def swim(self):
        return "Fish can swim!"
    
f = Fish()
#print(f.swim())

class Duck:
    def fly(self):
        return "Duck can fly!"
    
    def swim(self):
        return "Duck can swim!"

d = Duck()


def make_fly(obj:Flyable):
    print(obj.fly())

def make_swim(obj:Swimmable):
    print(obj.swim())
    
make_fly(b)
make_fly(a)
make_swim(f)
make_swim(d)
make_fly(d)
