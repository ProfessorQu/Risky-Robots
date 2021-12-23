import pygame

from src.player.bullet import Bullet
from src.weapons.data.particle import Particle
from src.constants import particle

from typing import List
import random



def damage(bullet: Bullet, obj: pygame.sprite.Sprite, players: List, particles: List[Particle], player_hit: bool):
    """Damage the player

    Args:
        bullet (Bullet): the bullet that hit the player
        obj (pygame.sprite.Sprite): the object that was hit
        players (List): the list of players
        player_hit (bool): whether or not the player was hit
    """
    if player_hit:
        # Calculate the knockback
        horizontal_knockback = bullet.bullet_type.knockback.x if bullet.velocity.x > 0 else -bullet.bullet_type.knockback.x
        knockback = pygame.Vector2(horizontal_knockback, bullet.bullet_type.knockback.y)
        # Do damage
        obj.hit(bullet.bullet_type.damage, knockback)
    
    bullet.kill()

def explode(bullet: Bullet, obj: pygame.sprite.Sprite, players: List, particles: List[Particle], player_hit: bool):
    """Explode

    Args:
        bullet (Bullet): the bullet that hit the player
        obj (pygame.sprite.Sprite): the object that was hit
        players (List): the list of players
        player_hit (bool): whether or not the player was hit
    """
    explosion_sound = pygame.mixer.Sound("src/assets/sounds/shoot.wav")

    collide_pos = pygame.Vector2(bullet.rect.center)
    # Apply knockback to all players
    for player in players:
        # Check if the player is hit
        player_pos = pygame.Vector2(player.rect.center)
        distance = collide_pos.distance_to(player_pos)
        if distance < 200:
            # Calculate the knockback
            knockback = player_pos - collide_pos
            knockback.normalize_ip()

            # Calculate variable
            var =  (200 - distance) / 200 # 0 to 1

            # Apply knockback and damage
            knockback *= var * bullet.bullet_type.knockback
            player.hit(var * bullet.bullet_type.damage, knockback)

    # Create particles
    for _ in range(particle.NUM_PARTICLES):
        # Get color
        color = (255, random.randint(0, 255), 0)
        velocity = pygame.Vector2(random.uniform(particle.MIN_VELOCITY, particle.MAX_VELOCITY), random.uniform(particle.MIN_VELOCITY, particle.MAX_VELOCITY))
        radius = random.uniform(particle.MIN_RADIUS, particle.MAX_RADIUS)
        lifetime = random.uniform(particle.MIN_LIFETIME, particle.MAX_LIFETIME)
        particles.add(Particle(collide_pos, velocity, radius, color, lifetime))
    
    explosion_sound.play()

    bullet.kill()
    