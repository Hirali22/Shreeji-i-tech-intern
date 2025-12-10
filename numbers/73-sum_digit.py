# Sum of digits of a number.
no = int(input("Enter number: "))
sum = 0

while no > 0:
    digit = no % 10
    sum += digit
    no //= 10

print(sum)
