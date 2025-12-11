# **Implement abstract class** using `abc` module.
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Child class 1
class Dog(Animal):
    def sound(self):
        return "Bark 🐶"


# Child class 2
class Cat(Animal):
    def sound(self):
        return "Meow 🐱"


# Using the classes
dog = Dog()
cat = Cat()

print(dog.sound())
print(cat.sound())
