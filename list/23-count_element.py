# using method
my_list = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
element_to_count = 3
occurrences = my_list.count(element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list.")

# using loop
my_list = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
element_to_count = 2
count = 0
for item in my_list:
    if item == element_to_count:
        count += 1
print(f"The element {element_to_count} appears {count} times in the list.")