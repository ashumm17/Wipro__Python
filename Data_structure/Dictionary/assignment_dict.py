# Program to add a key and value to a dictionary.
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)


# Program to concatenate multiple dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

print(result)


# Program to check if a given key already exists in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'

if key_to_check in my_dict:
    print("Key exists.")
else:
    print("Key does not exist.")


# Program to iterate over a dictionary using a for loop and print keys, values, and both.
my_dict = {'x': 100, 'y': 200, 'z': 300}

print("Keys:")
for key in my_dict:
    print(key)

print("Values:")
for value in my_dict.values():
    print(value)

print("Keys and Values:")
for key, value in my_dict.items():
    print(key, value)


# Program to prepare a dictionary with keys from 1 to 15 and values as squares of keys.
squares = {x: x**2 for x in range(1, 16)}
print(squares)


# Program to sum all the values in a dictionary where values are of int type.
my_dict = {'a': 10, 'b': 20, 'c': 30}
total = sum(my_dict.values())
print("Sum of values:", total)
