import globals
import pygame

p_size = 30
p_speed = 90
key_left = pygame.K_LEFT
key_right = pygame.K_RIGHT
key_up = pygame.K_UP
key_down = pygame.K_DOWN


class Player:
    def __init__(self):
        self.xPos = (globals.resolution[0] / 2) - (p_size / 2)
        self.yPos = (globals.resolution[1] / 2) + (globals.resolution[1] / 3)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[key_left]:
            self.xPos -= p_speed * dt
        if keys[key_right]:
            self.xPos += p_speed * dt
        if keys[key_up]:
            self.yPos -= p_speed * dt
        if keys[key_down]:
            self.yPos += p_speed * dt

    def draw(self):
        pygame.draw.rect(globals.screen, (0, 0xFF, 0),
                         pygame.Rect(self.xPos, self.yPos, p_size, p_size))
