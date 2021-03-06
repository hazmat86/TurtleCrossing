from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.up()
        self.setheading(90)
        self.goto(0, -275.00)

    def hop(self):
        self.forward(20)

    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
