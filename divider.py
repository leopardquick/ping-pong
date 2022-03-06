from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, -400)
        self.shape("turtle")
        self.left(90)
        self.color("white")
        self.hideturtle()

    def move_foward(self):
        for rang in range(-40, 40):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
