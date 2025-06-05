from turtle import Turtle, Screen
import random

# Flag to control when the race should start
is_race_on = False

# Set up the screen dimensions
screen = Screen()
screen.setup(width=600, height=400)

# Ask the user to place a bet on which turtle will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)  # Optional: just to confirm the input

# List of turtle colors and their respective y-axis positions
colors = ["red", "yellow", "blue", "green", "violet", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []  # Will store all turtle objects

# Create turtles, assign color and position them on the starting line
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()  # So the turtles don't draw lines when moving
    new_turtle.goto(x=-250, y=y_positions[turtle_index])  # Start on the left side of the screen
    all_turtles.append(new_turtle)

# Start the race if user placed a bet
if user_bet:
    is_race_on = True

# Main race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()  # Get the color of the winning turtle

            # Compare with user's bet and print the result
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move turtle forward by a random small distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Keep the screen open until user clicks
screen.exitonclick()
