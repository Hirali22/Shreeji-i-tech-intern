# Function factory using closures** (e.g., power(base), returns base^x).
def power(base):
    def inner(x):
        return base ** x
    return inner

square = power(2)
print(square(3))
print(square(4))    