import pygame
import random

from src.constants.weapon_pickup import *
from src.weapons.data.weapon_pickup import WeaponPickUp
from src.constants import game

class WeaponPickUps(pygame.sprite.Group):
    def __init__(self, terrain):
        super().__init__()

        self.terrain = terrain

        self.spawn_timer = SPAWN_RATE
    
    def update(self, dt):
        if self.spawn_timer > 0:
            self.spawn_timer -= dt
        else:
            self.spawn_timer = SPAWN_RATE
            pickups, weights = list(zip(*WEAPON_PICKUPS))
            pickup = random.choices(pickups, weights=weights)[0]
            pos = (random.randint(0, game.WIDTH), 0)

            self.add(WeaponPickUp(pickup, pos, self.terrain))


