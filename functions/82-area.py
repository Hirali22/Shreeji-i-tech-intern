#calculate area of square

def area(side):
    area = side * side
    return area

print(area(5))

# return area of rectangle
def rectangle (width,height):
    area = width * height
    return area
print(rectangle(5,10))

# triangle area
def triangle(base,height):
    area = 0.5 * base * height
    return area
print(triangle(5,10))

# circle area
def circle(radius):
    area = 3.14 * radius * radius
    return area
print(circle(5))



