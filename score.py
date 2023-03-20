from turtle import Turtle


class Scoreboard(Turtle):

    score = 0

    def __init__(self, xpos, ypos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(xpos, ypos)
        self.write(f"Score: {self.score}", font=("Verdana", 15, "bold"))

    def increase_score(self, inc_amt):
        self.score += inc_amt
        self.clear()
        self.write(f"Score: {self.score}", font=("Verdana", 15, "bold"))


class Lives(Turtle):

    lives = "❤❤❤"

    def __init__(self, xpos, ypos):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(xpos, ypos)
        self.write(self.lives, font=("Verdana", 15, "bold"))

    def lose(self):
        if len(self.lives) > 0:
            self.lives = self.lives[:-1]
        self.clear()
        self.write(self.lives, font=("Verdana", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Verdana", 15, "bold"))

    def win(self):
        self.goto(0, 0)
        self.write("You Win!", align="center", font=("Verdana", 15, "bold"))
