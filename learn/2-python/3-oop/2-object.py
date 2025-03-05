# class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking.")

# object
my_dog = Dog("Buddy", 3)

# accessing attributes
my_dog.name
my_dog.age

# changing attributes
my_dog.name = "Max"
my_dog.age = 5

# calling methods
my_dog.bark()
