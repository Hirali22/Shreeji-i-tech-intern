# *Write a closure** that generates a multiplier function.
def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print(double(5))