# Angela Yu's 100 Days of Code Challenge - Day 18 (Part 1)
# Drawing Multiple Shapes with Different Colors
# Practice with loops, functions, and color randomization

# =============================================================================
# VERSION 1: YOUR IMPLEMENTATION (More structured and detailed)
# =============================================================================

def create_your_version_shapes():
    """
    Your implementation using RGB colors and explicit shape definitions
    Features: RGB color generation, named shapes, detailed structure
    """
    from turtle import Turtle, Screen
    import random

    def draw_shape(turtle_obj, num_sides):
        """
        Draw a polygon with specified number of sides

        Args:
            turtle_obj: The turtle object to draw with
            num_sides: Number of sides for the polygon
        """
        angle = 360 / num_sides  # Calculate interior angle for regular polygon
        for _ in range(num_sides):
            turtle_obj.forward(100)  # Move forward 100 units
            turtle_obj.right(angle)  # Turn by calculated angle

    def random_color():
        """
        Generate random RGB color tuple

        Returns:
            tuple: (r, g, b) values between 0-255
        """
        r = random.randint(0, 255)  # Random red component
        g = random.randint(0, 255)  # Random green component
        b = random.randint(0, 255)  # Random blue component
        return (r, g, b)

    # Create and configure turtle
    tim = Turtle()
    tim.shape("turtle")  # Use turtle cursor shape
    tim.speed("fastest")  # Maximum drawing speed

    # Setup screen for RGB color mode
    screen = Screen()
    screen.colormode(255)  # Enable RGB values (0-255)
    screen.title("Version 1: Your Implementation - RGB Colors")

    # List of shapes with names and side counts
    # More descriptive and educational approach
    shapes = [
        ("triangle", 3),  # 3-sided polygon
        ("square", 4),  # 4-sided polygon
        ("pentagon", 5),  # 5-sided polygon
        ("hexagon", 6),  # 6-sided polygon
        ("heptagon", 7),  # 7-sided polygon
        ("octagon", 8),  # 8-sided polygon
        ("nonagon", 9),  # 9-sided polygon
        ("decagon", 10)  # 10-sided polygon
    ]

    print("🎯 Drawing shapes with RGB colors...")

    # Draw all shapes with random RGB colors
    for shape_name, sides in shapes:
        tim.color(random_color())  # Set random RGB color
        print(f"Drawing {shape_name} ({sides} sides)")
        draw_shape(tim, sides)  # Draw the shape

    print("✅ Version 1 complete! Click to close and continue...")
    screen.exitonclick()  # Wait for click to close


# =============================================================================
# VERSION 2: COURSE IMPLEMENTATION (Angela Yu's approach)
# =============================================================================

def create_course_version_shapes():
    """
    Course implementation using predefined color names and range loop
    Features: Named colors, compact loop structure, simpler approach
    """
    import turtle as t
    import random

    # Create turtle object
    tim = t.Turtle()
    tim.speed("fastest")  # Maximum drawing speed

    # Setup screen
    screen = t.Screen()
    screen.title("Version 2: Course Implementation - Named Colors")

    # Predefined list of color names (Turtle's built-in colors)
    # More limited but consistent color palette
    colors = [
        "CornflowerBlue",  # Light blue
        "DarkOrchid",  # Purple
        "IndianRed",  # Red-brown
        "DeepSkyBlue",  # Bright blue
        "LightSeaGreen",  # Teal
        "wheat",  # Light brown
        "SlateGray",  # Gray
        "SeaGreen"  # Green
    ]

    def draw_shape(num_sides):
        """
        Draw a polygon with specified number of sides
        Uses the global tim turtle object

        Args:
            num_sides: Number of sides for the polygon
        """
        angle = 360 / num_sides  # Calculate turning angle
        for _ in range(num_sides):
            tim.forward(100)  # Move forward 100 units
            tim.right(angle)  # Turn right by calculated angle

    print("🎯 Drawing shapes with named colors...")

    # Draw shapes from triangle (3 sides) to decagon (10 sides)
    # Uses range() for more compact code
    for shape_side_n in range(3, 11):  # 3 to 10 sides
        tim.color(random.choice(colors))  # Pick random color from list
        print(f"Drawing {shape_side_n}-sided polygon")
        draw_shape(shape_side_n)  # Draw the current shape

    print("✅ Version 2 complete! Click to close...")
    screen.exitonclick()  # Wait for click to close


# =============================================================================
# MAIN EXECUTION - RUN BOTH VERSIONS CONSECUTIVELY
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("SHAPE DRAWING CHALLENGE - DAY 18 (PART 1)")
    print("Drawing polygons from triangle to decagon")
    print("=" * 60)

    # Version 1: Your structured implementation
    print("\n🎯 Starting Version 1 (Your Implementation)...")
    print("Features: RGB colors, named shapes, detailed structure")
    create_your_version_shapes()

    print("\n✅ Version 1 complete!")
    print("\n🎯 Starting Version 2 (Course Implementation)...")
    print("Features: Named colors, compact loops, simpler approach")

    # Version 2: Course implementation
    create_course_version_shapes()

    print("\n✅ Both versions complete!")
    print("🎨 You've successfully drawn 16 colorful polygons!")
    print("=" * 60)

# =============================================================================
# KEY DIFFERENCES BETWEEN VERSIONS:
#
# Version 1 (Your Implementation):
# - Uses RGB color generation (0-255 values)
# - Explicit shape names in tuples for clarity
# - More structured with detailed comments
# - Separate random_color() function
# - Educational approach with shape names
#
# Version 2 (Course Implementation):
# - Uses predefined named colors (turtle built-ins)
# - Compact range loop (3 to 11)
# - More concise and direct
# - Global turtle usage in function
# - Simpler but effective approach
#
# Both create the same 8 shapes (triangle through decagon) with random colors!
# The key learning: There are multiple ways to solve the same problem!
# =============================================================================