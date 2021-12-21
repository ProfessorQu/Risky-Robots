import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData
from src.weapons.functions import spread, damage


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (25, 25),
    speed = 500,
    damage = 10,
    knockback = pygame.Vector2(500, -100),
    lifetime = 1000,
    hit = damage
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/shotgun.png"),
    size = (50, 50),
    cooldown = 100,
    bullet = BULLET,
    shoot = spread
)

WEAPON_SPAWN_RATE = 0.5