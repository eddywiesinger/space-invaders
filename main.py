import random
import time
from turtle import Screen, Turtle
from constants import *
from enemy import *
from score import Scoreboard, Lives
from ship import *


# helper
def remove_object_from_game(turtle):
    if type(turtle) == Bullet:
        bullets.remove(turtle)
    elif type(turtle) == Enemy:
        enemies.remove(turtle)
    elif type(turtle) == EnemyBullet:
        enemy_bullets.remove(turtle)
    turtle.reset()
    turtle.clear()


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

bullets = []
ship = Ship(bullets)

screen.listen()
screen.onkeypress(ship.activate_left, "Left")
screen.onkeyrelease(ship.deactivate_left, "Left")
screen.onkeypress(ship.activate_right, "Right")
screen.onkeyrelease(ship.deactivate_right, "Right")
screen.onkey(ship.shoot, "space")

# spawn enemies
enemies = []
enemy_bullets = []


scoreboard = Scoreboard(- SCREEN_WIDTH/2 + 30, - SCREEN_HEIGHT/2 + 40)
lives = Lives(- SCREEN_WIDTH/2 + 30, - SCREEN_HEIGHT/2 + 20)

for i in range(NROWS):
    for j in range(NCOLS):
        xpos = ((i / (2 * NROWS)) - 0.25) * SCREEN_WIDTH
        ypos = SCREEN_HEIGHT / 2 - 20 - 30 * j
        enemy = Enemy(xpos, ypos, enemy_bullets)
        enemies.append(enemy)

game_is_on = True
while game_is_on:
    dt = .01
    screen.update()
    time.sleep(dt)

    if len(enemies) == 0:
        game_is_on = False
        lives.win()
        break

    # Ship movement
    ship.move()
    ship.cooldown(dt)

    # Enemies movement
    leftmost_enemy = enemies[0]
    rightmost_enemy = enemies[0]
    for enemy in enemies:
        enemy.move()
        enemy.cooldown(dt)
        enemy.max_rand = int(1 + 10 * (len(enemies) / (NROWS * NCOLS)))
        enemy.speed = (NROWS * NCOLS) / (len(enemies) + 1)
        if enemy.xcor() < leftmost_enemy.xcor():
            leftmost_enemy = enemy
        if enemy.xcor() > rightmost_enemy.xcor():
            rightmost_enemy = enemy

        enemy.shoot()

    if leftmost_enemy.xcor() <= - SCREEN_WIDTH / 2 + 20 or rightmost_enemy.xcor() >= SCREEN_WIDTH / 2 - 20:
        for enemy in enemies:
            enemy.change_direction()

    # Bullets movement
    for bullet in bullets:
        bullet.move()

        # wall collision
        if bullet.ycor() >= SCREEN_HEIGHT / 2:
            remove_object_from_game(bullet)

        # enemy collision
        for enemy in enemies:
            if bullet.distance(enemy) < 10:
                remove_object_from_game(bullet)
                remove_object_from_game(enemy)
                scoreboard.increase_score(10)

    # Enemy bullets movement
    for enemy_bullet in enemy_bullets:
        enemy_bullet.move()
        # wall collision
        if enemy_bullet.ycor() <= - SCREEN_HEIGHT / 2:
            remove_object_from_game(enemy_bullet)

        # player collision
        elif enemy_bullet.distance(ship) <= 10:
            remove_object_from_game(enemy_bullet)
            lives.lose()
            if len(lives.lives) <= 0:
                lives.game_over()
                game_is_on = False

        # bullet collision:
        else:
            for bullet in bullets:
                if enemy_bullet.distance(bullet) <= 5:
                    remove_object_from_game(enemy_bullet)
                    remove_object_from_game(bullet)


screen.exitonclick()

