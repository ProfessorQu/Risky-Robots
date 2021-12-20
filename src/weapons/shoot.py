from src.player.bullet import Bullet

def one_bullet(weapon):
    # Create a bullet
    bullet_pos = (
        weapon.rect.centerx + (weapon.dir * weapon.image.get_width() / 2),
        weapon.rect.centery - weapon.image.get_height() / 4
    )
    bullet = Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, 0), weapon.terrain)
    # Reset fire rate
    weapon.cooldown = weapon.weapon_type.cooldown

    return bullet

def spread(weapon):
    bullets = []
    # Create bullets
    bullet_pos = (
        weapon.rect.centerx + (weapon.dir * weapon.image.get_width() / 2),
        weapon.rect.centery - weapon.image.get_height() / 4
    )
    bullets.append(Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, 0), weapon.terrain))
    bullets.append(Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, -0.1), weapon.terrain))
    bullets.append(Bullet(weapon.weapon_type.bullet, bullet_pos, (weapon.dir, 0.2), weapon.terrain))
    # Reset fire rate
    weapon.cooldown = weapon.weapon_type.cooldown

    return bullets