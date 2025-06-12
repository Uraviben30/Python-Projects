from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from pongscoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create right and left paddles, ball, and scoreboard
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control ball speed
    screen.update()              # Manually update screen
    ball.move()                  # Move the ball

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Ball goes past right paddle: left player scores
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Ball goes past left paddle: right player scores
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Exit on mouse click
screen.exitonclick()
