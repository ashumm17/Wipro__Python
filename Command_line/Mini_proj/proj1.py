# Project: Happiness Counter using Command Line Arguments

import sys

def calculate_happiness():
    if len(sys.argv) != 4:
        print("Usage: python script.py <like> <dislike> <given>")
        print("Example: python script.py 3-1 5-7 1-5-3-8")
        return

    # Extract command-line arguments
    like_str = sys.argv[1]
    dislike_str = sys.argv[2]
    given_str = sys.argv[3]

    # Convert to sets/lists of integers
    like_set = set(map(int, like_str.split('-')))
    dislike_set = set(map(int, dislike_str.split('-')))
    given_list = list(map(int, given_str.split('-')))

    happiness = 0

    for num in given_list:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1

    print(happiness)

# Call the function
if __name__ == "__main__":
    calculate_happiness()
