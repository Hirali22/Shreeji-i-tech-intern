# Least Common Multiple (LCM) using logic.
no1 = int(input("Enter number 1: "))
no2 = int(input("Enter number 2: "))

for i in range(1, max(no1, no2) + 1):
    if i % no1 == 0 and i % no2 == 0:
        lcm = i
        break

print(lcm)
