from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(size=5)
screen.update()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Left", fun=snake.turn_left)

while True:
    snake.move_forward()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
