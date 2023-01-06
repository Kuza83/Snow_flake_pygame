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
        self.state = ""
        self.color = globals.WHITE

    def updateSnow(self):
        self.y += self.speed
        self.x += random.uniform(0, 1)
        self.x -= random.uniform(0, 1)
        self.state = "falling"
        if self.y > globals.screen_height - 1:
            self.y = globals.screen_height - 1
            self.state = "on_ground"

    def draw(self, color):
        pygame.draw.circle(globals.screen, color, (self.x, self.y), self.size)
        #pygame.draw.rect(globals.screen, globals.RED, self.rect)
