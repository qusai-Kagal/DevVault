import random
import string

# Ask user for password complexity
mode = input("Choose password type: Type 'easy' for ordered or 'hard' for shuffled: ").lower()

# Ask how many characters of each type
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# Character pools
letters = list(string.ascii_letters)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = list(string.digits)

# Generate random characters
password_letters = [random.choice(letters) for _ in range(num_letters)]
password_symbols = [random.choice(symbols) for _ in range(num_symbols)]
password_numbers = [random.choice(numbers) for _ in range(num_numbers)]

# Combine all characters
password_chars = password_letters + password_symbols + password_numbers

# Decide output based on mode
if mode == 'hard':
    random.shuffle(password_chars)
    password = ''.join(password_chars)
else:
    # Default to easy if not 'hard'
    password = ''.join(password_letters + password_symbols + password_numbers)

print("Your password is:", password)
