from turtle import Turtle
import random


STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVING_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.AddSegment(position)
            
    def AddSegment(self, position):
            new_segment = Turtle("square")
            new_segment.color("red")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    # def random_color(self):
    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     random_color = (r, g, b)
    #     return random_color
    
    # def snake_color(self):
    #     if self.new_segment:
    #         new_segment.color(self.random_color())
        
    def extend(self):
        self.AddSegment(self.segments[-1].position())
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_FORWARD)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)