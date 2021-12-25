import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData
from src.weapons.functions import one_bullet, damage


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/goldenbullet.png"),
    size = (20, 20),
    speed = 500,
    damage = 100,
    knockback = pygame.Vector2(100, -50),
    lifetime = 5,
    hit = damage
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/goldenrevolver.png"),
    size = (40, 40),
    cooldown = 100,
    bullet = BULLET,
    shoot = one_bullet
)