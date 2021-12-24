import pygame
import random

from src.constants.weapon_pickup import *
from src.weapons.data.weapon_pickup import WeaponPickUp
from src.constants import game
from src.terrain import Terrain, CollideMode

class WeaponPickUps(pygame.sprite.Group):
    def __init__(self, terrain: Terrain):
        """Initialize the weapon pickups

        Args:
            terrain (Terrain): the terrain of the map
        """
        super().__init__()

        # Set the terrain
        self.terrain = terrain

        # Set the spawn timer
        self.spawn_timer = SPAWN_RATE

        # Set the weapon pickup spawn locations
        self.spawn_locations = []
        for tile in terrain:
            for x in range(tile.rect.width):
                spawn_location = pygame.Vector2(tile.rect.left + x, tile.rect.top)
                self.spawn_locations.append(spawn_location)
    
    def update(self, dt: float):
        """Update the weapon pickups

        Args:
            dt (float): the time since the last frame
        """
        if self.spawn_timer > 0:
            self.spawn_timer -= dt
        else:
            self.spawn_timer = SPAWN_RATE
            pickups, weights = list(zip(*WEAPON_PICKUPS))
            pickup = random.choices(pickups, weights=weights)[0]
            pos_x = random.randint(0, game.WIDTH)
            
            spawn_location = random.choice(self.spawn_locations)
            spawn_location.y -= pickup.size[1]

            rect = pygame.Rect(0, 0, pickup.size[0], pickup.size[1])
            rect.center = spawn_location

            tries = 0
            while self.terrain.collide(rect, CollideMode.Current) and tries < 1000:
                spawn_location.x = random.randint(0, game.WIDTH)
                rect.center = spawn_location

                tries += 1
            
            if tries == 1000:
                return

            self.add(WeaponPickUp(pickup, spawn_location, self.terrain))

        for weapon_pickup in self:
            weapon_pickup.update(dt)


