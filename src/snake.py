from turtle import Turtle


class Snake:
    def __init__(self, size) -> None:
        self.size = size
        self.speed = 10
        self.snake = []

        self.square = Turtle(shape="square")
        self.square.color("white")
        self.square.penup()
        self.square.speed(0)
        self.snake.append(self.square)
        for _ in range(size-1):
            new_square = self.snake[-1].clone()
            new_square.backward(20)
            self.snake.append(new_square)

    def move_forward(self):
        next_pos = self.snake[0].pos()
        self.snake[0].forward(self.speed)
        for square in self.snake[1:]:
            old_pos = square.pos()
            square.setpos(next_pos)
            next_pos = old_pos

    def turn_up(self):
        self.snake[0].seth(90)

    def turn_down(self):
        self.snake[0].seth(270)

    def turn_right(self):
        self.snake[0].seth(0)

    def turn_left(self):
        self.snake[0].seth(180)
