from turtle import Screen

from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

_snake = Snake()
_food = Food()
_score = Score()

screen.listen()
screen.onkey(_snake.up, "Up")
screen.onkey(_snake.left, "Left")
screen.onkey(_snake.right, "Right")
screen.onkey(_snake.down, "Down")


game_is_on = True
while game_is_on:
    _s_x = _snake.head.xcor()
    _s_y = _snake.head.ycor()
    _snake.move()
    # collision with food
    if _snake.head.distance(_food) < 20:
        _food.refresh()
        _score.increase_score()
        _snake.eat_food()

    # wall collision detection
    if _s_x > 270 or _s_x < -270 or _s_y > 250 or _s_y < -270:
        game_is_on = False
        _score.game_over()

    # tail collision detection
    for segment in _snake.segments[1:]:
        if _snake.head.distance(segment) < 10:
            game_is_on = False
            _score.game_over()

screen.exitonclick()
