from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        a= self.xcor()+self.x_move
        b=self.ycor()+self.y_move
        self.goto(a,b)
    def bounce_back(self):
        self.y_move *= -1
    def hit_back(self):
        self.x_move *= -1

    def start_again(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.hit_back()
        self.bounce_back()



