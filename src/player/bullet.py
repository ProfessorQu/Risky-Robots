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

        # Set the position and velocity
        self.pos = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(direction) * self.bullet_type.speed
        
        # Create the rect
        self.rect = pygame.Rect((0, 0), self.bullet_type.size)
        self.rect.center = self.pos
        
        # Set the image
        self.image = self.bullet_type.image
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

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
        self.pos.x += self.velocity.x * dt
        self.pos.y += self.velocity.y * dt

        # Check for hit with players
        for player in players:
            if self.rect.colliderect(player.rect):
                self.bullet_type.hit(self, player, players, True)
        
        # Check for hit with terrain or out of bounds
        if (self.rect.x < 0 or self.rect.x > game.WIDTH):
            self.bullet_type.hit(self, None, players, False)
        if self.rect.y < 0 or self.rect.y > game.HEIGHT:
            self.bullet_type.hit(self, None, players, False)
        if self.terrain.collide(self, CollideMode.Current):
            self.bullet_type.hit(self, None, players, False)
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y


    def draw(self, surface: pygame.Surface):
        """Draw the bullet

        Args:
            surface (pygame.Surface): the surface to draw the bullet on
        """
        # Draw the bullet
        angle = self.velocity.angle_to(pygame.math.Vector2(1, 0))
        image = pygame.transform.rotate(self.image, angle)
        surface.blit(image, self.rect)
