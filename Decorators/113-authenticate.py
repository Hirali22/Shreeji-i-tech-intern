# **Decorator to check authentication** before running function.
def is_authenticated():
    return True
def authenticate_decorator(func):
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            return "Authentication failed"
        return func(*args, **kwargs)
    return wrapper

@authenticate_decorator
def example_function():
    return "Function executed"

print(example_function())