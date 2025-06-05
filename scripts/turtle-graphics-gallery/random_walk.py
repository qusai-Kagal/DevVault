# Angela Yu's 100 Days of Code Challenge - Day 18 (Part 2)
# Random Walk Art with Turtle Graphics
# Simulating random movement with colorful thick lines

# =============================================================================
# VERSION 1: YOUR IMPLEMENTATION (More structured and detailed)
# =============================================================================

def create_your_version_random_walk():
    """
    Your implementation with clear structure and screen setup
    Features: Explicit screen setup, turtle shape, organised imports
    """
    from turtle import Turtle, Screen
    import random

    def random_color():
        """
        Generate a random RGB color tuple

        Returns:
            tuple: (r, g, b) with values between 0-255
        """
        r = random.randint(0, 255)  # Random red component
        g = random.randint(0, 255)  # Random green component
        b = random.randint(0, 255)  # Random blue component
        return (r, g, b)

    # Create and configure turtle
    tim = Turtle()
    tim.shape("turtle")  # Use turtle cursor for visibility
    tim.speed("fastest")  # Maximum drawing speed
    tim.pensize(10)  # Thick line (10 pixels wide)

    # Setup screen with proper configuration
    screen = Screen()
    screen.colormode(255)  # Enable RGB values (0-255)
    screen.bgcolor("black")  # Black background for better contrast
    screen.title("Version 1: Your Implementation - Random Walk")
    screen.setup(800, 600)  # Set window size

    # Define possible movement directions (in degrees)
    # 0° = East, 90° = North, 180° = West, 270° = South
    directions = [0, 90, 180, 270]

    print("🎯 Starting random walk with turtle shape...")
    print("Watch the turtle create colorful random paths!")

    # Perform random walk with 200 steps
    for step in range(200):
        tim.color(random_color())  # Set random color for this step
        tim.forward(30)  # Move forward 30 units
        tim.setheading(random.choice(directions))  # Turn to random direction

        # Print progress every 50 steps
        if (step + 1) % 50 == 0:
            print(f"Completed {step + 1}/200 steps")

    print("✅ Random walk complete! Click to close and continue...")
    screen.exitonclick()  # Wait for click to close


# =============================================================================
# VERSION 2: COURSE IMPLEMENTATION (Angela Yu's approach)
# =============================================================================

def create_course_version_random_walk():
    """
    Course implementation with compact structure
    Features: Module-level colormode, thicker pen, minimal setup
    """
    import turtle as t
    import random

    # Create turtle object
    tim = t.Turtle()

    # Set color mode at module level (more compact)
    t.colormode(255)  # Enable RGB values (0-255)

    # Setup screen
    screen = t.Screen()
    screen.bgcolor("white")  # White background (default)
    screen.title("Version 2: Course Implementation - Random Walk")
    screen.setup(800, 600)  # Set window size

    def random_color():
        """
        Generate a random RGB color tuple
        Course version with local variable for clarity

        Returns:
            tuple: (r, g, b) with values between 0-255
        """
        r = random.randint(0, 255)  # Random red component
        g = random.randint(0, 255)  # Random green component
        b = random.randint(0, 255)  # Random blue component
        ran_color = (r, g, b)  # Store in variable for clarity
        return ran_color  # Return the color tuple

    # Define movement directions (cardinal directions only)
    # Each direction is 90° apart for perpendicular movements
    directions = [0, 90, 180, 270]

    # Configure turtle drawing properties
    tim.pensize(15)  # Even thicker line (15 pixels wide)
    tim.speed("fastest")  # Maximum drawing speed
    # Note: No turtle shape set - uses default arrow

    print("🎯 Starting random walk with thicker lines...")
    print("Creating abstract art through random movement!")

    # Execute random walk algorithm
    for step in range(200):  # 200 random steps
        tim.color(random_color())  # Apply random color
        tim.forward(30)  # Move 30 units forward
        tim.setheading(random.choice(directions))  # Choose random direction

        # Print progress every 40 steps
        if (step + 1) % 40 == 0:
            print(f"Progress: {step + 1}/200 steps completed")

    print("✅ Course version complete! Click to close...")
    screen.exitonclick()  # Wait for click to close


# =============================================================================
# MAIN EXECUTION - RUN BOTH VERSIONS CONSECUTIVELY
# =============================================================================

if __name__ == "__main__":
    print("=" * 65)
    print("RANDOM WALK ART CHALLENGE - DAY 18 (PART 2)")
    print("Creating abstract art through random turtle movement")
    print("Each version takes 200 random steps with thick colorful lines")
    print("=" * 65)

    # Version 1: Your structured implementation
    print("\n🎯 Starting Version 1 (Your Implementation)...")
    print("Features: Turtle shape, 10px pen, black background, structured setup")
    create_your_version_random_walk()

    print("\n✅ Version 1 complete!")
    print("\n🎯 Starting Version 2 (Course Implementation)...")
    print("Features: Arrow cursor, 15px pen, white background, compact code")

    # Version 2: Course implementation
    create_course_version_random_walk()

    print("\n✅ Both versions complete!")
    print("🎨 You've created two unique random walk artworks!")
    print("Notice how randomness creates different patterns each time!")
    print("=" * 65)

# =============================================================================
# RANDOM WALK ALGORITHM EXPLANATION:
#
# What is a Random Walk?
# - A mathematical concept where each step is randomly determined
# - In this case: turtle moves 30 units forward, then randomly turns
# - Creates unpredictable, organic-looking paths
# - Used in physics, biology, economics, and computer graphics
#
# Key Components:
# 1. Fixed step size (30 units) - consistent movement distance
# 2. Random direction choice from [0°, 90°, 180°, 270°]
# 3. Color changes with each step for visual appeal
# 4. Thick pen size creates bold, visible paths
#
# Artistic Result:
# - Creates abstract, maze-like patterns
# - Each run produces completely different artwork
# - Demonstrates how simple rules can create complex beauty
# - Shows the intersection of mathematics and art
# =============================================================================

# =============================================================================
# KEY DIFFERENCES BETWEEN VERSIONS:
#
# Version 1 (Your Implementation):
# - Explicit Screen() object creation and configuration
# - Turtle shape set to "turtle" for visibility
# - 10px pen thickness
# - Black background for contrast
# - More structured import and setup
# - Clear variable organization
#
# Version 2 (Course Implementation):
# - Module-level colormode setting (t.colormode)
# - Default arrow cursor (no shape set)
# - Thicker 15px pen for bolder lines
# - White background (default)
# - More compact code structure
# - Local variable in random_color() for clarity
#
# Both create fascinating random walk art, but with different visual styles!
# The randomness ensures each execution creates unique artwork.
# =============================================================================