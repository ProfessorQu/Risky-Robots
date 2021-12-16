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
    Solid((0, HEIGHT / 3, WIDTH / 3, HEIGHT / 15), PLATFORM_COLOR), # Left platform
    Solid((WIDTH / 3, HEIGHT / 1.5, WIDTH / 3, HEIGHT / 15), PLATFORM_COLOR), # Middle platform
    Solid((WIDTH / 3 * 2, HEIGHT / 3, WIDTH / 3, HEIGHT / 15), PLATFORM_COLOR), # Right platform

    Solid((0, 0, WIDTH, 20), WALL_COLOR), # Ceiling
    Solid((0, FLOOR, WIDTH, 20), WALL_COLOR), # Floor

    Solid((0, 0, 20, FLOOR), WALL_COLOR), # Left wall
    Solid((WIDTH - 20, 0, 20, FLOOR), WALL_COLOR), # Right wall
)

players = []
bullets = []

players.append(
    Player(
        1,
        (100, FLOOR - 40),
        True,
        Inputs(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
        terrain
    )
)
players.append(
    Player(
        2,
        (WIDTH - 100, FLOOR - 40),
        False,
        Inputs(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN),
        terrain
    )
)

prev_time = time.time()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tick
    CLOCK.tick(FPS)

    # Calculate delta time
    now = time.time()
    dt = now - prev_time
    prev_time = now

    # Set background color
    SCREEN.fill((0, 128, 128))

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
    
    pygame.display.update()

pygame.quit()
