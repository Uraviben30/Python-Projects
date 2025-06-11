from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from scoreboard import Scoreboard
import time

# Create the game screen
screen=Screen()
screen.setup(width=600,height=600)  # Set the screen size
screen.bgcolor("black")  # Set the background color
screen.title("Snake Game")  # Set the window title
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Initialize the game objects
snake = Snake()
food=Food()
scoreboard = Scoreboard()

# Set up key controls for snake movement
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Start the game loop
game_is_on=True
while game_is_on:
    screen.update()  # Refresh the screen
    time.sleep(0.1)  # Pause to control the speed of the snake
    snake.move_snake()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move food to a new random location
        snake.extend_()  # Add a new segment to the snake
        scoreboard.increase_score()  # Update the score

    # Detect collision with wall boundaries
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
      game_is_on=False
      scoreboard.game_over()  # End the game

    # Detect collision with tail
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            game_is_on=False
            scoreboard.game_over()  # End the game if head hits its body

# Exit the game on mouse click
screen.exitonclick()
