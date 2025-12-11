# Make a closure for adding prefix** to strings.
def add_prefix(prefix):
    def inner(string):
        return prefix + string
    return inner

add_hello = add_prefix("Hello, ")
print(add_hello("World!"))
print(add_hello("Python!"))