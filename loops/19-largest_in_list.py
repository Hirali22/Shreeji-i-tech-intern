# find largest element in a list
lst = [10, 20, 30, 40, 50]
max = lst[0]
for i in lst:
    if i > max:
        max = i
print("Largest Element in List is:",max)
