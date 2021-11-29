import pygame
from pygame.locals import *

from src.player import Player
from src.terrain import Solid
from src.constants import *

pygame.init()
pygame.display.set_caption("Game")


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

running = True

player = Player(200, 200, 0.05, 3, 5, 1)

terrain = [
    Solid(0, HEIGHT - 10,   WIDTH, 10),  # Ground
    Solid(WIDTH - 10, 0,    10, HEIGHT),  # Right Wall
    Solid(0, 0,             10, HEIGHT),  # Left Wall
    Solid(0, 0,             WIDTH, 10),  # Ceiling
]

while running:
    CLOCK.tick(FPS)
    SCREEN.fill((0, 255, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(terrain)
    player.draw(SCREEN)

    for block in terrain:
        block.draw(SCREEN)

    pygame.display.flip()


pygame.quit()
