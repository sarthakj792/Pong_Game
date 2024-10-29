from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)

    def move(self,a,b):
        self.goto(a,b)

    def up(self):
        x=self.xcor()
        y=self.ycor()+40
        self.goto(x,y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 40
        self.goto(x, y)
