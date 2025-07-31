from turtle import Turtle
my_list = [(0, 0), (-20, 0), (-40, 0)]
move_amount=20
class SnakeGame:

    def __init__(self):
        self.another_list = []
        self.create_snake()
        self.head=self.another_list[0]
        self.tail=self.another_list[-1]


    def create_snake(self):

        for i in my_list:
            self.increase_head(i)
    def move_snake(self):

        for i in range(len(self.another_list) - 1, 0, -1):
            new_x = self.another_list[i - 1].xcor()
            new_y = self.another_list[i - 1].ycor()
            self.another_list[i].goto(new_x, new_y)

        self.head.forward(move_amount)
    def increase_head(self,i):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.shapesize(1, 1)
        turtle.penup()
        turtle.goto(i)
        self.another_list.append(turtle)
    def extend(self):
        self.increase_head(self.tail.position())


    def up(self ):
        if self.head.heading() != 270:

            self.head.setheading(90)

    def down(self ):
        if self.head.heading() != 90:
            self.another_list[0].setheading(270)


    def right(self ):
        if self.head.heading() != 180:
            self.another_list[0].setheading(0)



    def left(self ):

        if self.head.heading() != 0:
            self.another_list[0].setheading(180)








