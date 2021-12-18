import pygame

from src.weapons.data import *


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (25, 25),
    speed = 1000,
    damage = 20
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/sniperrifle.png"),
    size = (50, 50),
    cooldown = 200,
    bullet = BULLET
)