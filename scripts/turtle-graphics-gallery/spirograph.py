# Angela Yu's 100 Days of Code Challenge - Day 18 (Part 3)
# Spirograph Art with Turtle Graphics
# Creating beautiful geometric patterns using circles and rotation

# =============================================================================
# VERSION 1: YOUR FRACTAL TREE IMPLEMENTATION (Advanced Bonus)
# =============================================================================

def create_fractal_tree_version():
    """
    Your advanced implementation: Beautiful recursive fractal tree
    This goes beyond the basic spirograph and shows advanced turtle techniques
    """
    from turtle import Turtle, Screen
    import colorsys
    import math

    def hsv_color(hue):
        """
        Generate color using HSV color space for smooth transitions
        HSV (Hue, Saturation, Value) provides better color control than RGB

        Args:
            hue: Hue value (0.0 to 1.0) representing color on color wheel

        Returns:
            tuple: RGB color tuple (r, g, b) with values 0-255
        """
        # Convert HSV to RGB with full saturation and brightness
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        # Scale RGB values from 0-1 to 0-255 range
        return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

    def draw_fractal_tree(turtle_obj, length, depth, angle_variation=25):
        """
        Draw a beautiful recursive fractal tree using recursion

        Args:
            turtle_obj: Turtle object to draw with
            length: Length of current branch segment
            depth: Recursion depth (how many branch levels to draw)
            angle_variation: Angle between left and right branches (degrees)
        """
        # Base case: stop recursion when depth reaches 0
        if depth == 0:
            # At branch tips, draw small circular leaves/flowers
            turtle_obj.color(hsv_color(0.3))  # Green hue for leaves
            turtle_obj.circle(3)  # Small 3-pixel radius circle
            return

        # Color progression: brown trunk → brown branches → colorful tips
        if depth > 6:
            hue = 0.1  # Brown for main trunk
        elif depth > 3:
            hue = 0.08  # Darker brown for major branches
        else:
            # Transition to colorful tips (purple/blue spectrum)
            hue = 0.6 - (depth * 0.1)

        turtle_obj.color(hsv_color(hue))

        # Branch thickness: thicker at base, thinner at tips
        turtle_obj.pensize(max(1, depth))  # Minimum pen size of 1

        # Draw current branch segment
        turtle_obj.forward(length)

        # Save current state for backtracking after drawing sub-branches
        current_pos = turtle_obj.pos()  # Remember position
        current_heading = turtle_obj.heading()  # Remember direction

        # Draw LEFT sub-branch
        turtle_obj.left(angle_variation)  # Turn left
        # Recursive call: shorter length, reduced depth
        draw_fractal_tree(turtle_obj, length * 0.75, depth - 1, angle_variation)

        # Return to branch point for right sub-branch
        turtle_obj.penup()
        turtle_obj.goto(current_pos)  # Return to saved position
        turtle_obj.setheading(current_heading)  # Restore direction
        turtle_obj.pendown()

        # Draw RIGHT sub-branch
        turtle_obj.right(angle_variation)  # Turn right
        # Recursive call: shorter length, reduced depth
        draw_fractal_tree(turtle_obj, length * 0.75, depth - 1, angle_variation)

        # Return to original state (clean up)
        turtle_obj.penup()
        turtle_obj.goto(current_pos)
        turtle_obj.setheading(current_heading)
        turtle_obj.pendown()

    def create_beautiful_tree():
        """Create a stunning fractal tree masterpiece"""
        # Screen setup with dramatic black background
        screen = Screen()
        screen.bgcolor("black")  # Black background for contrast
        screen.colormode(255)  # Enable RGB color mode
        screen.setup(800, 800)  # Square canvas
        screen.title("Version 1: Advanced Fractal Tree Art")

        # Create and configure turtle
        tree_artist = Turtle()
        tree_artist.speed("fastest")  # Maximum drawing speed
        tree_artist.hideturtle()  # Hide cursor for cleaner look

        # Position turtle at bottom center, pointing upward
        tree_artist.penup()
        tree_artist.goto(0, -300)  # Bottom center of screen
        tree_artist.setheading(90)  # Point straight up (north)
        tree_artist.pendown()

        print("🌳 Drawing recursive fractal tree...")
        print("This demonstrates advanced recursion and color theory!")

        # Draw the magnificent tree with these parameters:
        # - Initial length: 120 pixels
        # - Recursion depth: 9 levels
        # - Branch angle: 30 degrees
        draw_fractal_tree(tree_artist, 120, 9, 30)

        # Add artistic title text
        tree_artist.penup()
        tree_artist.goto(-150, 320)
        tree_artist.color("white")
        tree_artist.write("Recursive Fractal Tree", font=("Arial", 18, "bold"))

        tree_artist.goto(-100, 290)
        tree_artist.write("Computer Science Beauty", font=("Arial", 12, "normal"))

        print("✅ Fractal tree complete! Click to close and see spirograph...")
        screen.exitonclick()

    # Execute the tree creation
    create_beautiful_tree()


# =============================================================================
# VERSION 2: COURSE SPIROGRAPH IMPLEMENTATION (Angela Yu's approach)
# =============================================================================

