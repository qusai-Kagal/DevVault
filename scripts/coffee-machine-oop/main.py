# Coffee Machine Program - Angela Yu's 100 Days of Code Day 16
# This program simulates a coffee vending machine using Object-Oriented Programming

# Import the required classes from separate modules
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of each class to handle different aspects of the coffee machine
money_machine = MoneyMachine()  # Handles all money-related operations (payments, change, profit)
coffee_maker = CoffeeMaker()  # Manages resources (water, milk, coffee) and makes drinks
menu = Menu()  # Contains drink options and finds specific drinks

# Control variable to keep the machine running
is_on = True

# Main program loop - continues until user turns off the machine
while is_on:
    # Get all available drink options from the menu
    options = menu.get_items()

    # Prompt user for their choice, showing available options
    choice = input(f"What would you like ({options}): ")

    # Check if user wants to turn off the machine
    if choice == "off":
        is_on = False

    # Check if user wants to see a report of resources and money
    elif choice == "report":
        coffee_maker.report()  # Shows current water, milk, coffee levels
        money_machine.report()  # Shows current profit/money collected

    # Handle drink selection
    else:
        # Find the drink object that matches the user's choice
        drink = menu.find_drink(choice)

        # Check if there are enough resources AND if payment is successful
        # Both conditions must be true to proceed with making the drink
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make the coffee and deduct resources
            coffee_maker.make_coffee(drink)