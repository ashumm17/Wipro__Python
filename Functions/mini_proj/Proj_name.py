def ispalindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    return sum(1 for c in name if c in vowels)

def frequency_of_letters(name):
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    return freq

name = input("Enter the name: ")

print("Is palindrome:", ispalindrome(name))
print("Vowel count:", count_the_vowels(name))
print("Letter frequency:", frequency_of_letters(name))