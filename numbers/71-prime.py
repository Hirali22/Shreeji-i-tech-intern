# Check prime number.
no = int(input("Enter number: "))

for i in range(2, no):
    if no % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
