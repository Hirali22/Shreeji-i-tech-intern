# List comprehension

# 1.square
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2.even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# 3.uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# 4.flatten matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flattened = [element for row in matrix for element in row]
print(flattened)

# area of rectangle
rectangles = [(2, 3), (4, 5), (6, 8)]
area = [length * width for length, width in rectangles]
print(area)
