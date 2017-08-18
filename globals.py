import pygame


def init():
    pygame.init()
    global resolution
    resolution = (500, 900)
    global screen
    screen = pygame.display.set_mode(resolution)
