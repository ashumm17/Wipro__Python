def sort_colors(color_string):
    color_list = color_string.split('-')
    color_list.sort()
    return '-'.join(color_list)

print(sort_colors("green-red-yellow-black-white"))
print(sort_colors("PINK-BLUE-TAN-PURPLE"))