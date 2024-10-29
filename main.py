import time
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
screen=Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=1200,height=600)
screen.tracer(0)


paddle1 = Paddle()
paddle1.move(-570,0)
paddle2 = Paddle()
paddle2.move(560,0)

screen.listen()
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")

ball = Ball()

def condition_pdl1():
    if paddle1.ycor()-60<=ball.ycor()<=paddle1.ycor()+60:
        return True
def condition_pdl2():
    if paddle2.ycor() - 60 <= ball.ycor() <= paddle2.ycor() + 60:
        return True

score = ScoreBoard()



game_is_on  = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()
    if ball.ycor() >280  or ball.ycor()< -280 :
        ball.bounce_back()

    if (ball.xcor() == 540 and condition_pdl2() )  or ( ball.xcor()==-550 and condition_pdl1() ):
        ball.hit_back()

    elif ball.xcor()>580:
        ball.start_again()
        score.score_1()

    elif(ball.xcor()<-600):
        ball.start_again()
        score.score_2()






















screen.exitonclick()