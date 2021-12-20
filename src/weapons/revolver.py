import pygame

from src.weapons.data.bullet import BulletData
from src.weapons.data.weapon import WeaponData
from src.player.bullet import Bullet


def shoot(weapon):
    # Create a bullet
    bullet_pos = (
        weapon.rect.centerx + (weapon.dir * weapon.image.get_width() / 2),
        weapon.rect.centery - weapon.image.get_height() / 4
    )
    bullet = Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, 0), weapon.terrain)
    # Reset fire rate
    weapon.cooldown = weapon.weapon_type.cooldown

    return bullet

BULLET = BulletData(
    image = pygame.image.load("src/assets/bullets/bullet.png"),
    size = (25, 25),
    speed = 500,
    damage = 10,
    knockback = pygame.Vector2(500, -100)
)

WEAPON = WeaponData(
    image = pygame.image.load("src/assets/weapons/revolver.png"),
    size = (50, 50),
    cooldown = 100,
    bullet = BULLET,
    shoot = shoot
)

WEAPON_SPAWN_RATE = 0