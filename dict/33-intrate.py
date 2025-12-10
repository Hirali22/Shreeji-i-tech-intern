# Iterate through keys, values, items.\

stud = {
    "name":"Hiral",
    "rno": 1 ,
    "city":"jnd"
    }
print(stud)

# iterate through keys
for key in stud:
    print(key)

# iterate through values
for value in stud.values():
    print(value)

# iterate through items (key-value pairs)
for key, value in stud.items():
    print(key, value)
