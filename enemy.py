import random
import pygame
import globals

from math import floor


def get_speed(size):
    return (size + 1) * 10


class Enemy:
    def get_random_x(self):
        return random.randint(self.border_offset,
                              globals.resolution[0] - self.border_offset)

    def __init__(self):
        self.size = 30
        self.border_offset = floor((self.size / 2))
        self.speed = get_speed(self.size)
        self.xPos = self.get_random_x()
        self.yPos = random.uniform(0, globals.resolution[1])

    def re_init(self):
        self.__init__()
        self.yPos = -self.size

    def draw(self):
        pygame.draw.rect(globals.screen, (0xFF, 0, 0),
                         pygame.Rect(self.xPos, self.yPos,
                                     self.size, self.size))

    def update(self, dt):
        self.yPos += self.speed * dt
        if self.yPos > globals.resolution[1] + self.size:
            self.re_init()