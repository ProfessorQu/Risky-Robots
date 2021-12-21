import pygame
import random

from src.constants.weapon_pickup import *
from src.weapons.data.weapon_pickup import WeaponPickUp
from src.constants import game
from src.terrain import Terrain

class WeaponPickUps(pygame.sprite.Group):
    def __init__(self, terrain: Terrain):
        """Initialize the weapon pickups

        Args:
            terrain (Terrain): the terrain of the map
        """
        super().__init__()

        self.terrain = terrain

        self.spawn_timer = SPAWN_RATE
    
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
            pos = (random.randint(0, game.WIDTH), 0)

            self.add(WeaponPickUp(pickup, pos, self.terrain))


