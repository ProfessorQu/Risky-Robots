import pygame

from src.weapons.data import *


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (25, 25),
    speed = 500,
    damage = 1
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/assaultrifle.png"),
    size = (50, 50),
    cooldown = 50,
    bullet = BULLET
)