import pygame
from star import Star
from time import time
from player import Player
from collision import has_collision

import globals
globals.init()

from enemy import Enemy

# Gameplay configuration things
e_spawnrate = 0.4
e_spawn_timer = 0
e_score_kill = 20


def reset():
    global stars, enemies
    global player, score
    player = Player()
    stars = []
    enemies = []
    score = 0
    for i in range(80):
        stars.append(Star())

    for i in range(7):
        enemies.append(Enemy())


dt = 0
done = False
reset()
while not done:
    t_start = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not globals.game_over:
                    globals.pause = not globals.pause
                else:
                    reset()
                    globals.game_over = globals.pause = False

    globals.screen.fill((0, 0, 0))

    for i in stars:
        if not globals.pause:
            i.update(dt)
        i.draw()

    e_spawn_timer += dt
    if e_spawn_timer >= e_spawnrate:
        enemies.append(Enemy())
        e_spawn_timer = 0

    player_damaged = False
    for i in enemies:
        if not globals.pause:
            i.update(dt)
            if has_collision(player, i):
                # player.take_damage()
                player_damaged = True
                break

        i.draw()

    if player_damaged:
        globals.pause = globals.game_over = True
        for i in enemies:
            i.__init__()
        globals.projectiles = []

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
                    score += e_score_kill
                    break
        j.draw()

    for i in range(len(proj_removal)):
        del globals.projectiles[proj_removal[i]]

    if globals.game_over:
        globals.screen.blit(globals.main_font.render("Game Over!", False, (0xFF, 0xFF, 0xFF)), (100, 450))
    elif globals.pause:
        globals.screen.blit(globals.main_font.render("Paused", False, (0xFF, 0xFF, 0xFF)), (100, 450))
    else:
        player.update(dt)

    player.draw()

    globals.screen.blit(globals.main_font.render("Score: %5s" %(score), False, (0xFF, 0xFF, 0xFF)), (0, 0))
    pygame.display.flip()
    dt = time() - t_start
