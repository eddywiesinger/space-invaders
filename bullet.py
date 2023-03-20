from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.3, stretch_wid=0.3)
        self.color("orange")
        self.setposition(xpos, ypos)
        self.setheading(90)

    def move(self):
        self.forward(10)


class EnemyBullet(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=0.3, stretch_wid=0.1)
        self.color("red")
        self.setposition(xpos, ypos)
        self.setheading(270)

    def move(self):
        self.forward(10)
