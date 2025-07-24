# -------------------------------------------
# Question:
# Cube every number in the given list using lambda function and map().
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output: [1, 8, 27, 64, 125, 216, 343, 512, 729]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cubed_list = list(map(lambda x: x**3, list_1))
print("Cubed List:", cubed_list)
