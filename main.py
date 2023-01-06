import sys
import pygame
import flocon
import globals


pygame.init()

pygame.display.set_caption("REINE DES NEIGES")

bg_color = globals.BLACK

listSnowFlake = []

listSnowOnGround = []

listExplo = []

timer = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                globals.create_List(listSnowFlake, 5)

    globals.screen.fill(globals.BLACK)

    for i in listSnowFlake:
        i.timer += 1
        i.updateSnow()
        # if i.state == "on_ground":
        #     listSnowFlake.remove(i)
        #     listSnowOnGround.append(i)
        if i.tLife > i.timer:
            i.draw(globals.WHITE)
        elif i.tLife > i.timer:
            listSnowFlake.remove(i)

    globals.drawtext("nb item dans liste SnowFlake : " + str(len(listSnowFlake)), 10, 10)
    globals.drawtext("nb item dans liste au sol : " + str(len(listSnowOnGround)), 10, 30)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

    sys.stdout.flush()

pygame.quit()
sys.exit()
