import random
import pygame
from pygame.math import Vector2
import globals

from math import floor
from player import Player
import time


e_x_min = 30
e_x_max = globals.resolution[0] - e_x_min
e_y_min = 30
e_y_max = globals.resolution[1] - e_y_min
e_max_distance = 250
e_max_speed = 600
e_speed_factor = 3

def gen_coords():
    return Vector2(random.uniform(e_x_min, e_x_max),
                   random.uniform(e_y_min, e_y_max))

class Enemy:

    def get_random_x(self):
        return random.uniform(self.border_offset,
                              globals.resolution[0] - self.border_offset)

    def __init__(self):
        self.size = 30
        self.border_offset = floor((self.size / 2))
        self.xPos = self.get_random_x()
        self.yPos = -self.size
        self.target_coords = gen_coords()
        self.move_vector = self.target_coords - Vector2(self.xPos, self.yPos)
        if self.move_vector.length() > e_max_distance:
            self.move_vector.scale_to_length(e_max_distance)

    def get_collision_info(self):
        return (self.xPos, self.yPos, self.size, self.size)

    def draw(self):
        pygame.draw.rect(globals.screen, (0xFF, 0, 0),
                         pygame.Rect(self.xPos, self.yPos,
                                     self.size, self.size))

    def update(self, dt):
        movement = self.move_vector * (e_speed_factor * dt)
        if movement.length() > e_max_speed:
            movement.scale_to_length(e_max_speed)
        self.xPos += movement.x
        self.yPos += movement.y
        if self.yPos > globals.resolution[1] + self.size:
            self.__init__()
