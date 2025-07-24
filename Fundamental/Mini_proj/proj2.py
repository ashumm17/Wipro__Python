# Project 2: Cloud Server Cost Calculator

def server_cost_calculator():
    hourly_cost = 50.51
    daily_cost = hourly_cost * 24
    weekly_cost = daily_cost * 7
    monthly_cost = daily_cost * 30  # Approximate month as 30 days

    print("\n--- Server Operation Cost ---")
    print(f"Cost per day   : ${daily_cost:.2f}")
    print(f"Cost per week  : ${weekly_cost:.2f}")
    print(f"Cost per month : ${monthly_cost:.2f}")

    budget = 918
    days_operable = budget / daily_cost
    print(f"\nWith ${budget}, you can operate one server for approximately {days_operable:.2f} days.")

# Run the function
server_cost_calculator()
