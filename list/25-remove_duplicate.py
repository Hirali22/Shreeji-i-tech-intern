# remove duplicates from a list
my_list = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
print(my_list)
my_list = list(set(my_list))
print(my_list)

# using loop
my_list = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
print(my_list)
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)
