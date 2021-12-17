import pygame
from pygame.locals import *

import time
import sys

from src.player.player import Player
from src.player.inputs import Inputs
from src.constants.game import *
from src.maps import Map

def game(game_map: Map):
    pygame.init()
    pygame.display.set_caption("Game")

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    terrain = game_map.terrain
    players_pos = game_map.players_pos

    running = True

    players = []
    bullets = []

    players.append(Player(1, players_pos[0], True, Inputs(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s), terrain))
    players.append(Player(2, players_pos[1], False, Inputs(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN), terrain))

    prev_time = time.time()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

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
