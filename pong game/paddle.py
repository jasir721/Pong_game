from turtle import Turtle

class Paddle:
    def __init__(self,X=0) :
        self.segments=[]
        self.X=X
        self.start_pos=[(self.X,-40),(self.X,-20),(self.X,0),(self.X,20)]
        self.create_paddle()
        self.head=self.segments[0]
        self.tail=self.segments[3]
        self.head.setheading(270)
        self.tail.setheading(90)

    def create_paddle(self):
        for pos in self.start_pos:
            self.add_segment(pos)
    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def down(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)
    def up(self):
        for seg_num in range(0,len(self.segments)-1,1):
            new_x=self.segments[seg_num+1].xcor()
            new_y=self.segments[seg_num+1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.tail.forward(20)