print("Welcome to the tip calculator!")

# Ask the user for input
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate tip multiplier
tip_percent = tip / 100
total_with_tip = bill * (1 + tip_percent)
amount_per_person = total_with_tip / people

# Format to 2 decimal places
final_amount = round(amount_per_person, 2)

print(f"Each person should pay: ${final_amount}")
# This code calculates the total amount each person should pay when splitting a bill with a tip.
# It takes the total bill, tip percentage, and number of people as input and outputs the amount each person should pay.