# 1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except Exception as e:
    print("Error:", e)

# 2. Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, handle the exception and print an error message.
try:
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not Prime")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
except ValueError:
    print("Invalid input. Please enter a valid number.")

# 3. Write a program to accept the file name to be opened from the user, if file exists print the contents of the file in title case or else handle the exception and print an error message.
try:
    filename = input("Enter file name: ")
    with open(filename, 'r') as f:
        content = f.read()
        print(content.title())
except FileNotFoundError:
    print("File not found.")

# 4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
nums = [5, -2, 9, 0, -7, 3, -1, 6, -8, 4]
try:
    index = int(input("Enter index (0-9): "))
    if nums[index] >= 0:
        print("Positive number or Zero")
    else:
        print("Negative number")
except IndexError:
    print("Invalid index. Please enter a value between 0 and 9.")