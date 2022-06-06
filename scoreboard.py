from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, x_val):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.ht()
        self.up()
        self.goto(x_val, 225)
        self.score = 0

    def show_score(self):
        self.write(self.score, move=False, align='center', font=("Arial", 24,))


    
