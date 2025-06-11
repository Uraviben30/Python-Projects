from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.score = 0  # Initial score
        self.color("white")  # Set the text color to white
        self.penup()  # Prevent drawing lines when moving
        self.goto(0, 270)  # Position the scoreboard at the top center
        self.update_scoreboard()  # Display the initial score
        self.hideturtle()  # Hide the turtle cursor

    def update_scoreboard(self):
        # Display the current score on the screen
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Display 'Game Over' message at the center of the screen
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Increment the score by 1 and update the display
        self.score += 1
        self.clear()  # Clear the previous score
        self.update_scoreboard()  # Write the updated score
