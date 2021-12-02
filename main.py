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

player = Player(
    x=200, y=FLOOR - 100,
)

terrain = Terrain(
    Solid(0, FLOOR - 10,         WIDTH, 200),  # Ground
    Solid(WIDTH - 10, 0,    200, HEIGHT),  # Right Wall
    Solid(-190, 0,             200, HEIGHT),  # Left Wall
    Solid(0, -190,             WIDTH, 200),  # Ceiling
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

    player.update(dt, terrain)
    player.draw(SCREEN)

    for block in terrain:
        block.draw(SCREEN)

    for bullet in player.bullets:
        bullet.draw(SCREEN)

    pygame.display.flip()


pygame.quit()
