import turtle as t  # Import turtle module and alias it as 't'
import random       # For generating random colors

timmy = t.Turtle()  # Create a turtle object named timmy
t.colormode(255)    # Enable RGB color mode (values from 0 to 255)

# Function to generate a random RGB color
def random_color():
    r = random.randint(0, 255)  # Red component
    g = random.randint(0, 255)  # Green component
    b = random.randint(0, 255)  # Blue component
    color = (r, g, b)
    return color

# Set turtle speed to the fastest for smooth drawing
timmy.speed(0)

# Function to draw a spirograph pattern
def draw_spirograph(size_of_gap):
    # Draw 360 degrees worth of circles, with each one rotated by 'size_of_gap'
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())  # Pick a random color
        timmy.circle(100)            # Draw a circle with radius 100
        # Change the turtle's heading so the next circle is rotated
        timmy.setheading(timmy.heading() + size_of_gap)

# Call the function with a 5-degree gap between circles
draw_spirograph(5)

# Keep the screen open until the user clicks
my_screen = t.Screen()
print(my_screen.canvheight)  # Optional: print the canvas height
my_screen.exitonclick()
