import pygame
from pygame.locals import *

from src.constants.game import *

pygame.init()
pygame.display.set_caption("Game")

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False