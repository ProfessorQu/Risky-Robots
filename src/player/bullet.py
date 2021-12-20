import pygame

from src.constants import game
from src.terrain import Terrain
# from src.weapons.data.bullet import BulletData
from src.terrain import CollideMode

from typing import Tuple, List


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_type, pos: Tuple[int, int], direction: pygame.math.Vector2, terrain: Terrain):
        """Initialize the bullet

        Args:
            pos (Tuple[int, int]): the position of the bullet
            direction (int): the direction of the bullet
            terrain (Terrain): the terrain of the map
        """        """"""
        pygame.sprite.Sprite.__init__(self)
        self.bullet_type = bullet_type

        # Create the rect
        self.rect = pygame.Rect((0, 0), self.bullet_type.size)
        self.rect.center = pos
        
        # Set the image
        self.image = self.bullet_type.image
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        # Set the direction and velocity
        self.velocity = pygame.math.Vector2(direction) * self.bullet_type.speed

        # Set the terrain
        self.terrain = terrain

    def update(self, dt: float, players: List[pygame.sprite.Sprite]) -> bool:
        """Update the bullet's position

        Args:
            dt (float): the time since the last frame
            players (List[pygame.sprite.Sprite]): the list of players

        Returns:
            bool: True if the bullet is still alive, False otherwise
        """
        # Update the position
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

        # Check for hit with players
        for player in players:
            if self.rect.colliderect(player.rect):
                horizontal_knockback = self.bullet_type.knockback.x if self.velocity.x > 0 else -self.bullet_type.knockback.x
                knockback = pygame.Vector2(horizontal_knockback, self.bullet_type.knockback.y)
                player.hit(self.bullet_type.damage, knockback)

                self.kill()
        
        # Check for hit with terrain or out of bounds
        if (self.rect.x < 0 or self.rect.x > game.WIDTH):
            self.kill()
        if self.rect.y < 0 or self.rect.y > game.HEIGHT:
            self.kill()
        if self.terrain.collide(self, CollideMode.Current):
            self.kill()


    def draw(self, surface: pygame.Surface):
        """Draw the bullet

        Args:
            surface (pygame.Surface): the surface to draw the bullet on
        """
        # Draw the bullet
        angle = self.velocity.angle_to(pygame.math.Vector2(1, 0))
        image = pygame.transform.rotate(self.image, angle)
        surface.blit(image, self.rect)
