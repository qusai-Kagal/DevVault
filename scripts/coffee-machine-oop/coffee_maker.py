class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        """Initialize the coffee maker with starting resources."""
        # Dictionary to store the current amounts of each resource
        # These are the initial quantities when the machine starts
        self.resources = {
            "water": 300,  # Starting water amount in milliliters
            "milk": 200,  # Starting milk amount in milliliters
            "coffee": 100,  # Starting coffee amount in grams
        }

    def report(self):
        """Prints a report of all resources."""
        # Display current resource levels to the user
        # This is called when user types "report"
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # Assume we can make the drink initially
        can_make = True

        # Loop through each ingredient required for the drink
        for item in drink.ingredients:
            # Check if we need more of this ingredient than we have available
            if drink.ingredients[item] > self.resources[item]:
                # Not enough of this ingredient - inform user and mark as unable to make
                print(f"Sorry there is not enough {item}.")
                can_make = False

        # Return True only if ALL ingredients are sufficient
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        # Loop through each ingredient needed for this drink
        for item in order.ingredients:
            # Subtract the required amount from our available resources
            # This reduces our stock after making the drink
            self.resources[item] -= order.ingredients[item]

        # Confirm to user that their drink is ready
        print(f"Here is your {order.name} ☕️. Enjoy!")