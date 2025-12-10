# sort using bubble sort
list = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
print(list)
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print(list)

# sort method
list.sort()
print(list)
