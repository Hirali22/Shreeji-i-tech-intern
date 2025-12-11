# **Car class** implementing **encapsulation**.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def set_make(self, make):
        self.make = make
    def set_model(self, model):
        self.model = model
    def set_year(self, year):
        self.year = year

c1 = Car("Honda", "Civic", 2020)    
print(c1)
