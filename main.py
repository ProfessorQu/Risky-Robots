import pygame
from src.player import Player
from src.object import Object
pygame.init()

running = True

screen = pygame.display.set_mode((800, 600))

p = Player(pygame.Rect(100, 100, 50, 50), (255, 0, 0))
o = Object(pygame.Rect(200, 200, 50, 50), (0, 255, 0))

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
