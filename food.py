from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
