from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')      # Set text color to white
        self.penup()             # Prevent drawing lines
        self.hideturtle()        # Hide the turtle icon
        self.l_score = 0         # Initialize left player's score
        self.r_score = 0         # Initialize right player's score
        self.update_scoreboard() # Display initial score

    def update_scoreboard(self):
        # Clear previous score and write updated score
        self.clear()
        self.goto(-100, 200)     # Position for left player's score
        self.write(self.l_score, align='center', font=('Arial', 35, 'normal'))
        self.goto(100, 200)      # Position for right player's score
        self.write(self.r_score, align='center', font=('Arial', 35, 'normal'))

    def l_point(self):
        # Increment left player's score and update display
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # Increment right player's score and update display
        self.r_score += 1
        self.update_scoreboard()
