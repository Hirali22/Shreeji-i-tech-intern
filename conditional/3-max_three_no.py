# Find greatest of three numbers
no1 = int(input("Enter First Number:"))
no2 = int(input("Enter Second Number:"))
no3 = int(input("Enter Third Number:"))

if no1 > no2 and no1 > no3:
    print("First Number is greatest")
elif no2 > no1 and no2 > no3:
    print("Second Number is greatest")
else:
    print("Third Number is greatest")