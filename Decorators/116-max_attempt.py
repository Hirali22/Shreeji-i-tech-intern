# *Decorator to restrict function calling** (max attempts).
def max_attempts_decorator(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                result = func(*args, **kwargs)
                if result is not None:
                    return result
                attempts += 1
            return "Max attempts reached"
        return wrapper
    return decorator

@max_attempts_decorator(3)
def example_function():
    return "Function executed"

print(example_function())