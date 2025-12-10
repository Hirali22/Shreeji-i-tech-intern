# Remove spaces from string.
input = "hello world"
output = ""

for i in input:
    if i != " ":
        output += i

print(output)

# method 
input = "hello world"
output = input.strip()
print(output)


