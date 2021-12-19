import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (25, 25),
    speed = 500,
    damage = 10,
    knockback = pygame.math.Vector2(500, -100)
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/revolver.png"),
    size = (50, 50),
    cooldown = 100,
    bullet = BULLET
)

WEAPON_SPAWN_RATE = 0