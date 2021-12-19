import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (25, 25),
    speed = 1000,
    damage = 20,
    knockback = pygame.math.Vector2(2_000, -200)
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/sniperrifle.png"),
    size = (50, 50),
    cooldown = 150,
    bullet = BULLET
)

WEAPON_SPAWN_RATE = 0.5