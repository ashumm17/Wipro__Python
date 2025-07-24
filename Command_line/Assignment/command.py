# -----------------------------------------------
# Q1. Write a program to accept two numbers as command line arguments and display their sum.
# -----------------------------------------------
import sys

if len(sys.argv) >= 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print(f"Sum of {num1} and {num2} is: {num1 + num2}")
    except ValueError:
        print("Please provide valid integers as command line arguments.")
else:
    print("Usage: python script.py <num1> <num2>")

# -----------------------------------------------
# Q2. Write a program to accept a welcome message through command line arguments
# and display the file name along with the welcome message.
# -----------------------------------------------
import sys

if len(sys.argv) >= 2:
    welcome_message = " ".join(sys.argv[1:])
    print(f"Filename: {sys.argv[0]}")
    print(f"Welcome Message: {welcome_message}")
else:
    print("Usage: python script.py <welcome message>")

# -----------------------------------------------
# Q3. Write a program to accept 10 numbers through command line arguments
# and calculate the sum of prime numbers among them.
# -----------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) >= 11:
    try:
        numbers = list(map(int, sys.argv[1:11]))
        prime_sum = sum(num for num in numbers if is_prime(num))
        print(f"Sum of prime numbers among the given inputs: {prime_sum}")
    except ValueError:
        print("Please enter only integers as command line arguments.")
else:
    print("Usage: python script.py <num1> <num2> ... <num10>")
