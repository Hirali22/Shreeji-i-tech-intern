# **Decorator to cache results** (simple memoization).
def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@cache_decorator
def example_function(a, b):
    return a + b

print(example_function(2, 3))
print(example_function(2, 3)) # Cached result