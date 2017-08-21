import globals
import pygame

p_size = 30
p_speed = 90
p_speed_boost = 2 * p_speed
key_left = pygame.K_LEFT
key_right = pygame.K_RIGHT
key_up = pygame.K_UP
key_down = pygame.K_DOWN
key_boost = pygame.K_LSHIFT


class Player:
    def __init__(self):
        self.xPos = (globals.resolution[0] / 2) - (p_size / 2)
        self.yPos = (globals.resolution[1] / 2) + (globals.resolution[1] / 3)

    def take_damage(self):
        self.__init__()  # TODO: Replace with proper system

    def get_collision_info(self):
        return (self.xPos, self.yPos, p_size, p_size)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        speed = p_speed
        if keys[key_boost]:
            speed = p_speed_boost
        if keys[key_left]:
            self.xPos -= speed * dt
        if keys[key_right]:
            self.xPos += speed * dt
        if keys[key_up]:
            self.yPos -= speed * dt
        if keys[key_down]:
            self.yPos += speed * dt

    def draw(self):
        pygame.draw.rect(globals.screen, (0, 0xFF, 0),
                         pygame.Rect(self.xPos, self.yPos, p_size, p_size))
