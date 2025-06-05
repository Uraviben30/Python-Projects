import turtle as t  # Import turtle module and give it an alias 't'
import random       # Import random module for generating randomness

timmy = t.Turtle()  # Create a turtle named timmy
t.colormode(255)    # Set color mode to RGB (0–255 values)

# Function to generate a random RGB color
def random_color():
    r = random.randint(0, 255)  # Red component
    g = random.randint(0, 255)  # Green component
    b = random.randint(0, 255)  # Blue component
    random_color = (r, g, b)
    return random_color

# Possible directions the turtle can face (right, up, left, down)
directions = [0, 90, 180, 270]

timmy.pensize(15)       # Make the pen thick so the lines are bold
timmy.speed("fastest")  # Set speed to fastest for smooth drawing

# Make the turtle do 200 steps in random directions with random colors
for _ in range(200):
    timmy.color(random_color())                # Set a random color for each move
    timmy.forward(20)                          # Move forward
    timmy.setheading(random.choice(directions))  # Turn in a random cardinal direction
