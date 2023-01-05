import pygame
import random
import globals


class Flocon(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, size):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.centerx = (self.x, self.y)
        self.speed = speed
        self.size = size
        self.rect = self.size
        self.state = ""

    def updateSnow(self):
        self.y += self.speed
        self.x += random.uniform(0, 1)
        self.x -= random.uniform(0, 1)
        self.state = "falling"
        if self.y > globals.screen_height - 1:
            self.y = globals.screen_height - 1
            self.state = "on_ground"

    def draw(self):
        pygame.draw.circle(globals.screen, globals.WHITE, (self.x, self.y), self.size)
