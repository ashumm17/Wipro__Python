# Project 1: Travel Suggestion

def travel_suggestion():
    try:
        distance = float(input("How far would you like to travel in miles? "))
        
        if distance < 3:
            print("\nI suggest Bicycle to your destination")
        elif distance < 300:
            print("\nI suggest Motor-Cycle to your destination")
        else:
            print("\nI suggest Super-Car to your destination")
    except ValueError:
        print("\nInvalid input! Please enter a numeric value.")

# Run the function
travel_suggestion()
