import pygame

from src.player.bullet import Bullet
# from src.player.player import Player

from typing import List


def damage(bullet: Bullet, obj: pygame.sprite.Sprite, players: List, player_hit: bool):
    if player_hit:
        horizontal_knockback = bullet.bullet_type.knockback.x if bullet.velocity.x > 0 else -bullet.bullet_type.knockback.x
        knockback = pygame.Vector2(horizontal_knockback, bullet.bullet_type.knockback.y)
        obj.hit(bullet.bullet_type.damage, knockback)
    
    bullet.kill()

def explode(bullet: Bullet, obj: pygame.sprite.Sprite, players: List, player_hit: bool):
    collide_pos = pygame.Vector2(bullet.rect.center)
    for player in players:
        player_pos = pygame.Vector2(player.rect.center)
        distance = collide_pos.distance_to(player_pos)
        if distance < 300:
            knockback = player_pos - collide_pos
            knockback *= bullet.bullet_type.knockback
            player.hit((1 / distance) * bullet.bullet_type.damage, knockback)
    
    bullet.kill()