# polymorphism: a method can be implemented in multiple ways
class Animal: 
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
dog.make_sound()  # Output: Woof!

cat = Cat()
cat.make_sound()  # Output: Meow!
