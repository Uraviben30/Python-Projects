from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")                      # Paddle shape
        self.color("white")                       # Paddle color
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make the paddle tall and thin
        self.penup()                              # Prevent drawing lines
        self.goto(position)                       # Place paddle at starting position

    def go_up(self):
        # Move paddle up by 20 pixels
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # Move paddle down by 20 pixels
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
