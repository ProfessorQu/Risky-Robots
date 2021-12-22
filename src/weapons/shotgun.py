import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData
from src.weapons.functions import spread, damage


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (20, 20),
    speed = 500,
    damage = 10,
    knockback = pygame.Vector2(100, -50),
    lifetime = 1000,
    hit = damage
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/shotgun.png"),
    size = (40, 40),
    cooldown = 100,
    bullet = BULLET,
    shoot = spread
)

WEAPON_SPAWN_RATE = 0.5