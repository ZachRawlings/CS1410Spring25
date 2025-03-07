class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def get_info(self):
        return f"{self.name} is a {self.species} aged {self.age} years."


class Dog(Animal):
    def __init__(self, name, age, breed, species="Dog"):
        super().__init__(name, species, age) # fixed the error here
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barks loudly!")

    def fetch(self):
        print(f"{self.name} fetches the ball.")


class Cat(Animal):
    def __init__(self, name, age, color, species="Cat"):
        super().__init__(name,species, age) # fixed the error here
        self.color = color

    def make_sound(self):
        print(f"{self.name} meows softly.")

    def scratch(self):
        print(f"{self.name} scratches the furniture.")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("Error: Only animals can be added to the zoo.")

    def list_animals(self):
        for animal in self.animals:
            print(animal.get_info())

    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()

    def feed_animals(self):
        if len(self.animals) == 0:
            print("There are no animals to feed.")
        else:
            for animal in self.animals:
                print(f"Feeding {animal.name}")
                feed += 1
        if feed == 5:  # ATTEMTPED FIX HERE
            animal.age += 1
                
fido = Dog("Fido", 5, "Golden Retriever")
whiskers = Cat("Whiskers", 3, "Orange")



zoo = Zoo()
zoo.add_animal(fido)
zoo.add_animal(whiskers)
zoo.make_all_sounds() 
print(zoo.list_animals())# FIXED ERROR HERE
zoo.feed_animals()
print(zoo.list_animals()) # FIXED ERROR HERE
