import sys
import pygame
import flocon
import globals

pygame.init()

pygame.display.set_caption("REINE DES NEIGES")

bg_color = globals.BLACK

listSnowFlake = []
listSnowFlake2 = []

flocon.create_List(listSnowFlake, 250)

flocon.create_List(listSnowFlake2, 250)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    globals.screen.fill(globals.BLACK)

    flocon.update(listSnowFlake, -100)
    flocon.update(listSnowFlake2, 0)

    print(listSnowFlake[0].state)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

    sys.stdout.flush()

pygame.quit()
sys.exit()
