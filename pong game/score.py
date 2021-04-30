from turtle import Turtle
FONT=("Arial", 36,"normal")
class Score(Turtle):
    def __init__(self,X=-30):
        super().__init__()
        self.score = 0
        self.X=X
        self.color("white")
        self.penup()
        self.goto(self.X,240)
        self.write(f"{self.score}",align="center",font=FONT)
        self.hideturtle()
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"{self.score}",align="center",font=FONT)

