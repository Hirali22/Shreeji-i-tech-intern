# Count vowels and consonants.
input = "hello world"

v = 0
c = 0

for i in input:
    if i in "aeiou":
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)