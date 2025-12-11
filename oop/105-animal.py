# **Animal → Dog** inheritance example.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def __str__(self):
        return f"{self.name} is {self.age} years old"

dog= Dog("Buddy", 3)
print(dog)

