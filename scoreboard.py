UPPER_EDGE =270
from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=UPPER_EDGE)
        self.pencolor("white")
        self.paddle1=0
        self.paddle2=0
        self.write(f"""{self.paddle1}                   Scores                   {self.paddle2} """,False,"center",("Arial",20,"bold"))


    def score_1(self):
        self.clear()
        self.paddle1 +=1
        self.write(f"""{self.paddle1}                   Scores                   {self.paddle2} """,False,"center",("Arial",20,"bold"))


    def score_2(self):
        self.clear()
        self.paddle2 += 1
        self.write(f"""{self.paddle1}                   Scores                   {self.paddle2} """, False, "center",
               ("Arial", 20, "bold"))
