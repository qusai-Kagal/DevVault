class MoneyMachine:
    """Models a coin-operated payment system for the coffee machine."""

    # Class constants - these values never change and are shared by all instances
    CURRENCY = "$"  # The currency symbol to display

    # Dictionary mapping coin types to their monetary values
    # These represent US coin denominations
    COIN_VALUES = {
        "quarters": 0.25,  # Quarter = 25 cents
        "dimes": 0.10,  # Dime = 10 cents
        "nickles": 0.05,  # Nickel = 5 cents
        "pennies": 0.01  # Penny = 1 cent
    }

    def __init__(self):
        """Initialize the money machine with zero profit and no money received."""
        # Track total profit earned by the machine (cumulative)
        self.profit = 0

        # Track money received for the current transaction (resets after each purchase)
        self.money_received = 0

    def report(self):
        """Prints the current profit earned by the machine."""
        # Display total money earned (like checking the cash register)
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted by the user."""
        # Prompt user to start inserting coins
        print("Please insert coins.")

        # Loop through each type of coin we accept
        for coin in self.COIN_VALUES:
            # Ask user how many of this coin type they're inserting
            # Convert their input to integer, multiply by coin value, and add to total
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]

        # Return the total amount of money collected for this transaction
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        # First, collect coins from the user
        self.process_coins()

        # Check if user inserted enough money for their purchase
        if self.money_received >= cost:
            # Payment successful - calculate change needed
            change = round(self.money_received - cost, 2)  # Round to avoid floating point errors
            print(f"Here is {self.CURRENCY}{change} in change.")

            # Add the drink cost to our total profit (not the extra money they gave us)
            self.profit += cost

            # Reset money received for next customer
            self.money_received = 0

            # Return True to indicate successful payment
            return True

        else:
            # Payment failed - not enough money inserted
            print("Sorry that's not enough money. Money refunded.")

            # Reset money received (simulating refunding their coins)
            self.money_received = 0

            # Return False to indicate failed payment
            return False