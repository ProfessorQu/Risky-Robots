import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData
from src.weapons.functions import one_bullet, explode


BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/rocket.png"),
    size = (20, 20),
    speed = 500,
    damage = 75,
    knockback = 100,
    lifetime = 10,
    hit = explode
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/rocketlauncher.png"),
    size = (40, 40),
    cooldown = 100,
    bullet = BULLET,
    shoot = one_bullet
)

WEAPON_SPAWN_RATE = 0.25