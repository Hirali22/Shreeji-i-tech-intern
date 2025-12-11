# Closure to track how many times a function is called
def function_caller():
    count = 0
    def inner(func, *args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, **kwargs)
    return inner

# Example usage
def add(a, b):
    return a + b

caller = function_caller()
print(caller(add, 2, 3))  # Output: 5
print(caller(add, 4, 5))  # Output: 9
print(caller(add, 6, 7))  # Output: 13
