import random
import sys
import pygame
import globals


pygame.init()

pygame.display.set_caption("REINE DES NEIGES")

bg_color = globals.BLACK

listSnowFlake = []

groupSprite = pygame.sprite.Group()

timer = 0
timerSnow = 0

timerCreateSnow = random.randint(75, 150)
creationRand = random.randint(100, 350)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                globals.create_List(listSnowFlake, creationRand)

    globals.screen.fill(globals.BLACK)

    # globals.drawtext("nb item dans liste SnowFlake : " + str(len(listSnowFlake)), 10, 10)

    timer += 1
    timerSnow += 1

    if timer > timerCreateSnow:
        globals.create_List(listSnowFlake, creationRand)
        timer = 0

    globals.updateSnowFall(listSnowFlake)
    globals.eraseSnow(listSnowFlake)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
