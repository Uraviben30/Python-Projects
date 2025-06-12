from turtle import Turtle

# Font style used for displaying text on the screen
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1                   # Start at level 1
        self.hideturtle()               # Hide the turtle icon
        self.penup()                    # Don't draw lines
        self.goto(-280, 250)            # Position the level display at the top-left corner
        self.update_scoreboard()        # Show the initial level

    def update_scoreboard(self):
        # Clear previous text and display the current level
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        # Increase the level by 1 and update the display
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        # Display "GAME OVER" message at the center of the screen
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
