import pygame
from pygame import sprite
from pygame.locals import *

from src.player.player import Player
from src.player.inputs import Inputs
from src.constants.game import *
from src.weapons.data.weapon_pickups import WeaponPickUps
from src.weapons.data.weapon_pickup import WeaponPickUp
from src.weapons import assaultrifle, revolver, goldenrevolver, sniperrifle, shotgun, rocketlauncher
from src.terrain import Terrain
from src.maps import Map

import time
import sys



def add_pickups(weapon_pickups: WeaponPickUps, terrain: Terrain):
    weapon_pickups.add(
        WeaponPickUp(
            sniperrifle.WEAPON,
            (100, 100),
            terrain
        )
    )

    weapon_pickups.add(
        WeaponPickUp(
            revolver.WEAPON,
            (200, 100),
            terrain
        )
    )
    weapon_pickups.add(
        WeaponPickUp(
            goldenrevolver.WEAPON,
            (300, 100),
            terrain
        )
    )

    weapon_pickups.add(
        WeaponPickUp(
            assaultrifle.WEAPON,
            (400, 100),
            terrain
        )
    )

    weapon_pickups.add(
        WeaponPickUp(
            shotgun.WEAPON,
            (500, 100),
            terrain
        )
    )

    weapon_pickups.add(
        WeaponPickUp(
            rocketlauncher.WEAPON,
            (600, 100),
            terrain
        )
    )

def game(game_map: Map):
    # Initialize the game
    pygame.init()
    pygame.display.set_caption("Game")

    # Create the screen and the clock
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    # Get information from the map
    players_pos = game_map.players_pos
    bounds = game_map.bounds
    terrain = game_map.terrain
    terrain.convert()

    running = True

    # Create the players
    players = [
        Player(
            1,
            players_pos[0],
            True,
            Inputs(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s),
            bounds,
            terrain
        ),
        Player(
            2,
            players_pos[1],
            False,
            Inputs(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN),
            bounds,
            terrain
        ),
    ]

    # Create list of bullets and pickups
    bullets = sprite.Group()
    weapon_pickups = WeaponPickUps(terrain)

    add_pickups(weapon_pickups, terrain)

    prev_time = time.time()

    # Main loop
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
            new_bullets = player.update(weapon_pickups, dt)

            if new_bullets:
                bullets.add(new_bullets)

            player.draw(SCREEN)

        # Update bullets
        for bullet in bullets:
            remove = bullet.update(dt, players)

            if remove:
                bullets.remove(bullet)

            bullet.draw(SCREEN)
        
        for weapon_pickup in weapon_pickups:
            weapon_pickup.update(dt)
            weapon_pickup.draw(SCREEN)
        
        weapon_pickups.update(dt)

        # Update the screen
        pygame.display.update()

    pygame.quit()
