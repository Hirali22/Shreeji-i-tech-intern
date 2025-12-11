import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def print_area(shape_instance):
    print(f"The area is: {shape_instance.area()}")

rectangle = Rectangle(width=10, height=5)
circle = Circle(radius=7)

print_area(rectangle) # Calls Rectangle.area()
print_area(circle)    # Calls Circle.area()

shapes = [rectangle, circle, Rectangle(4, 4), Circle(3)]
print("\nIterating through a list of various shapes:")
for shape in shapes:
    print_area(shape) # The correct area method is automatically selected for each object
