import pygame
import random
import globals


def create_List(liste, nb):
    for i in range(nb):
        x = random.randint(0, globals.screen_width)
        y = -250
        speed = random.uniform(0.5, 3)
        size = random.uniform(0.5, 3)
        liste.append(Flocon(x, y, speed, size))


def update(liste, posy):
    for i in liste:
        i.y += i.speed
        i.x += random.uniform(0, 1)
        i.x -= random.uniform(0, 1)
        pygame.draw.circle(globals.screen, globals.WHITE, (i.x, i.y), i.size)
        i.state = "falling"
        if i.y > globals.screen_height:
            i.y = globals.screen_height
            i.state = "on_ground"
            #i.y = posy


class Flocon:
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.state = ""
