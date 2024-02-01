import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
velocity_player = 0

enemyImg = pygame.image.load('enemy.png')
enemyXY = [[100, 0], [100, 0], [100, 0], [100, 0], [100, 0], [100, 0]]
velocity_enemy = 0.5
counter_variable = [0, 0, 0, 0, 0, 0]

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
velocity_bullet = 0
bullet_State = False


def enemy():
    for x, y in enemyXY:
        screen.blit(enemyImg, (x, y))


def player():
    screen.blit(playerImg, (playerX, playerY))


def bullet_fire():
    screen.blit(bulletImg,(bulletX,bulletY))


def isCollision():
    for i in range(len(counter_variable)):
        distance = math.sqrt(math.pow(enemyXY[i][0] - bulletX, 2) + (math.pow(enemyXY[i][1] - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False
def game_over():
    screen.fill((255, 0, 0))
    pygame.display.update()
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_player = 0.5
            if event.key == pygame.K_LEFT:
                velocity_player = -0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                velocity_player = 0

            if event.key == pygame.K_SPACE and bullet_State == False:
                bullet_State = True
                bulletX = playerX
                bulletY = 480

    if playerX < 0:
        playerX = 0
        velocity_player = 0
    elif playerX > 736:
        playerX = 736
        velocity_player = 0
    playerX += velocity_player
    player()
    for i in range(len(counter_variable)):
        if int(counter_variable[i]) == 0:
            enemyXY[i][0] += velocity_enemy
            if enemyXY[i][0] >= 736:
                counter_variable[i] = 1
                enemyXY[i][1] += 20
        else:
            enemyXY[i][0] -= velocity_enemy
            if enemyXY[i][0] <= 0:
                counter_variable = 0
                enemyXY[i][1] += 20
    for i in range(len(counter_variable)):
        if enemyXY[i][1] >= 424:
            enemyXY[i][1] = 100
            enemyXY[i][0] = 0
            velocity_enemy = 0.5
            counter_variable[i] = 0
            enemy()
    if bullet_State:
        bullet_fire()
        bulletY -= 0.8
    if bulletY <= 0:
        bullet_State = False
    if isCollision():
        game_over()
        bullet_State = False
    enemy()
    pygame.display.update()