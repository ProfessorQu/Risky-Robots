import pygame
from pygame.locals import *

import time

from src.player.player import Player
from src.terrain.terrain import Terrain, Solid
from src.player.inputs import Inputs
from src.bullets import Bullets
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

    Solid(WIDTH / 2, HEIGHT,   20, 20),     # Door
)

bullets = Bullets()

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

player1.weapon.bullets = bullets
player2.weapon.bullets = bullets

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

    player1.update(dt, SCREEN)
    player2.update(dt, SCREEN)

    for block in terrain:
        block.draw(SCREEN)

    pygame.display.flip()


pygame.quit()
