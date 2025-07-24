# Program to remove a given item from the set.
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  
print(my_set)


# Program to create an intersection of sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2)
print(intersection)


# Program to create a union of sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)


# Program to find the maximum and minimum value in a set.
my_set = {10, 25, 5, 30, 15}
print("Maximum:", max(my_set))
print("Minimum:", min(my_set))
