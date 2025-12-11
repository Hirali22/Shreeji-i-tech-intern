# check if a list has any duplicate elements
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 2, 3, 4, 5, 1]))
