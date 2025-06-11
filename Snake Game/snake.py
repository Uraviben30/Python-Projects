from turtle import Turtle

# Initial positions of the three starting segments of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Distance the snake moves forward with each step
MOVE_DISTANCE = 20

# Direction constants (angle in degrees)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # List to hold all segments of the snake
        self.segments = []
        # Create the initial snake body
        self.create_snake()
        # Head of the snake is the first segment
        self.head = self.segments[0]

    def create_snake(self):
        # Create each segment at the starting positions
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Create a new turtle segment and add it to the snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # Move the head of the snake forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change direction to up unless currently moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change direction to down unless currently moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change direction to left unless currently moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change direction to right unless currently moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
