# Find frequency of each word in sentence.
input = "hello world hello world hello world"
words = input.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)




