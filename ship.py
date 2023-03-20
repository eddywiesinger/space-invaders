from turtle import Turtle

from bullet import Bullet

COOLDOWN_TIME = 0.3


class Ship(Turtle):

    move_left = False
    move_right = False
    shoot_cooldown = COOLDOWN_TIME

    def __init__(self, bullets):
        super().__init__()
        self.penup()
        self.color("white")
        self.setposition(0, -250)
        self.setheading(90)
        self.bullets = bullets

    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.bullets.append(Bullet(self.xcor(), self.ycor()))
            self.shoot_cooldown = COOLDOWN_TIME

    def cooldown(self, dt):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

    def move(self):
        if self.move_left:
            self.goto(self.xcor() - 5, self.ycor())
        if self.move_right:
            self.goto(self.xcor() + 5, self.ycor())

    def activate_left(self):
        self.move_left = True

    def activate_right(self):
        self.move_right = True

    def deactivate_left(self):
        self.move_left = False

    def deactivate_right(self):
        self.move_right = False
