# Write a program to check if a given number is Positive, Negative, or Zero.
# Topics Covered: if else

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Write a program to check if a given number is odd or even.
# Topics Covered: if else

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Given two non-negative values, print true if they have the same last digit.
# Example: lastDigit(7, 17) → true, lastDigit(6, 17) → false, lastDigit(3, 113) → true
# Topics Covered: if else

def lastDigit(a, b):
    return a % 10 == b % 10

# Test cases
print(lastDigit(7, 17))   # True
print(lastDigit(6, 17))   # False
print(lastDigit(3, 113))  # True


# Write a program to print numbers from 1 to 10 in a single row with one tab space.
# Topics Covered: for

for i in range(1, 11):
    print(i, end='\t')


# Write a program to print even numbers between 23 and 57.
# Each number should be printed in a separate row.
# Topics Covered: for

for i in range(23, 58):
    if i % 2 == 0:
        print(i)


# Write a program to check if a given number is prime or not.
# Topics Covered: for

num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# Write a program to print prime numbers between 10 and 99.
# Topics Covered: for

for num in range(10, 100):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)


# Write a program to print the sum of all the digits of a given number.
# Example: I/P: 1234 → O/P: 10
# Topics Covered: while

num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num = num // 10
print("Sum of digits:", total)


# Write a program to reverse a given number and print.
# Example: I/P: 1234 → O/P: 4321
#          I/P: 1004 → O/P: 4001
# Topics Covered: while

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(f"Reversed number of {original} is: {reverse}")


# Write a program to find if the given number is palindrome or not.
# Example: I/P: 110011 → O/P: 110011 is a palindrome.
#          I/P: 1234   → O/P: 1234 is not a palindrome.
# Topics Covered: while

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")


