# *Employee class** with **constructor, increment salary**
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def increment_salary(self, amount):
        self.salary += amount
    def __str__(self):
        return f"Employee {self.name} with salary {self.salary}"

emp = Employee("Shreeji", 50000)
print(emp)
emp.increment_salary(10000)
print(emp)
