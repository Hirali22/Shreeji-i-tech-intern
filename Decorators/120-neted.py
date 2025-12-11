# **Nested decorators** (e.g., timer + logger together).
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@timer_decorator
@logger_decorator
def example_function(a, b):
    return a + b

print(example_function(2, 3))