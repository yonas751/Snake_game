
from turtle import Turtle,Screen
from SCORE import Score
from food import Food
from snake import SnakeGame
import time
snake = SnakeGame()


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)




game_on=True
snake.create_snake()
screen.listen()
screen.onkey(snake.up,"Up" )
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food=Food()
score=Score()
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:

        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
            score.reset()
            snake.reset_snake()
    for i in snake.another_list[1:]:

        if snake.head.distance(i) < 10:
            snake.reset_snake()
            score.reset()

screen.exitonclick()









