# **Create a Student class** (name, marks, grade method).
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"

stud = Student("Shreeji", 85)
print(stud.name)
print(stud.marks)
print(stud.grade())
