from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=1000,height=600)
screen.title("PONG GAME!!!")
screen.tracer(0)
tim=Turtle()
tim.color("white")
tim.penup()
tim.goto(0,300)
tim.right(90)
for i in range(10):
    tim.pendown()
    tim.forward(30)
    tim.penup()
    tim.forward(30)

paddle1=Paddle(-470)
paddle2=Paddle(460)
B=Ball()
score1=Score()
score2=Score(30)
#Event listener
screen.listen()
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    B.move()
    #Detect if player has missed the ball
    if B.ball.xcor()>490:
        if score1.score==5:
            game_is_on=False
        score1.increase_score()
        B.reset_ball()
    if B.ball.xcor()<-490:
        if score2.score==5:
            game_is_on=False
        score2.increase_score()
        B.reset_ball()
    if B.ball.ycor()>270 or B.ball.ycor()<-270:
        if B.ball.heading()==45 or B.ball.heading()==225:
            B.ball.right(90)
        else:
            B.ball.left(90)
    #Detect if it hit the paddle
    for segment in paddle1.segments:
        if B.ball.distance(segment)<20:
            if B.ball.heading()==135:
                B.ball.right(90)
            else:
                B.ball.left(90)
    for segment in paddle2.segments:
        if B.ball.distance(segment)<20:
            if B.ball.heading()==315:
                B.ball.right(90)
            else:
                B.ball.left(90)
            break
screen.exitonclick()