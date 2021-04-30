from turtle import Turtle
import random
MOVE_DIST=10
class Ball:
    def __init__(self,Y=random.randint(-200,200)):
        self.Y=Y
        self.create_ball()
        self.ball

    def create_ball(self):
        ball=Turtle("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0,self.Y)
        ball.setheading(45)
        self.ball=ball
    def move(self):
        self.ball.forward(MOVE_DIST)
    def reset_ball(self):
        self.ball.goto(0,random.randint(-200,200))

