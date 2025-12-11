# *Closure to store last N executed values**.
def last_values(n):
    values = []
    def inner(x):
        nonlocal values
        values.append(x)
        if len(values) > n:
            values.pop(0)
        return values
    return inner

last_3 = last_values(3)
print(last_3(1))
print(last_3(2))
print(last_3(3))
print(last_3(4))
print(last_3(5))