def create_course_spirograph():
    """
    Course implementation: Classic spirograph pattern
    Creates beautiful circular patterns using rotation and circle drawing
    """
    import turtle as t
    import random

    # Create turtle object
    tim = t.Turtle()

    # Enable RGB color mode for full color spectrum
    t.colormode(255)

    # Setup screen
    screen = t.Screen()
    screen.bgcolor("black")  # Dark background for vibrant colors
    screen.title("Version 2: Course Implementation - Spirograph")
    screen.setup(800, 800)

    def random_color():
        """
        Generate completely random RGB color

        Returns:
            tuple: Random RGB color (r, g, b) with values 0-255
        """
        r = random.randint(0, 255)  # Random red component
        g = random.randint(0, 255)  # Random green component
        b = random.randint(0, 255)  # Random blue component
        random_color = (r, g, b)  # Store in variable (course style)
        return random_color

    # Configure turtle for smooth, fast drawing
    tim.speed("fastest")  # Maximum drawing speed

    def draw_spirograph(size_of_gap):
        """
        Draw a complete spirograph pattern

        Args:
            size_of_gap: Angular gap between each circle (degrees)
                        Smaller gaps = more circles = denser pattern
        """
        # Calculate how many circles needed for full rotation
        num_circles = int(360 / size_of_gap)

        print(f"Drawing {num_circles} circles with {size_of_gap}° gaps...")

        # Draw circles in a complete rotation
        for circle_num in range(num_circles):
            tim.color(random_color())  # Random color for each circle
            tim.circle(100)  # Draw circle with 100-pixel radius
            tim.setheading(tim.heading() + size_of_gap)  # Rotate by gap amount

            # Progress indicator every 60 circles
            if (circle_num + 1) % 60 == 0:
                print(f"Progress: {circle_num + 1}/{num_circles} circles")

    print("🎨 Creating spirograph art...")
    print("Watch as overlapping circles create beautiful patterns!")

    # Draw spirograph with 1-degree gaps (360 circles total)
    # Smaller gap = more detailed pattern
    draw_spirograph(1)

    print("✅ Spirograph complete! Click to close...")
    screen.exitonclick()


# =============================================================================
# MAIN EXECUTION - RUN BOTH VERSIONS CONSECUTIVELY
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("ADVANCED TURTLE GRAPHICS CHALLENGE - DAY 18 (PART 3)")
    print("Exploring advanced techniques: Recursion & Geometric Patterns")
    print("=" * 70)

    # Version 1: Advanced fractal tree (your implementation)
    print("\n🎯 Starting Version 1 (Your Advanced Implementation)...")
    print("Features: Recursive fractal tree, HSV colors, mathematical beauty")
    print("This goes beyond basic spirographs to show advanced CS concepts!")
    create_fractal_tree_version()

    print("\n✅ Fractal tree complete!")
    print("\n🎯 Starting Version 2 (Course Spirograph Implementation)...")
    print("Features: Classic spirograph, random colors, geometric patterns")

    # Version 2: Course spirograph implementation
    create_course_spirograph()

    print("\n✅ Both versions complete!")
    print("🎨 You've mastered both recursion and geometric pattern generation!")
    print("From mathematical fractals to classic spirograph art!")
    print("=" * 70)

# =============================================================================
# EDUCATIONAL CONCEPTS DEMONSTRATED:
#
# Version 1 - Fractal Tree (Advanced):
# 🌳 RECURSION: Function calls itself with modified parameters
# 🎨 HSV COLOR SPACE: Better color control than RGB
# 📐 MATHEMATICAL SCALING: Each branch is 75% of parent length
# 🎯 STATE MANAGEMENT: Saving and restoring turtle position/heading
# 🧮 ALGORITHMIC THINKING: Breaking complex shapes into simple rules
#
# Version 2 - Spirograph (Course):
# ⭕ GEOMETRIC PATTERNS: Circles + rotation = beautiful art
# 🔄 ANGULAR MATHEMATICS: 360° rotation divided into equal steps
# 🎲 RANDOMIZATION: Each element gets random color
# 🔢 MODULAR ARITHMETIC: Using remainder (%) for progress tracking
# ⚡ OPTIMIZATION: Calculating exact number of iterations needed
#
# Key Learning:
# - Same turtle graphics foundation can create vastly different art
# - Advanced techniques (recursion) can create sophisticated results
# - Mathematics and programming create beautiful visual art
# - Different approaches solve different creative problems
# =============================================================================

# =============================================================================
# KEY DIFFERENCES BETWEEN VERSIONS:
#
# Version 1 (Your Fractal Tree):
# - Uses advanced recursion algorithms
# - HSV color space for smooth transitions
# - Complex state management (position saving/restoring)
# - Mathematical scaling relationships (0.75 factor)
# - Variable pen thickness based on branch level
# - Demonstrates computer science concepts
#
# Version 2 (Course Spirograph):
# - Simple iterative approach (loop-based)
# - RGB random color generation
# - Straightforward geometric pattern
# - Fixed circle size with angular rotation
# - Classic spirograph mathematical model
# - Demonstrates geometric art principles
#
# Both showcase turtle graphics power but at different complexity levels!
# =============================================================================