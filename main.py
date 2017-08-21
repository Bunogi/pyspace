import pygame
from star import Star
from time import time
from player import Player
from enemy import Enemy
from collision import has_collision

import globals

globals.init()

done = False

stars = []

for i in range(50):
    stars.append(Star())

enemies = []
for i in range(10):
    enemies.append(Enemy())


dt = 0
player = Player()
while not done:
    t_start = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                globals.pause = not globals.pause

    globals.screen.fill((0, 0, 0))

    for i in stars:
        i.update(dt)
        i.draw()

    player_damaged = False
    for i in enemies:
        if not globals.pause:
            i.update(dt)
            if has_collision(player, i):
                player.take_damage()
                player_damaged = True
                break

        i.draw()

    for i in globals.projectiles:
        if not globals.pause:
            i.update(dt)
        i.draw()

    if player_damaged:
        globals.pause = True
        for i in enemies:
            i.__init__()

    if globals.pause:
        globals.screen.blit(globals.main_font.render("Paused/ded", False,
                                                     (0xFF, 0xFF, 0xFF)), (100, 450))
    else:
        player.update(dt)

    player.draw()

    pygame.display.flip()
    dt = time() - t_start
