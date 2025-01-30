class PetStore:
    def __init__(self, name, money = 500, pets = None):
        self.name = name
        self.money = money
        if pets is None:
            self.pets = []
        self.upkeep = 0
    def buyFromVendor(self, pet):
        self.pets.append(pet)
        self.money -= pet.cost
        self.upkeep += pet.upkeep
        return self.pets
    def sellToCustomer(self, pet):
        self.pets.remove(pet)
        self.money += pet.cost
        self.upkeep -= pet.upkeep
    def storeUpkeep(self,upkeep):
        self.money -= upkeep

class Pet:
    pass
class Dog(Pet):
    def __init__(self, name, breed, cost = 15, upkeep = 5):
        self.name = name
        self.breed = breed
        self.cost = cost
        self.upkeep = upkeep
    def speak(self,sound):
        return sound

class Cat(Pet):
    def __init__(self, name, breed, cost = 10, upkeep = 3):
        self.name = name
        self.breed = breed
        self.cost = cost
        self.upkeep = upkeep
    def speak(self,sound):
        return sound
    
class Bird(Pet):
    def __init__(self, name, breed, cost = 5, upkeep = 1):
        self.name = name
        self.breed = breed
    def speak(self,sound):
        return sound

P = PetStore("Monkey Business")
print(P.name)
P.buyFromVendor(Dog("Fido","Labrador"))
print(P.pets[0].name)