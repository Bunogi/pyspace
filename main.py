import pygame
from star import Star
from time import time
import globals

globals.init()

done = False

stars = []

for i in range(50):
    stars.append(Star())

dt = 0
while not done:
    t_start = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    globals.screen.fill((0, 0, 0))

    for i in stars:
        i.update(dt)
        i.draw()

    pygame.display.flip()
    dt = time() - t_start
