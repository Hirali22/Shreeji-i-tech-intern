#  Armstrong number check.
no = int(input("Enter number: "))
sum = 0
temp = no

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if no == sum:
    print("Armstrong")
else:
    print("Not Armstrong")