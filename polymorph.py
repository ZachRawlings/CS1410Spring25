class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self):
        print("hello")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def sound(self):
        print("bark")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def sound(self):
        print("meow")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def sound(self):
        print("chirp")

d = Dog("Tommy", 5)
c = Cat("Kitty", 3)
b = Bird("Polly", 2)

animals =[]
animals.append(d)
animals.append(c)
animals.append(b)

for animal in animals:
    print(animal.name, animal.age)
    animal.sound()