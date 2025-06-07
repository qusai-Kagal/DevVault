# Angela Yu's 100 Days of Code Challenge - Day 19
# Turtle Race Game with Betting System
# Create 6 racing turtles and let user bet on the winner

# Import required libraries
import turtle
from turtle import Turtle, Screen
import random

# GAME SETUP - Initialize race variables and screen
is_race_on = False  # Flag to control race loop
screen = Screen()  # Create the race track screen
screen.setup(width=500, height=400)  # Set screen dimensions (500x400 pixels)

# USER INPUT - Get player's bet before race starts
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: red/orange/yellow/green/blue/purple: ")

# RACE CONFIGURATION - Define turtle properties
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # 6 different turtle colors
y_positions = [-70, -40, -10, 20, 50, 80]  # Vertical positions for each turtle lane
all_turtles = []  # List to store all racing turtle objects

# TURTLE CREATION - Create and position 6 racing turtles
for turtle_index in range(0, 6):  # Loop through 6 turtles
    new_turtle = Turtle(shape="turtle")  # Create new turtle with turtle shape
    new_turtle.color(colors[turtle_index])  # Set turtle color from colors list
    new_turtle.penup()  # Lift pen so turtle doesn't draw while moving
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Position turtle at starting line
    all_turtles.append(new_turtle)  # Add turtle to race participants list

# RACE START CONDITION - Begin race if user made a bet
if user_bet:  # Only start race if user entered a bet
    is_race_on = True  # Set race flag to True to start main game loop

# MAIN RACE LOOP - Continue until a turtle wins
while is_race_on:

    # Move each turtle in the race
    for turtle in all_turtles:  # Loop through all racing turtles

        # CHECK WIN CONDITION - Has any turtle crossed the finish line?
        if turtle.xcor() > 230:  # If turtle's x-coordinate exceeds finish line (230 pixels)
            is_race_on = False  # Stop the race
            winning_color = turtle.pencolor()  # Get the color of winning turtle

            # DETERMINE WINNER - Check if user's bet was correct
            if winning_color == user_bet:  # User bet on winning turtle
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:  # User bet on losing turtle
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # TURTLE MOVEMENT - Move turtle forward by random distance
        rand_distance = random.randint(0, 10)  # Generate random movement (0-10 pixels)
        turtle.forward(rand_distance)  # Move turtle forward by random amount

# PROGRAM EXIT - Keep window open until user clicks
screen.exitonclick()  # Wait for mouse click to close the game window

# GAME RULES SUMMARY:
# 1. Enter a color to bet on (red, orange, yellow, green, blue, purple)
# 2. Watch the 6 turtles race across the screen
# 3. First turtle to cross the finish line wins
# 4. Check if your bet was correct!
# 5. Click screen to exit when race is finished