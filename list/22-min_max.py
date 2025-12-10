# Find max/min from list without using built-ins.
list = [1,2,3,4,5]
max = list[0]
min = list[0]
for i in list:
    if i > max:
        max = i
    if i < min:
        min = i
print(max)
print(min)
