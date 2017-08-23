import random
import pygame
import globals

from math import floor
from player import Player
import time


class Enemy:
    def get_random_x(self):
        return random.uniform(self.border_offset,
                              globals.resolution[0] - self.border_offset)

    def __init__(self):
        self.size = 30
        self.border_offset = floor((self.size / 2))
        self.speed = random.uniform(200, 600)
        self.xPos = self.get_random_x()
        self.yPos = -self.size

    def get_collision_info(self):
        return (self.xPos, self.yPos, self.size, self.size)

    def draw(self):
        pygame.draw.rect(globals.screen, (0xFF, 0, 0),
                         pygame.Rect(self.xPos, self.yPos,
                                     self.size, self.size))

    def update(self, dt):
        self.yPos += self.speed * dt
        if self.yPos > globals.resolution[1] + self.size:
            self.__init__()
