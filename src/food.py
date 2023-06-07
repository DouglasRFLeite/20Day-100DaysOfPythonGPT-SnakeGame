from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.penup()
        self.color("red")
        self.setpos(x=random.randint(-280, 280), y=random.randint(-280, 280))

    def respawn(self):
        self.setpos(x=random.randint(-280, 280), y=random.randint(-280, 280))
