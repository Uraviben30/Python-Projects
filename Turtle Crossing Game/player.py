from turtle import Turtle

# Constants for player's behavior and movement
STARTING_POSITION = (0, -280)  # Starting location at bottom center
MOVE_DISTANCE = 10             # Distance moved per key press
FINISH_LINE_Y = 280            # Y-coordinate threshold for winning

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")     # Set the player shape to a turtle
        self.penup()             # Prevent drawing lines while moving
        self.go_to_start()       # Place player at the starting position
        self.setheading(90)      # Face the turtle upwards

    def go_up(self):
        # Move the player up by a fixed distance
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Reset the player back to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the player has reached the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
