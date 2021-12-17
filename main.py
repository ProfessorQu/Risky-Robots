import pygame
from pygame.locals import *

from src.constants.game import *
from src.menu.button import Button
from src.terrain import Terrain, Solid
from src.player.healthbar import HealthBar
import src.game as game

import time


pygame.init()
pygame.display.set_caption("Game")

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

running = True

buttons = []
button_pos = [
    (200, 150),
    (600, 150),
    (200, 450),
    (600, 450),
]

rect = pygame.Rect(0, 0, WIDTH / 3, HEIGHT / 3)
for i in range(3):
    rect.center = button_pos[i]
    
    buttons.append(Button(i, rect, (200, 200, 200), (100, 100, 100), f"Map {i + 1}", (255, 255, 255)))
    
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
                game.game(MAP1_TERRAIN, MAP1_PLAYERS_POS)
            elif button.id == 1:
                game.game(MAP2_TERRAIN, MAP2_PLAYERS_POS)
            elif button.id == 2:
                game.game(MAP3_TERRAIN, MAP3_PLAYERS_POS)

    pygame.display.update()

pygame.quit()