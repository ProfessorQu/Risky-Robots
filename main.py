import pygame
from pygame.locals import *

import time

from src.player.player import Player
from src.terrain.terrain import Terrain, Solid
from src.player.inputs import Inputs
from src.constants import *

pygame.init()
pygame.display.set_caption("Game")


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

running = True

terrain = Terrain(
    Solid(WIDTH / 2, 0,         WIDTH, 20),  # Ceiling
    Solid(WIDTH / 2, HEIGHT,    WIDTH, 20),  # Ground

    Solid(0, HEIGHT / 2,        20, HEIGHT),    # Left wall
    Solid(WIDTH, HEIGHT / 2,    20, HEIGHT),    # Right wall

    Solid(WIDTH / 2, HEIGHT / 2, 20, 100),       # Center
)

bullets = []

inputs1 = Inputs(
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s,
)

inputs2 = Inputs(
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN,
)


player1 = Player(
    1,
    (40, FLOOR - 40),
    inputs1,
    terrain,
)

player2 = Player(
    2,
    (200, FLOOR - 40),
    inputs2,
    terrain,
)

prev_time = time.time()

while running:
    CLOCK.tick(FPS)

    now = time.time()
    dt = now - prev_time
    prev_time = now

    SCREEN.fill((0, 255, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_bullet1 = player1.update(dt)
    new_bullet2 = player2.update(dt)

    player1.draw(SCREEN)
    player2.draw(SCREEN)

    if new_bullet1:
        bullets.append(new_bullet1)
    if new_bullet2:
        bullets.append(new_bullet2)

    for block in terrain:
        block.draw(SCREEN)

    for bullet in bullets:
        remove = bullet.update(dt, SCREEN)

        if remove:
            bullets.remove(bullet)
        elif bullet.player_id == 1 and player2.rect.colliderect(bullet.rect):
            bullets.remove(bullet)
        elif bullet.player_id == 2 and player1.rect.colliderect(bullet.rect):
            bullets.remove(bullet)

    pygame.display.flip()

pygame.quit()
