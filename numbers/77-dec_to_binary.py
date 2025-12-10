# Convert decimal to binary manually.
dec = int(input("Enter decimal number: "))
binary = ""

while dec > 0:
    binary = str(dec % 2) + binary
    dec //= 2

print(binary)