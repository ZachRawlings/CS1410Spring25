class Animal:
    def __init__(self, name, cost=None, upkeep=None):
        self.name = name
        self.cost = cost
        self.upkeep = upkeep
    def get_upkeep_cost(self):
        return self.upkeep

class Dog(Animal):
    def __init__(self, name, cost=20, upkeep=5):
        self.name = name
        self.cost = cost
        self.upkeep = upkeep
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, cost=15, upkeep=3):
        self.name = name
        self.cost = cost
        self.upkeep = upkeep
    def sound(self):
        print("Meow!")

class Mouse(Animal):
    def __init__(self, name, cost=5, upkeep=1):
        self.name = name
        self.cost = cost
        self.upkeep = upkeep
    def sound(self):
        print("Squeak!")

class PetStore:
    def __init__(self):
        self.animals = []
        self.bank_balance = 500.0  # Initial bank balance
    def buy_from_vendor(self, animal):
        self.animals.append(Animal.name)
        self.bank_balance -= Animal.cost
        animal.upkeep += Animal.upkeep
    def sell_to_customer(self, animal):
        if animal not in self.animals:
            print("Animal not in store")
            return
        else:
            self.animals.remove(animal)
            self.bank_balance += Animal.cost
            Animal.upkeep -= Animal.upkeep
    def store_upkeep(self):
        for animal in self.animals:
            self.bank_balance -= Animal.get_upkeep_cost()
    def display_status(self):
        print(f"Bank balance: ${self.bank_balance}")
        for animal in self.animals:
            print(animal.name)

d = Dog("Tommy")
c = Cat("Kitty")
m = Mouse("Mickey")
store = PetStore()
store.buy_from_vendor(d)
store.display_status()
store.buy_from_vendor(c)
store.store_upkeep()
store.display_status()