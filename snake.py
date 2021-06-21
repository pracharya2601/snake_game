from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SPEED = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        _t = Turtle("square")
        _t.color("white")
        _t.penup()
        _t.goto(pos)
        self.segments.append(_t)

    def eat_food(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            _x = self.segments[seg_num - 1].xcor()
            _y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(_x, _y)
        self.segments[0].forward(SNAKE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.forward(SNAKE_SPEED)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.forward(SNAKE_SPEED)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.forward(SNAKE_SPEED)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.forward(SNAKE_SPEED)
