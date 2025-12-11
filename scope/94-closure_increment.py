# **Create closure-based counter** (increment function).
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

inc = counter()
print(inc())
print(inc())
print(inc())