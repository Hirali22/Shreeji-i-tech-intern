# Perfect number check.
no = int(input("Enter number: "))
sum = 0
for i in range(1, no // 2 + 1):
    if no % i == 0:
        sum += i
if sum == no:
    print("Perfect")
else:
    print("Not Perfect")