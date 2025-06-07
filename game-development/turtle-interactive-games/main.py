# Angela Yu's 100 Days of Code Challenge - Day 19
# Turtle Graphics with Keyboard Controls - Etch-A-Sketch
# Control turtle movement using keyboard keys (WASD + Clear function)

# Import turtle graphics library
from turtle import Turtle, Screen

# SETUP - Create turtle instance and screen
tim = Turtle()  # Create our drawing turtle
screen = Screen()  # Create the drawing canvas

# MOVEMENT FUNCTIONS - Define all turtle movement behaviours
def move_forwards():
    """Move turtle forward by 10 units when W key pressed"""
    tim.forward(10)  # Move forward 10 pixels

def move_backwards():
    """Move turtle backward by 10 units when S key pressed"""
    tim.backward(10)  # Move backward 10 pixels

def turn_left():
    """Turn turtle left by 10 degrees when A key pressed"""
    new_heading = tim.heading() + 10  # Get current direction and add 10 degrees
    tim.setheading(new_heading)  # Set new heading direction

def turn_right():
    """Turn turtle right by 10 degrees when D key pressed"""
    new_heading = tim.heading() - 10  # Get current direction and subtract 10 degrees
    tim.setheading(new_heading)  # Set new heading direction

def clear():
    """Clear the screen and reset turtle to home position when C key pressed"""
    tim.clear()    # Clear all drawings from screen
    tim.penup()    # Lift pen to avoid drawing line whilst moving
    tim.home()     # Move turtle back to centre (0, 0) facing east
    tim.pendown()  # Put pen down to resume drawing

# EVENT LISTENING - Set up keyboard controls
screen.listen()                    # Tell screen to start listening for key presses
screen.onkey(move_forwards, "w")   # Bind W key to move forward function
screen.onkey(move_backwards, "s")  # Bind S key to move backward function  
screen.onkey(turn_left, "a")       # Bind A key to turn left function
screen.onkey(turn_right, "d")      # Bind D key to turn right function
screen.onkey(clear, "c")           # Bind C key to clear screen function

# PROGRAM EXIT - Keep window open until user clicks
screen.exitonclick()  # Wait for mouse click to close program

# CONTROLS SUMMARY:
# W = Move Forward    S = Move Backward
# A = Turn Left       D = Turn Right  
# C = Clear Screen    Click = Exit Program