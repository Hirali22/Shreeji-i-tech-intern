#  Count character frequency in a string using dictionary. without udf"""  """
freq = {}
string = "hello world"

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)
