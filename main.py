import pygame
from pygame.locals import *

import time

from src.player import Player
from src.terrain import Terrain, Solid
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

player = Player(
    x=40, y=FLOOR - 40, terrain=terrain,
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

    player.update(dt)
    player.draw(SCREEN)

    for block in terrain:
        block.draw(SCREEN)

    pygame.display.flip()


pygame.quit()
