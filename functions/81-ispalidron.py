# Write a function that takes a string as input and returns True if the string is a palindrome, False otherwise.
input = input("Enter string: ")
def is_palindrome(input):
    reversed = ""
    for i in input:
        reversed = i + reversed
    if input == reversed:
        print(reversed)
        return True
    else:
        print(reversed)
        return False
print(is_palindrome(input))
