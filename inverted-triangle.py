# Program: Draw an Inverted Triangle Pattern
# Features: Takes the height of the triangle as input and prints an inverted triangle pattern using a function.
# Procedure:
# 1. Define a function to draw an inverted triangle pattern of a given height.
# 2. Validate the input to ensure the height is a positive integer.
# 3. Print the pattern if the input is valid; otherwise, handle invalid inputs.

def draw_inverted_triangle(height):
    """Draw an inverted triangle pattern of a given height.

    Args:
        height (int): The height of the inverted triangle.
    """
    for i in range(height, 0, -1):
        print("*" * i)

def get_triangle_height():
    """Get and validate the height of the triangle from user input.

    Returns:
        int: The valid height of the triangle.
    """
    while True:
        try:
            height = int(input("Enter the height of the triangle: "))
            if height > 0:
                return height
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Start of the program
triangle_height = get_triangle_height()
draw_inverted_triangle(triangle_height)
