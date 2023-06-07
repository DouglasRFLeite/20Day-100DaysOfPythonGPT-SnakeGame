from turtle import Turtle

UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


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

        self.head = self.snake[0]

    def move_forward(self):
        next_pos = self.snake[0].pos()
        self.snake[0].forward(self.speed)
        for square in self.snake[1:]:
            old_pos = square.pos()
            square.setpos(next_pos)
            next_pos = old_pos

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def grow(self):
        new_square = self.snake[-1].clone()
        new_square.seth(self.head.heading())
        new_square.backward(20)
        self.snake.append(new_square)
