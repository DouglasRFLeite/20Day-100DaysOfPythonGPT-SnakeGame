from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(size=5)
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Left", fun=snake.turn_left)

game_running = True
while game_running:
    snake.move_forward()
    screen.update()
    time.sleep(0.1)

    # Detect colision with food
    if snake.head.distance(food) < 20:
        food.respawn()
        score.update_score()
        snake.grow()

    # Detect colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_running = False

    # Detect colision with tail
    for square in snake.snake[2:]:
        if snake.head.distance(square) < 5:
            score.game_over()
            game_running = False

screen.exitonclick()
