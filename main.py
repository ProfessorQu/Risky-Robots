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
    scale=0.05, speed=250,
    jump_height=400, max_jumps=2
)

terrain = Terrain(
    Solid(0, FLOOR,   WIDTH, 10),  # Ground
    Solid(WIDTH - 10, 0,    10, HEIGHT),  # Right Wall
    Solid(0, 0,             10, HEIGHT),  # Left Wall
    Solid(0, 0,             WIDTH, 10),  # Ceiling
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

    pygame.display.flip()


pygame.quit()
