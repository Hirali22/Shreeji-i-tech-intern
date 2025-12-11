# **Create a simple decorator** that prints "Function started" & "Function ended".
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@simple_decorator
def example_function():
    print("Inside the example function")
    return 42

example_function()
