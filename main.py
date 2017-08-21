import pygame
from star import Star
from time import time
from player import Player
import globals

globals.init()

done = False

stars = []

for i in range(50):
    stars.append(Star())

dt = 0
player = Player()
while not done:
    t_start = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    globals.screen.fill((0, 0, 0))

    for i in stars:
        i.update(dt)
        i.draw()

    player.update(dt)
    player.draw()
    pygame.display.flip()
    dt = time() - t_start
