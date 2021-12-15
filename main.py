import pygame
from pygame.locals import *

import time

from src.player.player import Player
from src.player.healthbar import HealthBar
from src.terrain import Terrain, Solid
from src.player.inputs import Inputs
from src.constants.game import *

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

    Solid(WIDTH / 2, HEIGHT / 1.5, 200, 50),
    Solid(0, HEIGHT / 2, 300, 50),
    Solid(WIDTH, HEIGHT / 2, 300, 50),
)

players = []
bullets = []

players.append(
    Player(
        1,
        (50, FLOOR - 40),
        True,
        Inputs(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
        terrain
    )
)
players.append(
    Player(
        2,
        (WIDTH - 50, FLOOR - 40),
        False,
        Inputs(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN),
        terrain
    )
)

prev_time = time.time()

while running:
    CLOCK.tick(FPS)

    # Calculate delta time
    now = time.time()
    dt = now - prev_time
    prev_time = now

    # Set background color
    SCREEN.fill((0, 128, 128))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw terrain
    terrain.draw(SCREEN)

    # Update players
    for player in players:
        new_bullet = player.update(dt)

        if new_bullet:
            bullets.append(new_bullet)

        player.draw(SCREEN)

    # Update bullets
    for bullet in bullets:
        remove = bullet.update(dt, players)

        if remove:
            bullets.remove(bullet)

        bullet.draw(SCREEN)

    pygame.display.flip()

pygame.quit()
