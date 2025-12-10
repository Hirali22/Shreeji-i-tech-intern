# Greatest Common Divisor (GCD) using loop
no1 = int(input("Enter number 1: "))
no2 = int(input("Enter number 2: "))

for i in range(1, min(no1, no2) + 1):
    if no1 % i == 0 and no2 % i == 0:
        gcd = i

print(gcd)
