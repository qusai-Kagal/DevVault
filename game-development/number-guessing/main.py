# Number Guessing Game
# Angela Yu - Day 11 - 100 Days of Code
# A simple guessing game where the user tries to guess a random number between 1-100

from random import randint
from art import logo

# Constants for game difficulty levels
EASY_LEVEL_TURNS = 10  # Number of attempts for easy mode
HARD_LEVEL_TURNS = 5   # Number of attempts for hard mode


def check_answer(user_guess, actual_answer, turns):
    """
    Checks the user's guess against the actual answer and provides feedback.
    
    Args:
        user_guess (int): The number guessed by the user
        actual_answer (int): The correct answer
        turns (int): Current number of turns remaining
    
    Returns:
        int: Updated number of turns remaining (reduced by 1 if guess is wrong)
        None: If the guess is correct (game ends)
    """
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1  # Reduce turns and return updated count
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1  # Reduce turns and return updated count
    else:
        # Correct guess - print success message and don't return anything
        print(f"You got it! The answer was {actual_answer}")


def set_difficulty():
    """
    Prompts the user to choose a difficulty level and returns the corresponding number of turns.
    
    Returns:
        int: Number of turns based on difficulty (10 for easy, 5 for hard)
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS  # Defaults to hard if anything other than 'easy' is entered


def game():
    """
    Main game function that handles the entire game flow.
    Sets up the game, manages the guessing loop, and determines win/lose conditions.
    """
    # Display game logo and welcome message
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number between 1 and 100 (inclusive)
    answer = randint(1, 100)
    
    # Debug line - shows the answer (should be removed in production)
    print(f"Pssst, the correct answer is {answer}")

    # Get the number of turns based on difficulty selection
    turns = set_difficulty()

    # Initialize guess variable for the game loop
    guess = 0
    
    # Main game loop - continues until correct guess or runs out of turns
    while guess != answer:
        # Show remaining attempts to the user
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Get user's guess and convert to integer
        guess = int(input("Make a guess: "))
        
        # Check the guess and update remaining turns
        turns = check_answer(guess, answer, turns)
        
        # Check if player has run out of turns
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return  # Exit the function (end game)
        elif guess != answer:
            # If guess is wrong but still have turns, prompt to guess again
            print("Guess again.")


# Start the game
game()