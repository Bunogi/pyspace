import random
import pygame
import globals

from math import floor
from player import Player, p_size
import time


class Enemy:
    def get_random_x(self):
        return random.randint(self.border_offset,
                              globals.resolution[0] - self.border_offset)

    def __init__(self):
        self.size = 30
        self.border_offset = floor((self.size / 2))
        self.speed = random.uniform(200, 600)
        self.xPos = self.get_random_x()
        self.yPos = -self.size

    def check_collision(self, player):
        p_hit_x = player.xPos + 2
        p_hit_s = p_size - 2
        p_hit_y = player.yPos + 2
        e_hit_x = self.xPos + 2
        e_hit_y = self.yPos + 2
        e_hit_s = self.size - 2
        if p_hit_x < e_hit_x + e_hit_s and p_hit_x + p_hit_s > e_hit_x and p_hit_y < e_hit_y + e_hit_s and p_hit_s + p_hit_y > e_hit_y:
            print("Crash!")
            return True
        else:
            return False

    def draw(self):
        pygame.draw.rect(globals.screen, (0xFF, 0, 0),
                         pygame.Rect(self.xPos, self.yPos,
                                     self.size, self.size))

    def update(self, dt):
        self.yPos += self.speed * dt
        if self.yPos > globals.resolution[1] + self.size:
            self.__init__()
