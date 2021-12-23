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
from typing import List, Tuple


def add_pickups(weapon_pickups: WeaponPickUps, terrain: Terrain):
    """Add all weapons as pickups to the map

    Args:
        weapon_pickups (WeaponPickUps): the weapon pickups
        terrain (Terrain): the terrain of the map
    """
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


def setup(game_map: Map, inputs: List[Inputs]) -> Tuple[sprite.Group, sprite.Group, WeaponPickUps, sprite.Group, Terrain, pygame.Surface, List[bool]]:
    """Setup the game

    Args:
        game_map (Map): the map

    """
    # Initialize the game
    pygame.init()
    pygame.display.set_caption("Game")

    # Get information from the map
    players_pos = game_map.players_pos
    bounds = game_map.bounds

    terrain = game_map.terrain
    terrain.convert()

    void = pygame.image.load("src/assets/terrain/void.png")
    void.fill(VOID_COLOR, special_flags=BLEND_RGBA_MULT)

    # Create the players
    players = sprite.Group()
    for i, input in enumerate(inputs):
        facing_right = i % 2 == 0
        player = Player(
            i + 1,
            players_pos[i],
            facing_right,
            input,
            bounds,
            terrain
        )
        players.add(player)

    # Create list of bullets and pickups
    bullets = sprite.Group()
    weapon_pickups = WeaponPickUps(terrain)

    particles = sprite.Group()

    # add_pickups(weapon_pickups, terrain)

    players_dead = [False for player in players]

    return players, bullets, weapon_pickups, particles, terrain, void, players_dead


def calculate_dt(start_time: float) -> float:
    """Calculate the delta time

    Args:
        start_time (float): the time the game started

    Returns:
        float: the delta time
    """
    now = time.time()
    return now - start_time


def game(game_map: Map, SCREEN: pygame.Surface, CLOCK: pygame.time.Clock, inputs: List[Inputs]):
    """Run the game

    Args:
        game_map (Map): the map
        SCREEN (pygame.Surface): the screen
        CLOCK (pygame.time.Clock): the clock
    """
    # Setup the game
    players, bullets, weapon_pickups, particles, terrain, void, players_dead = setup(game_map, inputs)

    # Set the start time
    prev_time = time.time()

    running = True

    # Main loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Tick
        CLOCK.tick(FPS)

        # Calculate delta time
        dt = calculate_dt(prev_time)
        prev_time = time.time()

        # Set background color
        SCREEN.fill(BACKGROUND_COLOR)
        SCREEN.blit(void, (0, 0, WIDTH, HEIGHT))

        # Draw terrain
        terrain.draw(SCREEN)

        # Update players
        for player in players:
            new_bullets = player.update(weapon_pickups, dt)

            if new_bullets:
                bullets.add(new_bullets)

            player.draw(SCREEN)

            if player.health <= 0:
                players_dead[player.player_id - 1] = True
        
        # Check if all players but one are dead
        finished = sum(players_dead) == len(players_dead) - 1

        if finished:
            for player in players:
                if not players_dead[player.player_id - 1]:
                    print(f"Player {player.player_id} won!")

            running = False
        
        # Update bullets
        update_bullets(SCREEN, bullets, players, particles, dt)

        # Update weapon pickups and particles
        update_misc(SCREEN, particles, weapon_pickups, dt)
        
        # Update the screen
        pygame.display.update()


def update_bullets(SCREEN: pygame.Surface, bullets: sprite.Group, players: sprite.Group, particles: sprite.Group, dt: float):
    """Update the bullets

    Args:
        SCREEN (pygame.Surface): the screen
        bullets (sprite.Group): the bullets
        players (sprite.Group): the players
        particles (sprite.Group): the particles
        dt (float): the delta time
    """
    # Update bullets
    for bullet in bullets:
        remove = bullet.update(dt, players, particles)

        if remove:
            bullets.remove(bullet)

        bullet.draw(SCREEN)


def update_misc(SCREEN: pygame.Surface, particles: sprite.Group, weapon_pickups: WeaponPickUps, dt: float):
    """Update misc

    Args:
        SCREEN (pygame.Surface): the screen
        particles (sprite.Group): the particles
        weapon_pickups (WeaponPickUps): the weapon pickups
        dt (float): the delta time
    """    
    # Update particles
    particles.update()
    for particle in particles:
        particle.update()
        particle.draw(SCREEN)
    
    # Update weapon pickups
    weapon_pickups.update(dt)
    for weapon_pickup in weapon_pickups:
        weapon_pickup.draw(SCREEN)

