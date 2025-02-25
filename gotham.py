import random
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage and now has {self.health} health")
    
    def is_alive(self):
        if self.health > 0:
            print(f"{self.name} is alive")
            return True   
        else:
            print(f"{self.name} is dead")
            return False
            
    
class Batman(Character):
    def __init__(self, name = "Batman", health = 100, strength = 10):
        super().__init__(name, health, strength)
        self.gadgets = {"batarang": 10, "smoke bomb": 5, "grappling hook": 15}
            
    def use_gadget(self, gadget):
        if gadget in self.gadgets:
            print(f"{self.name} used {gadget}")
            return self.gadgets[gadget]
        else:
            print(f"{self.name} does not have {gadget}")
            return 0
    def rest(self):
        print(f"{self.name} is resting")
        self.health += 5
        return self.health
        
class Joker(Character):
    def __init__(self, name = "Joker", health = 50, strength = 5):
        super().__init__(name, health, strength)
        self.crime_level = 20
            
    def commit_crime(self):
        print(f"{self.name} committed a crime")
        self.crime_level += 5
        return self.crime_level
        
    def interact_with_batman(self):
        print(f"{self.name} is interacting with Batman")
        if self.crime_level <= 20:
            print(f"{self.name} ran from Batman")
        else:
            print(f"{self.name} is fighting Batman")
            for i in range(random.randint(1, 5)):
                attack = random.randint(1, 3)
                if attack == 1:
                    print("Batman dodged the attack")
                elif attack == 2:
                    print(f"{self.name} hit Batman")
                    Batman.take_damage(5)
                else:
                    print(f"Batman hit {self.name}")
                    self.take_damage(10)
        self.crime_level -= 5
        return self.crime_level
    
    def rest(self):
        print(f"{self.name} is resting")
        self.health += 5
        return self.health
    
class Citizen(Character):
    def __init__(self, name, health = 10, strength=1):
        super().__init__(name, health, strength)
        self.name = name
        self.fear_level = 0

    def call_batman(self):
        print(f"{self.name} called Batman")
        self.fear_level += 5
        return self.fear_level
        
    def interact_with_batman(self):
        print(f"{self.name} assisted Batman")
        self.fear_level -= 2
        if self.fear_level <= 0:
            self.fear_level == 0 
            print(f"{self.name} thanked Batman")
        else:
            print(f"{self.name} is still afraid")
        return self.fear_level
        
class Gotham:
    def __init__(self):
        self.citizens = []
        self.joker = Joker()
        self.batman = Batman()
        
    def add_citizen(self, citizen):
        self.citizens.append(citizen)
        
    def simulate_night(self):
        for citizen in self.citizens:
            for i in range(random.randint(1, 5)):
                self.joker.commit_crime()
            Citizen.call_batman(citizen)
            Citizen.interact_with_batman(citizen)
            for i in range(random.randint(1, 5)):
                self.joker.interact_with_batman()
            self.batman.use_gadget("batarang")
            for i in range(random.randint(1, 3)):
                self.batman.rest()
            for i in range(random.randint(1, 3)):
                self.joker.rest()
            if self.joker.is_alive() == False or self.joker.crime_level == 0:
                print("Batman wins! Gotham is safe once again!")
                break
            if self.batman.is_alive() == False or self.joker.crime_level == 100:
                print("Joker wins! Gotham is doomed!")
                break

gotham = Gotham()
gotham.add_citizen("John")
gotham.add_citizen("Jane")
gotham.add_citizen("Jack")   

gotham.simulate_night()