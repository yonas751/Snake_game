from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
           self.highscore=int( f.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.penup()

        self.hideturtle()
        self.update_score()
    def increase_score(self):

        self.score +=1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score :{self.score} High score:{self.highscore} ", align="center", font=("Arial", 20, "normal"))
    def reset(self):
        if self.score>self.highscore:
              self.highscore=self.score
              with open("data.txt", "w") as f:
                  f.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.write("Game Over", align="center", font=("Arial", 25, "normal"))





