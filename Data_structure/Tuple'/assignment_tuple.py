# Program to print the 4th element from first and 4th element from last in a tuple.
my_tuple = (5, 10, 15, 20, 25, 30, 35, 40)
print("4th element from start:", my_tuple[3])     
print("4th element from end:", my_tuple[-4])       


# Program to check whether an element exists in a tuple or not.
my_tuple = (1, 3, 5, 7, 9)
element = 5

if element in my_tuple:
    print("Element exists in tuple.")
else:
    print("Element does not exist in tuple.")


# Program to convert a list into a tuple.
my_list = [10, 20, 30, 40]
converted_tuple = tuple(my_list)
print(converted_tuple)


# Program to find the index of an item in a tuple.
my_tuple = (10, 20, 30, 40, 50)
index_of_item = my_tuple.index(30)
print("Index of 30 is:", index_of_item)


# Program to replace last value of tuples in a list to 100.
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list]
print(updated_list)
