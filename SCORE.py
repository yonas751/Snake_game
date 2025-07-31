from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score}", align="center", font=("Arial", 20, "normal"))
        self.penup()

        self.hideturtle()
    def increase_score(self):

        self.score +=1
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 20, "normal"))
    def game_over(self):
        self.write("Game Over", align="center", font=("Arial", 25, "normal"))





