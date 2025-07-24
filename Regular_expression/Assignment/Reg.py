import re
import requests

# -------------------------------------------------------
# Q1: Write a program to find if a string has only octal digits.
# Given string ['789','123','004']
# -------------------------------------------------------
octal_strings = ['789', '123', '004']
for s in octal_strings:
    if re.fullmatch(r'[0-7]+', s):
        print(f"{s} is an octal number.")
    else:
        print(f"{s} is NOT an octal number.")

# -------------------------------------------------------
# Q2: Extract the user id, domain name and suffix from email addresses.
# emails = """zuck@facebook.com
#             sunder33@google.com
#             jeff42@amazon.com"""
# -------------------------------------------------------
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'(\w+)@(\w+)\.(\w+)'
matches = re.findall(pattern, emails)
for user, domain, suffix in matches:
    print(f"User: {user}, Domain: {domain}, Suffix: {suffix}")

# -------------------------------------------------------
# Q3: Split the following irregular sentence into proper words.
# sentence = "A, very    very; irregular_sentence"
# Expected output: A very very irregular sentence
# -------------------------------------------------------
sentence = "A, very    very; irregular_sentence"
cleaned = re.sub(r'[^a-zA-Z]', ' ', sentence)
cleaned = re.sub(r'\s+', ' ', cleaned).strip()
print("Cleaned Sentence:", cleaned)

# -------------------------------------------------------
# Q4: Clean up the tweet to remove all URLs, hashtags, mentions, RTs, and CCs.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today
# http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# Desired output: 'Good advice What I would do differently if I was learning to code today'
# -------------------------------------------------------
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today
http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

clean_tweet = re.sub(r'http\S+|@\S+|#\S+|RT|cc:|[^\w\s]', '', tweet)
clean_tweet = re.sub(r'\s+', ' ', clean_tweet).strip()
print("Cleaned Tweet:", clean_tweet)

# -------------------------------------------------------
# Q5: Extract all the text portions between HTML tags from the HTML page.
# URL: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
# -------------------------------------------------------
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text
tags = re.findall(r'>([^<>]+)<', html)
tags = [tag.strip() for tag in tags if tag.strip()]
print("Extracted Text from HTML Tags:")
print(tags)


# -------------------------------------------
# Question 6:
# Write a program to check whether a given string is palindrome or not.
# Input: madam
# Output: Palindrome

def is_palindrome(text):
    return text == text[::-1]

text = "madam"
print("Palindrome" if is_palindrome(text) else "Not a Palindrome")