from turtle import Turtle
from food import Food


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"points:{self.score}", move=False, align='center', font=('Verdana', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align='center', font=('Verdana', 15, 'normal'))

    def current_score(self):
        self.score += 1
        self.update_score()
