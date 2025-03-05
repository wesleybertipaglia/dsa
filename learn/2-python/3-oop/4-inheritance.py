# inheritance: a class can inherit from another class
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

# dog inherits from animal
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog")
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} says Woof!")

# cat inherits from animal
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat")
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} says Meow!")
