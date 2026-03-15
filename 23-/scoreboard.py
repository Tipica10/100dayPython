from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 1
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.l_score}", align="center", font=FONT)


    def level_increase(self):
        self.l_score += 1
        self.update_Scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=FONT)
