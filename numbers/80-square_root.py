# Find square root manually (approximation method).

no = int(input("Enter number: "))

# using method
for i in range(1, no // 2 + 1):
    if i * i == no:
        sqrt = i
        break
    elif i * i > no:
        sqrt = i - 1
        break
print(sqrt)
