# Program to create a list of 5 integers and display the list items. Access individual elements through index.
numbers = [10, 20, 30, 40, 50]
print("Full List:", numbers)

print("Access elements by index:")
print("First Element:", numbers[0])
print("Second Element:", numbers[1])
print("Third Element:", numbers[2])
print("Fourth Element:", numbers[3])
print("Fifth Element:", numbers[4])

# Program to append a new item to the end of the list.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print("Updated List:", numbers)


# Program to reverse the order of the items in the list.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print("Reversed List:", numbers)


# Program to print the number of occurrences of a specified element in a list.
numbers = [1, 2, 3, 2, 4, 2, 5]
count_2 = numbers.count(2)
print("Number of occurrences of 2:", count_2)


# Program to append the items of list1 to list2 in the front.
list1 = [10, 20, 30]
list2 = [40, 50, 60]
result = list1 + list2
print("Combined List (list1 at front):", result)

# Program to insert a new item before the second element in an existing list.
numbers = [100, 200, 300]
numbers.insert(1, 150)  # Insert before index 1 (second element)
print("List after insertion:", numbers)


# Program to remove the item from a specified index in a list.
numbers = [10, 20, 30, 40, 50]
del numbers[2]  # Removes item at index 2 (which is 30)
print("List after removal:", numbers)


# Program to remove the first occurrence of a specified element from a list.
numbers = [5, 3, 7, 3, 9]
numbers.remove(3)  # Removes the first occurrence of 3
print("List after removing first occurrence of 3:", numbers)
