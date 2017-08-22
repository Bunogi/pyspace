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

    proj_removal = []
    for i, j in enumerate(globals.projectiles):
        if not globals.pause:
            if j.update(dt):
                proj_removal.append(i)
                continue

        # TODO: Use collision-detection algorithm to avoid checking every single entity
            for k, l in enumerate(enemies):
                if has_collision(j, l):
                    proj_removal.append(i)
                    enemies.remove(l)
                    break
        j.draw()

    for i in range(len(proj_removal)):
        del globals.projectiles[proj_removal[i]]

    if player_damaged:
        globals.pause = True
        for i in enemies:
            i.__init__()
        globals.projectiles = []

    if globals.pause:
        globals.screen.blit(globals.main_font.render("Paused/ded", False, (0xFF, 0xFF, 0xFF)), (100, 450))
    else:
        player.update(dt)

    player.draw()

    pygame.display.flip()
    dt = time() - t_start
