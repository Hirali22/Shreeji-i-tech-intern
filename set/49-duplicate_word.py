#  Eliminate repeated words from paragraph using set.
paragraph = "Hello world, hello world, hello world."
words = paragraph.split()
unique_words = set(words)
print(unique_words)