from turtle import Turtle, Screen  # Importing turtle graphics and screen control
import random  # For generating random colors

# Create a turtle named timmy and set its drawing speed
timmy = Turtle()
timmy.speed(1)  # Speed 1 is slow, so we can see the shapes being drawn clearly

# List of nice colors to randomly use for the shapes
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Function to draw a shape with 'num_sides' sides
def draw_shape(num_sides):
    angle = 360 / num_sides  # Total degrees in a circle divided by number of sides
    for _ in range(num_sides):
        timmy.forward(100)  # Draw one side of the shape
        timmy.right(angle)  # Turn to draw the next side

# Loop through shapes from triangle (3 sides) to decagon (10 sides)
for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))  # Change to a random color for each shape
    draw_shape(shape_side_n)  # Draw the shape

# Set up the screen so it doesn’t close immediately
my_screen = Screen()
print(my_screen.canvheight)  # Optional: prints the height of the canvas
my_screen.exitonclick()  # Keeps the window open until you click on it
