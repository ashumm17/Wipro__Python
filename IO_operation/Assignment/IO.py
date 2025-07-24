# 1. Write a program to read the entire content from a txt file and display it to the user.
def read_entire_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

# 2. Write a program to read first n lines from a txt file. Get n as user input.
def read_n_lines(filename, n):
    with open(filename, 'r') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip())

# 3. Write a program to accept input from user and append it to a txt file.
def append_user_input(filename):
    data = input("Enter text to append: ")
    with open(filename, 'a') as file:
        file.write(data + '\n')

# 4. Write a program to read contents from a txt file line by line and store each line into a list.
def file_to_list(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    print(lines)

# 5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
def find_longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        longest = max(words, key=len)
    print("Longest word:", longest)

# 6. Write a program to count the frequency of a user entered word in a txt file.
def word_frequency(filename):
    word = input("Enter the word to count: ")
    with open(filename, 'r') as file:
        content = file.read()
        count = content.split().count(word)
    print(f"Frequency of '{word}':", count)