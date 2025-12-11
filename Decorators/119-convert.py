# *Decorator that converts function output to uppercase**
def convert_output_to_uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@convert_output_to_uppercase_decorator
def example_function():
    return "hello world"

print(example_function())
