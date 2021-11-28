import pygame
from pygame.locals import *

from src.player import Player

pygame.init()
pygame.display.set_caption("Game")

WIDTH = 800
HEIGHT = 600
FPS = 60

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

running = True

player = Player(200, 200, 0.05, 3)

while running:
    CLOCK.tick(FPS)
    SCREEN.fill((0, 255, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    player.draw(SCREEN)

    pygame.display.flip()


pygame.quit()
