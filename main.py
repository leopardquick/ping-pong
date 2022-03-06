from turtle import Screen
from paddle import Paddle
import time
from divider import Divider
from ball import Ball

screen = Screen()
screen.setup(width=1400, height=700)
screen.bgcolor("black")
screen.tracer(0)

divider = Divider()
divider.move_foward()
paddle = Paddle(650)
paddle_2 = Paddle(-650)
ball = Ball()
screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")
screen.onkey(paddle_2.move_up, "q")
screen.onkey(paddle_2.move_down, "a")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.start()

    # collision with right paddle
    if ball.distance(paddle) < 50:
        ball.right_paddle_contact()

    # collision with left paddle
    if ball.distance(paddle_2) < 50:
        ball.left_paddle_contact()

    #collision with wall
    if ball.ycor() > 330:
        ball.top_bound()
        print("bound")
    if ball.ycor() < -330:
        ball.buttom_bound()

    if ball.xcor() > 650:
        ball.restart_position()

    if ball.xcor() < -650:
        ball.restart_position()
        

screen.exitonclick()
