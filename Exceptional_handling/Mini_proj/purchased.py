try:
    filename = input("Enter filename: ")
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_items = len(lines)
    free_items = total_items // 5
    total_cost = 0

    prices = []
    for line in lines:
        name, price = line.strip().split()
        prices.append(float(price))

    prices.sort()
    free_items_cost = sum(prices[:free_items])
    total_cost = sum(prices)
    final_amount = total_cost - free_items_cost

    print("Total items purchased:", total_items)
    print("Free items:", free_items)
    print("Total amount:", total_cost)
    print("Discount amount:", free_items_cost)
    print("Final amount after discount:", final_amount)

except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid file format.")
except Exception as e:
    print("Error:", e)