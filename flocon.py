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
        self.state = ""

    def updateSnow(self):
        self.y += self.speed
        self.state = "falling"
        if self.state == "falling":
            self.x += random.uniform(0, 1.5)
            self.x -= random.uniform(0, 1.5)
        if self.y > globals.screen_height - 1:
            self.state = "outScreen"

    def draw(self):
        color = 0
        if color == 0:
            pygame.draw.circle(globals.screen, globals.WHITE, (self.x, self.y), self.size)
        if color == 1:
            pygame.draw.circle(globals.screen, globals.RED, (self.x, self.y), self.size)
        if color == 2:
            pygame.draw.circle(globals.screen, globals.GREEN, (self.x, self.y), self.size)
        if color == 3:
            pygame.draw.circle(globals.screen, globals.YELLOW, (self.x, self.y), self.size)
        if color == 4:
            pygame.draw.circle(globals.screen, globals.BLUE, (self.x, self.y), self.size)

