# **Decorator to validate input types**
def validate_input_types_decorator(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("All arguments must be integers")
        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise TypeError("All keyword arguments must be integers")
        return func(*args, **kwargs)
    return wrapper

@validate_input_types_decorator
def example_function(a, b):
    return a + b

print(example_function(2, 3))
print(example_function(a=2, b=3))
