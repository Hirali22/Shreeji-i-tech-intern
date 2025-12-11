# frequency of char in string

str = "hello world"
def count_freq(str):
    freq = {}
    for char in str:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(count_freq(str))