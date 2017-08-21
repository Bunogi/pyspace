import pygame
import globals

pr_w = 5
pr_h = 15


class Projectile:
    def __init__(self, x, y, vel):
        self.xPos = x
        self.yPos = y
        self.vel = vel

    def get_collision_info(self):
        return (self.xPos, self.yPos, pr_w, pr_h)

    def update(self, dt):
        self.yPos += self.vel * dt
        return self.yPos < - pr_h or self.yPos > globals.resolution[1] + pr_h

    def draw(self):
        pygame.draw.rect(globals.screen, (0xFF, 0, 0xFF),
                         pygame.Rect(self.xPos, self.yPos, pr_w, pr_h))
