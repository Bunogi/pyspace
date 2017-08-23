import pygame


def init():
    pygame.init()
    global resolution, screen, pause, game_over, main_font, projectiles
    resolution = (500, 900)
    screen = pygame.display.set_mode(resolution)
    pause = False
    game_over = False
    pygame.font.init()
    main_font = pygame.font.SysFont("Sans", 30)
    projectiles = []
