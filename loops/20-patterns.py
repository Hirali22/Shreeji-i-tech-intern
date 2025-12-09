# print patterns (triangle, pyramid, square).

no = int(input("Enter Number:"))

# triangle
for i in range(1,no+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 


# pyramid
for i in range(1,no+1):
    for j in range(1,no-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(1,i):
        print(j,end=" ")
    print()

# square
for i in range(1,no+1):
    for j in range(1,no+1):
        print("*",end=" ")
    print()
