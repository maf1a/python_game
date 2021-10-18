import pygame, sys
from random import seed
from random import random

import colors
from User import User
from Enemy import Enemy

pygame.init()
clock = pygame.time.Clock()
seed(1)

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Space invaders")

user = User(pygame, windowSurface)
enemies = []

def createEnemy():
    enemy = Enemy(pygame, windowSurface)
    enemies.append(enemy)

while True:
    clock.tick(60)
    windowSurface.fill(colors.WHITE)

    if random() > 0.985:
        createEnemy()

    for enemy in enemies:
        enemy.update()
        enemy.draw()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        user.goLeft()
    if pressed[pygame.K_RIGHT]:
        user.goRight()

    user.update(enemies)
    user.draw()
    pygame.display.update()      

    for event in pygame.event.get():  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                user.shoot()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()