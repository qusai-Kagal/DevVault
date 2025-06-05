# Angela Yu's 100 Days of Code Challenge - Day 18
# Hirst-Style Dot Painting using Turtle Graphics
# Extract colors from famous paintings and create dot art

# Import required libraries for color extraction (commented out as already extracted)
# import colorgram
# from jinja2.runtime import new_context

# CODE TO EXTRACT COLORS FROM IMAGE (Run this first to get color palette)
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)  # Extract 30 most common colors
# for color in colors:
#     r = color.rgb.r  # Red component
#     g = color.rgb.g  # Green component
#     b = color.rgb.b  # Blue component
#     new_color = (r, g, b)  # Create RGB tuple
#     rgb_colors.append(new_color)  # Add to color list
#
# print(rgb_colors)  # Print extracted colors for use in painting

# =============================================================================
# VERSION 1: YOUR IMPLEMENTATION (More organised and readable)
# =============================================================================

from turtle import Turtle, Screen
import random

# Color palette extracted from a Hirst painting using colorgram
color_list = [(234, 232, 220), (47, 45, 45), (28, 35, 52), (185, 155, 128), (25, 106, 165), (225, 236, 226),
              (126, 71, 50), (216, 227, 233), (48, 44, 47), (131, 166, 191), (189, 12, 6), (210, 154, 21),
              (14, 55, 136), (232, 205, 103), (186, 11, 33), (180, 151, 160), (237, 223, 228), (228, 78, 56),
              (129, 61, 86), (212, 66, 101), (8, 37, 20), (42, 123, 84), (29, 160, 199), (9, 99, 66), (238, 170, 158),
              (136, 175, 158), (100, 121, 169), (223, 172, 186), (175, 187, 217), (159, 204, 215)]


def create_hirst_painting():
    """
    Create a Hirst-style dot painting with 10x10 grid of coloured dots
    Each dot is randomly coloured from the extracted palette
    """

    # Setup screen with proper dimensions and background
    screen = Screen()
    screen.colormode(255)  # Use RGB values (0-255) instead of default (0-1)
    screen.bgcolor("white")  # Clean white background
    screen.setup(600, 600)  # Square canvas 600x600 pixels
    screen.title("Hirst Style Dot Painting")

    # Create and configure turtle for drawing dots
    dot_artist = Turtle()
    dot_artist.speed("fastest")  # Maximum drawing speed
    dot_artist.hideturtle()  # Hide turtle cursor for cleaner look
    dot_artist.penup()  # Lift pen - we only want dots, no connecting lines

    # Calculate starting position to center the 10x10 grid
    start_x = -225  # Left edge of grid (centered on 600px canvas)
    start_y = 225  # Top edge of grid

    # Create 10x10 grid using nested loops
    for row in range(10):  # 10 rows from top to bottom
        for col in range(10):  # 10 columns from left to right

            # Calculate exact position for current dot
            x = start_x + col * 50  # Move right by 50 units for each column
            y = start_y - row * 50  # Move down by 50 units for each row

            # Move turtle to calculated position
            dot_artist.goto(x, y)

            # Select random color from extracted palette
            random_color = random.choice(color_list)
            dot_artist.color(random_color)

            # Draw filled circular dot
            dot_artist.pendown()  # Put pen down to draw
            dot_artist.begin_fill()  # Start filling shape
            dot_artist.circle(10)  # Draw circle with radius 10 (diameter 20)
            dot_artist.end_fill()  # Finish filling
            dot_artist.penup()  # Lift pen for next movement

    # Add title to the artwork
    dot_artist.goto(-100, 280)  # Position above the grid
    dot_artist.color("black")
    dot_artist.write("Hirst Style Dot Painting", font=("Arial", 14, "bold"))

    # Print completion message with specs
    print("🎨 Hirst painting complete!")
    print("Grid: 10x10 | Dot size: 20 | Spacing: 50")

    # Keep window open until clicked
    screen.exitonclick()


# Run the painting function
if __name__ == "__main__":
    create_hirst_painting()

# =============================================================================
# VERSION 2: COURSE IMPLEMENTATION (Angela Yu's approach)
# =============================================================================

import turtle as turtle_module  # Import with alias for clarity
import random

# Configure turtle to use RGB color mode (0-255)
turtle_module.colormode(255)

# Create and configure turtle
tim = turtle_module.Turtle()
tim.speed("fastest")  # Maximum speed for quick drawing
tim.penup()  # Lift pen - no lines, only dots
tim.hideturtle()  # Hide turtle for cleaner appearance

# Same color palette as Version 1
color_list = [(234, 232, 220), (47, 45, 45), (28, 35, 52), (185, 155, 128), (25, 106, 165), (225, 236, 226),
              (126, 71, 50), (216, 227, 233), (48, 44, 47), (131, 166, 191), (189, 12, 6), (210, 154, 21),
              (14, 55, 136), (232, 205, 103), (186, 11, 33), (180, 151, 160), (237, 223, 228), (228, 78, 56),
              (129, 61, 86), (212, 66, 101), (8, 37, 20), (42, 123, 84), (29, 160, 199), (9, 99, 66), (238, 170, 158),
              (136, 175, 158), (100, 121, 169), (223, 172, 186), (175, 187, 217), (159, 204, 215)]

# Position turtle at bottom-left corner of the grid
tim.setheading(225)  # Point turtle to bottom-left diagonal
tim.forward(300)  # Move to starting position (bottom-left)
tim.setheading(0)  # Point turtle to the right (east)

# Total number of dots to draw (10 rows × 10 columns)
number_of_dots = 100

# Main drawing loop - create dots in rows
for dot_count in range(1, number_of_dots + 1):
    # Draw dot with random color from palette
    tim.dot(20, random.choice(color_list))  # 20 pixel diameter dot
    tim.forward(50)  # Move 50 units right for next dot

    # Check if we've completed a row (every 10 dots)
    if dot_count % 10 == 0:
        # Move to start of next row
        tim.setheading(90)  # Point upward (north)
        tim.forward(50)  # Move up 50 units to next row
        tim.setheading(180)  # Point left (west)
        tim.forward(500)  # Move back to left edge (10 dots × 50 units)
        tim.setheading(0)  # Point right again for next row

# Create screen and wait for click to close
screen = turtle_module.Screen()
screen.exitonclick()  # Close window when clicked

# =============================================================================
# KEY DIFFERENCES BETWEEN VERSIONS:
#
# Version 1 (Your Implementation):
# - Uses nested loops (more intuitive for grid creation)
# - Calculates exact x,y positions for each dot
# - Includes function structure and documentation
# - Centers grid on screen
# - Adds title and completion message
#
# Version 2 (Course Implementation):
# - Uses single loop with modulo operator for row detection
# - Moves turtle sequentially (more like drawing by hand)
# - Starts from bottom-left corner
# - More compact but less readable for beginners
#
# Both create identical 10×10 grids with 20px dots spaced 50px apart!
# =============================================================================