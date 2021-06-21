from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('grey')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", False, align='center', font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align='center', font=("Arial", 20, "normal"))
