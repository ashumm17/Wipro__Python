# Program to count the number of upper and lower case letters in a string.
text = "Hello World"
upper = sum(1 for char in text if char.isupper())
lower = sum(1 for char in text if char.islower())
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# Program to check whether a given string is palindrome or not.
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Program to return a new string made of n copies of the first 2 chars of the original string.
s = "Wipro"
n = len(s)
new_str = s[:2] * n
print(new_str)


# Program to remove 'x' if it appears at the start or end of the string.
s = "xHix"
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print(s)

# Program to return a string made of n repetitions of the last n characters.
s = "Wipro"
n = 3
last_n = s[-n:]
result = last_n * n
print(result)
