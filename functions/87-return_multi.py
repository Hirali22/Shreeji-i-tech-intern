#return multiple values from function sum avg max

# sum of two numbers
def sum(a,b):
    return a+b
# max of two numbers
def max(a,b):
    if a > b:
        return a
    else:
        return b

# avg of two numbers
def avg(a,b):
    return (a+b)/2

print(sum(5,10))
print(max(5,10))
print(avg(5,10))
