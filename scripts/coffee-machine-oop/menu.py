class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, water, milk, coffee, cost):
        """Initialize a menu item with its recipe and price."""
        # Store the drink's name (e.g., "latte", "espresso")
        self.name = name

        # Store the price of this drink
        self.cost = cost

        # Create a dictionary containing the recipe for this drink
        # This tells us exactly how much of each ingredient is needed
        self.ingredients = {
            "water": water,  # Amount of water needed in ml
            "milk": milk,  # Amount of milk needed in ml
            "coffee": coffee  # Amount of coffee needed in grams
        }


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        """Initialize the menu with all available drink options."""
        # Create a list of MenuItem objects representing all available drinks
        # Each MenuItem contains the recipe and cost for that specific drink
        self.menu = [
            # Latte: milky coffee drink requiring water, milk, and coffee
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),

            # Espresso: strong coffee shot with no milk
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),

            # Cappuccino: coffee with steamed milk foam
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items as a formatted string."""
        # Start with an empty string to build our options list
        options = ""

        # Loop through each menu item in our menu list
        for item in self.menu:
            # Add the item's name followed by a slash to our options string
            # This creates a format like "latte/espresso/cappuccino/"
            options += f"{item.name}/"

        # Return the complete string of all available options
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        # Loop through each menu item to find a match
        for item in self.menu:
            # Check if the current item's name matches what the user ordered
            if item.name == order_name:
                # Found a match! Return the MenuItem object
                # This gives us access to the drink's ingredients and cost
                return item

        # If we get here, no matching drink was found
        # Inform the user and return None (implicit return)
        print("Sorry that item is not available.")