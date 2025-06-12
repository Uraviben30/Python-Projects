from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")     # Set ball shape
        self.color("white")      # Set ball color
        self.penup()             # Don't draw lines when the ball moves
        self.x_move = 10         # Ball movement in the X direction
        self.y_move = 10         # Ball movement in the Y direction
        self.move_speed = 0.1    # Ball movement speed (lower = faster)

    def move(self):
        # Update ball position based on current direction
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse the Y direction (when hitting top/bottom wall)
        self.y_move *= -1

    def bounce_x(self):
        # Reverse the X direction (when hitting a paddle)
        self.x_move *= -1
        # Increase speed slightly each time it bounces off a paddle
        self.move_speed *= 0.9

    def reset_position(self):
        # Reset ball to center and reset speed
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()  # Start moving in the opposite X direction
