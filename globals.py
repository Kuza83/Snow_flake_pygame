import flocon
import pygame
import random
import flocon

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen_width, screen_height = 1920, 1080

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 16)

timer = 0


def drawtext(t, x, y):
    text = font.render(t, True, RED)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)


def create_List(listSnow, nb):
    for i in range(nb):
        x = random.randint(0, screen_width)
        ypos = random.randint(100, 300)
        y = ypos * -1
        speed = random.uniform(0.5, 3)
        size = random.uniform(0.5, 3)
        tLife = random.randint(100, 500)
        listSnow.append(flocon.Flocon(x, y, speed, size, tLife))


def updateSnow(listSnow):
    for i in listSnow:
        i.timer += 1
        i.updateSnow()
        i.draw()


def eraseSnow(listSnow):
    for i in reversed(listSnow):
        if i.timer > i.tLife:
            i.size -= 0.2
        if i.size == 0 or i.state == "outScreen":
            listSnow.remove(i)
