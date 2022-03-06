from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.penup()
        self.left(90)
        self.goto(position, 0)

    def move_up(self):
        if self.ycor() < 350:
            self.forward(45)

    def move_down(self):
        if self.ycor() > -350:
            self.forward(-45)

