import flocon
import pygame
import random

BLACK = (0, 0, 0)

RED = (255, 0, 0)

WHITE = (255, 255, 255)

screen_width, screen_height = 800, 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 14)


def drawtext(t, x, y):
    text = font.render(t, True, RED)
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)


def create_List(liste, nb):
    for i in range(nb):
        x = random.randint(0, screen_width)
        y = -250
        speed = random.uniform(0.5, 3)
        size = random.uniform(0.5, 3)
        liste.append(flocon.Flocon(x, y, speed, size))

