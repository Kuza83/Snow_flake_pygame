import pygame
import random
import globals


class Flocon(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, size, tLife):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.tLife = tLife
        self.timer = 0
        self.state = "falling"

    def updateSnow(self):
        if self.state == "falling":
            self.x += random.uniform(0, 1.5)
            self.x -= random.uniform(0, 1.5)
        if self.y > globals.screen_height - 1:
            self.state = "outScreen"
        if self.state != "outScreen":
            self.y += self.speed
        if self.state == "outScreen":
            print("sol")
            self.y = globals.screen_height - 1

    def draw(self):
        pygame.draw.circle(globals.screen, globals.WHITE, (self.x, self.y), self.size)
