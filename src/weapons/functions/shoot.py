import pygame
from src.player.bullet import Bullet

from typing import List


def one_bullet(weapon) -> Bullet:
    """Shoot one bullet

    Args:
        weapon (Weapon): the weapon to shoot

    Returns:
        Bullet: the bullet that was shot
    """
    # Create a bullet
    bullet_pos = (
        weapon.rect.centerx + (weapon.dir * weapon.image.get_width() / 2),
        weapon.rect.centery - weapon.image.get_height() / 4
    )
    bullet = Bullet(
        weapon.weapon_type.bullet,
        bullet_pos, (weapon.dir, 0), 
        weapon.bounds, weapon.terrain)
    # Reset fire rate
    weapon.cooldown = weapon.weapon_type.cooldown


    return bullet

def spread(weapon) -> List[Bullet]:
    """Shoot three bullets

    Args:
        weapon (Weapon): the weapon to shoot

    Returns:
        List[Bullet]: the bullets that were shot
    """
    bullets = []
    # Create bullets
    bullet_pos = (
        weapon.rect.centerx + (weapon.dir * weapon.image.get_width() / 2),
        weapon.rect.centery - weapon.image.get_height() / 4
    )
    bullets.append(Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, 0), weapon.bounds, weapon.terrain))
    bullets.append(Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, -0.2), weapon.bounds, weapon.terrain))
    bullets.append(Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, 0.2), weapon.bounds, weapon.terrain))
    # Reset fire rate
    weapon.cooldown = weapon.weapon_type.cooldown

    return bullets