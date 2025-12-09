# reverse a number using for
n = int(input("Enter Number:"))
rev = 0

for i in range(1,n+1):
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print("Reverse of Number is:",rev)

# using while loop
n = int(input("Enter Number:"))
rev = 0

while n != 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print("Reverse of Number is:",rev)
