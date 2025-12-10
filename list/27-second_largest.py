# Find second-largest number in list.
my_list = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
print(my_list)
my_list.sort()
print(my_list)
print(my_list[-2])

# using loop
for i in range(len(my_list)):
    if my_list[i] == my_list[-2]:
        print(my_list[i])