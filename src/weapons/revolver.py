import pygame

from src.weapons.data import *

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/revolver.png"),
    rect = pygame.Rect(0, 0, 10, 10),
    cooldown = 100
)

BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    rect = pygame.Rect(0, 0, 10, 10),
    speed = 500,
    damage = 10
)