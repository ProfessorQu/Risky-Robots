import pygame
from pygame.locals import *

from src.constants.game import *
from src.menu.button import Button
from src.terrain import Terrain, Solid
from src.player.healthbar import HealthBar
import game

import time


pygame.init()
pygame.display.set_caption("Game")

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

running = True

buttons = []

rect = pygame.Rect(0, 0, WIDTH / 3, HEIGHT / 3)
for i in range(3):
    if i == 0:
        rect.center = (WIDTH / 4, HEIGHT / 4)
    elif i == 1:
        rect.center = (WIDTH / 4 * 3, HEIGHT / 4)
    elif i == 2:
        rect.center = (WIDTH / 4, HEIGHT / 4 * 3)
    elif i == 3:
        rect.center = (WIDTH / 4 * 3, HEIGHT / 4 * 3)
    
    buttons.append(Button(i, rect, (0, 0, 0), (100, 100, 100), (255, 0, 0), f"Map {i + 1}", (255, 255, 255)))
    
prev_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    CLOCK.tick(FPS)

    now = time.time()
    dt = now - prev_time
    prev_time = now

    SCREEN.fill((0, 128, 128))

    for button in buttons:
        button.draw(SCREEN)

        if button.pressed:
            if button.id == 0:
                game.game(game.MAP1_TERRAIN, game.MAP1_PLAYERS_POS)
            elif button.id == 1:
                game.game(game.MAP2_TERRAIN, game.MAP2_PLAYERS_POS)
            elif button.id == 2:
                game.game(game.MAP3_TERRAIN, game.MAP3_PLAYERS_POS)

    pygame.display.update()

pygame.quit()