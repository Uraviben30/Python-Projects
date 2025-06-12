from turtle import Turtle
import random

# Predefined car colors
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial car speed and speed increment per level
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []                  # List to store all car instances
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial car speed

    def create_car(self):
        # Randomly generate a car (1 in 6 chance per loop iteration)
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch to make it look like a car
            new_car.penup()
            new_car.color(random.choice(COLORS))             # Assign a random color
            random_y = random.randint(-250, 250)             # Random vertical position
            new_car.goto(300, random_y)                      # Start from the right edge
            self.all_cars.append(new_car)                    # Add to car list

    def move_cars(self):
        # Move all cars leftward based on current speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase speed to make the game harder
        self.car_speed += MOVE_INCREMENT
