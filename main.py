import random
import sys
import pygame
import globals
import plateforme

pygame.init()

pygame.display.set_caption("REINE DES NEIGES")

bg_color = globals.BLACK

listSnowFlake = []

groupSprite = pygame.sprite.Group()

timer = 0
timerSnow = 0

timerCreateSnow = random.randint(75, 150)
creationRand = random.randint(100, 200)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if len(listSnowFlake) < globals.limitList:
                    globals.create_List(listSnowFlake, creationRand)

    globals.screen.fill(globals.BLACK)

    timer += 1
    timerSnow += 1

    if timer > timerCreateSnow :
        if len(listSnowFlake) < globals.limitList:
          globals.create_List(listSnowFlake, creationRand)
        timer = 0

    globals.updateSnowFall(listSnowFlake)
    globals.eraseSnow(listSnowFlake)

    globals.drawtext("nb item dans liste SnowFlake : " + str(len(listSnowFlake)), 10, 10)
    globals.drawtext("timer : " + str(timer), 10, 30)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
