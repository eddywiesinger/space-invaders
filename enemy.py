import random
from turtle import Turtle

from bullet import EnemyBullet


class Enemy(Turtle):
    speed = 1
    move_direction = 1
    max_rand = 10

    def __init__(self, xpos, ypos, enemy_bullets):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.setheading(270)
        self.setposition(xpos, ypos)
        self.enemy_bullets = enemy_bullets
        self.shoot_cooldown = random.randint(2, self.max_rand)

    def move(self):
        self.goto(self.xcor() + self.move_direction * self.speed, self.ycor())

    def change_direction(self):
        self.move_direction = - self.move_direction

    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.enemy_bullets.append(EnemyBullet(self.xcor(), self.ycor()))
            self.shoot_cooldown = random.randint(1, self.max_rand)

    def cooldown(self, dt):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
