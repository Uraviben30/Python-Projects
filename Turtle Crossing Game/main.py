import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up keyboard listener for player movement
screen.listen()
screen.onkey(player.go_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)      # Control the game's refresh rate
    screen.update()      # Refresh the screen manually

    car_manager.create_car()  # Randomly generate new cars
    car_manager.move_cars()   # Move all cars forward

    # Detect collision between player and cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False          # End game on collision
            scoreboard.game_over()      # Display "Game Over"

    # Detect if player has successfully crossed
    if player.is_at_finish_line():
        player.go_to_start()            # Move player back to start
        car_manager.level_up()          # Increase car speed
        scoreboard.increase_level()     # Update level display

# Close the screen when user clicks
screen.exitonclick()
