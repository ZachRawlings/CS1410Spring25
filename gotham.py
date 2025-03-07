import random
from typing import Optional

# Base Character Class
class Character:
    def __init__(self, name, health, strength)-> any:
        self.name = name
        self.health = health
        self.strength = strength
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
    
    def is_alive(self):
        return self.health > 0

    def interact_with_batman(self):
        pass  # To be implemented in subclasses

# Hero Class: Batman
class Hero(Character):
    def __init__(self, name="Batman", health=100, strength=20, gadgets=None):
        super().__init__(name, health, strength)
        self.gadgets = gadgets if gadgets else ["Batarang", "Grappling Hook", "Smoke Bomb"]
    
    def use_gadget(self, gadget_name):
        if gadget_name in self.gadgets:
            print(f"{self.name} uses the {gadget_name}!")
        else:
            print(f"{self.name} doesn't have {gadget_name}!")
    
    def fight(self, villain:'Villain'):
        print(f"{self.name} fights {villain.name}!")
        villain.take_damage(self.strength)
        if not villain.is_alive():
            print(f"{villain.name} has been defeated by Batman!")

# Villain Class
class Villain(Character):
    def __init__(self, name, health, strength, crime_level):
        super().__init__(name, health, strength)
        self.crime_level = crime_level
    
    def commit_crime(self):
        print(f"{self.name} is causing chaos in Gotham!")
    
    def interact_with_batman(self):
        if random.choice([True, False]):
            print(f"{self.name}: 'Ha-ha! Gotham is mine!'")
        else:
            print(f"{self.name} tries to escape, but Batman is faster!")

# Citizen Class
class Citizen(Character):
    def __init__(self, name, fear_level):
        super().__init__(name, health=50, strength=5)
        self.fear_level = fear_level
    
    def call_batman(self):
        print(f"{self.name} calls Batman for help!")
    
    def interact_with_batman(self):
        print(f"{self.name} thanks Batman for keeping Gotham safe!")

# Gotham City Class
class GothamCity:
    def __init__(self):
        self.characters = []
    
    def add_character(self, character:str):
        self.characters.append(character)
    
    def simulate_night(self):
        print("Night falls over Gotham...")
        for character in self.characters:
            if isinstance(character, Villain):
                character.commit_crime()
            elif isinstance(character, Citizen):
                if random.choice([True, False]):
                    character.call_batman()
        print("Batman patrols the city!")
        for character in self.characters:
            if isinstance(character, Villain) and character.is_alive():
                batman.fight(character)


batman = Hero()
joker = Villain("Joker", health=80, strength=15, crime_level=10)
riddler = Villain("Riddler", health=70, strength=10, crime_level=7)
citizen1 = Citizen("John Doe", fear_level=5)
citizen2 = Citizen("Jane Smith", fear_level=8)

gotham = GothamCity()
gotham.add_character(joker)
gotham.add_character(riddler)
gotham.add_character(citizen1)
gotham.add_character(citizen2)

# Simulate a night in Gotham
print("--- Welcome to Gotham City ---")
gotham.simulate_night()
