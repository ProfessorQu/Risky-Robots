import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData
from src.weapons.functions import one_bullet, damage


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (20, 20),
    speed = 500,
    damage = 1,
    knockback = pygame.Vector2(40, 0),
    lifetime = 5,
    hit = damage
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/assaultrifle.png"),
    size = (40, 40),
    cooldown = 10,
    bullet = BULLET,
    shoot = one_bullet
)

WEAPON_SPAWN_RATE = 0.5