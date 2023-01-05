import sys
import pygame
import flocon
import globals


pygame.init()

pygame.display.set_caption("REINE DES NEIGES")

bg_color = globals.BLACK

listSnowFlake = []

listSnowOnGround = []

groupSprite = pygame.sprite.Group()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                globals.create_List(listSnowFlake, 250)

    globals.screen.fill(globals.BLACK)

    for i in listSnowFlake:
        i.updateSnow()
        if i.state == "on_ground":
            listSnowFlake.remove(i)
            listSnowOnGround.append(i)
        i.draw()

    for i in listSnowOnGround:
        i.draw()

    # for i in listSnowFlake:
    #     for g in listSnowOnGround:
    #         if pygame.sprite.collide_circle(i.rect, g.rect):
    #             print("COLLISION !!! ")

    globals.drawtext("nb item dans liste SnowFlake : " + str(len(listSnowFlake)), 10, 10)
    globals.drawtext("nb item dans liste au sol : " + str(len(listSnowOnGround)), 10, 30)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

    sys.stdout.flush()

pygame.quit()
sys.exit()
