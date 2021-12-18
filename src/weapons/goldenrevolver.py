import pygame

from src.weapons.data import *


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/goldenbullet.png"),
    size = (25, 25),
    speed = 500,
    damage = 100,
    knockback = pygame.math.Vector2(1_000, -400)
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/goldenrevolver.png"),
    size = (50, 50),
    cooldown = 100,
    bullet = BULLET
)