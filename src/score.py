from turtle import Turtle


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__("square", 1000, False)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x=0, y=280)

        self.points = 0

        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.points}", align="center",
                   font=('Courier', 14, 'normal'))

    def update_score(self):
        self.points += 1
        self.clear()
        self.write_score()
