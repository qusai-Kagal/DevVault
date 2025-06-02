# Coffee Machine Program
# Angela Yu's 100 Days of Code - Day 15
# A simple coffee machine that serves espresso, latte, and cappuccino

# Menu dictionary containing drink recipes and costs
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,    # ml of water needed
            "coffee": 18,   # grams of coffee needed
        },
        "cost": 1.5,        # price in dollars
    },
    "latte": {
        "ingredients": {
            "water": 200,   # ml of water needed
            "milk": 150,    # ml of milk needed
            "coffee": 24,   # grams of coffee needed
        },
        "cost": 2.5,        # price in dollars
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,   # ml of water needed
            "milk": 100,    # ml of milk needed
            "coffee": 24,   # grams of coffee needed
        },
        "cost": 3.0,        # price in dollars
    }
}

# Global variables to track machine state
profit = 0  # Total money earned by the machine
resources = {
    "water": 300,   # ml of water available
    "milk": 200,    # ml of milk available
    "coffee": 100,  # grams of coffee available
}


def is_resource_sufficient(order_ingredients):
    """
    Check if there are enough resources to make the requested drink.
    
    Args:
        order_ingredients (dict): Dictionary of ingredients needed for the drink
        
    Returns:
        bool: True when order can be made, False if ingredients are insufficient
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    Calculate and return the total amount of money inserted by the customer.
    Prompts user to insert quarters, dimes, nickels, and pennies.
    
    Returns:
        float: Total calculated from coins inserted
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25   # Quarter = $0.25
    total += int(input("how many dimes?: ")) * 0.1      # Dime = $0.10
    total += int(input("how many nickles?: ")) * 0.05   # Nickel = $0.05
    total += int(input("how many pennies?: ")) * 0.01   # Penny = $0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Check if the customer has inserted enough money for the drink.
    Calculate change if overpaid and update profit.
    
    Args:
        money_received (float): Amount of money customer inserted
        drink_cost (float): Cost of the requested drink
        
    Returns:
        bool: True when payment is accepted, False if money is insufficient
    """
    if money_received >= drink_cost:
        # Calculate change and round to 2 decimal places
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        # Update global profit variable
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Prepare the coffee by deducting the required ingredients from available resources.
    
    Args:
        drink_name (str): Name of the drink being made
        order_ingredients (dict): Dictionary of ingredients needed for the drink
    """
    # Deduct ingredients from resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Main program loop
is_on = True  # Flag to control the coffee machine's operation

while is_on:
    # Display menu and get user choice
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    
    # Secret command to turn off the machine (for maintenance)
    if choice == "off":
        is_on = False
    
    # Secret command to display current resources and profit
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    
    # Process drink order
    else:
        drink = MENU[choice]  # Get drink details from menu
        
        # Check if enough resources are available
        if is_resource_sufficient(drink["ingredients"]):
            # Process payment
            payment = process_coins()
            
            # Check if payment is sufficient
            if is_transaction_successful(payment, drink["cost"]):
                # Make and serve the coffee
                make_coffee(choice, drink["ingredients"])