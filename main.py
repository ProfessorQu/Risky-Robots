import pygame
from pygame.locals import *

import time

from src.player.player import Player
from src.player.healthbar import HealthBar
from src.terrain.terrain import Terrain, Solid
from src.player.inputs import Inputs
from src.constants import *

pygame.init()
pygame.display.set_caption("Game")


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

running = True

terrain = Terrain(
    Solid(WIDTH / 2, 0, WIDTH, 20), # Ceiling
    Solid(WIDTH / 2, HEIGHT, WIDTH, 20), # Floor

    Solid(0, HEIGHT / 2, 20, HEIGHT), # Left wall
    Solid(WIDTH, HEIGHT / 2, 20, HEIGHT), # Right wall
)

players = []
bullets = []

inputs1 = Inputs(
    pygame.K_a,
    pygame.K_d,
    pygame.K_w,
    pygame.K_s,
)

inputs2 = Inputs(
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN,
)


player1 = Player(
    1,
    (50, FLOOR - 40),
    True,
    inputs1,
    terrain,
)

player2 = Player(
    2,
    (WIDTH - 50, FLOOR - 40),
    False,
    inputs2,
    terrain,
)

players.append(player1)
players.append(player2)


prev_time = time.time()

while running:
    CLOCK.tick(FPS)

    now = time.time()
    dt = now - prev_time
    prev_time = now

    SCREEN.fill((0, 128, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    terrain.draw(SCREEN)

    for player in players:
        new_bullet = player.update(dt)

        if new_bullet:
            bullets.append(new_bullet)

        player.draw(SCREEN)

    for bullet in bullets:
        remove = bullet.update(dt, players)

        if remove:
            bullets.remove(bullet)

        bullet.draw(SCREEN)

    pygame.display.flip()

pygame.quit()
