import pygame
from pygame.locals import *

from src.player import Player, Platform

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
running = True

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

player = Player(
    pygame.Rect(100, 100, 50, 50),
    (255, 0, 0)
)

platform = Platform(
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
    (0, 255, 0)
)

while running:
    SCREEN.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    player.draw(SCREEN)
    platform.update()
    platform.draw(SCREEN)
    pygame.display.flip()

    CLOCK.tick(FPS)
