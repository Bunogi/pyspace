import pygame


def init():
    pygame.init()
    global resolution
    resolution = (500, 900)
    global screen
    screen = pygame.display.set_mode(resolution)
    global pause
    pause = False
    pygame.font.init()
    global main_font
    main_font = pygame.font.SysFont("Sans", 30)
