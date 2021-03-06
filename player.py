import globals
import pygame

from projectile import Projectile

p_size = 30
p_speed = 200
p_speed_boost = 1.5 * p_speed
p_firing_interval = 0.2
key_left = pygame.K_LEFT
key_right = pygame.K_RIGHT
key_up = pygame.K_UP
key_down = pygame.K_DOWN
key_boost = pygame.K_LSHIFT
key_shoot = pygame.K_SPACE


class Player:
    def __init__(self):
        self.xPos = (globals.resolution[0] / 2) - (p_size / 2)
        self.yPos = (globals.resolution[1] / 2) + (globals.resolution[1] / 3)
        self.t_last_shot = 100

    def take_damage(self):
        self.__init__()  # TODO: Replace with proper system

    def get_collision_info(self):
        return (self.xPos, self.yPos, p_size, p_size)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        speed = p_speed
        self.t_last_shot += dt

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
        if keys[key_shoot] and self.t_last_shot > p_firing_interval:
            self.shoot()
            self.t_last_shot = 0

        # Disallow player to go off screen
        clamp = lambda n, minn, maxn: max(min(maxn, n), minn)
        self.xPos = clamp(self.xPos, 0, globals.resolution[0] - p_size)
        self.yPos = clamp(self.yPos, 0, globals.resolution[1] - p_size)

    def shoot(self):
        globals.projectiles.append(Projectile(self.xPos + (p_size / 2),
                                              self.yPos - 5, -350))

    def draw(self):
        pygame.draw.rect(globals.screen, (0, 0xFF, 0),
                         pygame.Rect(self.xPos, self.yPos, p_size, p_size))
