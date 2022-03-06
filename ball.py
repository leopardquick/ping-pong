from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.lef_angle = []
        self.right_angle = []
        self.init_left_angle()
        self.init_right_angle()

    def init_left_angle(self):
        for left in range(5, 80, 5):
            self.lef_angle.append(left)
        for left in range(350, 280, -5):
            self.lef_angle.append(left)

    def init_right_angle(self):
        for right in range(170, 80, -10):
            self.right_angle.append(right)
        for right in range(190, 260, 5):
            self.right_angle.append(right)

    def start(self):
        self.forward(40)

    def restart_position(self):
        self.goto(0, 0)
        self.setheading(to_angle=0)



    def right_paddle_contact(self):
        self.setheading(to_angle=random.choice(self.right_angle))
        print(self.heading())

    def left_paddle_contact(self):
        self.setheading(to_angle=random.choice(self.lef_angle))
        print(self.heading())

    def top_bound(self):
        self.setheading(-self.heading())

    def buttom_bound(self):
        self.setheading(-self.heading())
