import pygame

from src.terrain import Terrain
from src.weapons.data import WeaponData
from src.constants.weapon_pickup import *
from src.constants import Direction

from typing import Tuple

class WeaponPickUp(pygame.sprite.Sprite):
    def __init__(self, weapon_type: WeaponData, pos: Tuple[int, int], terrain: Terrain):
        """Initialize the weapon
        
        Args:
            pos (Tuple[int, int]): the position of the weapon
            terrain ([type]): the terrain of the map
        """
        pygame.sprite.Sprite.__init__(self)
        self.weapon_type = weapon_type

        # Set the position of the weapon
        self.rect = pygame.Rect((0, 0), self.weapon_type.size)
        self.rect.center = pos
        
        # Set the image
        self.image = self.weapon_type.image
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        self.velocity = pygame.math.Vector2(0, GRAVITY)

        # Set the terrain
        self.terrain = terrain
    
    def pickup(self, player):
        """Pick up the weapon
        
        Args:
            player (Player): the player who picked up the weapon
        """
        # Add the weapon to the player
        player.weapon.weapon_type = self.weapon_type
        player.weapon.cooldown = self.weapon_type.cooldown
        self.kill()

    def collide(self):
        """Check if the player collided with the terrain
        """
        # Get all collisions
        collisions = self.terrain.collide(self, "Current")

        # Go through all collisions
        for (tile, direction) in collisions:
            if direction == Direction.UP:
                self.velocity.y = 0
            if direction == Direction.DOWN:
                self.velocity.y = 0

            if direction == Direction.LEFT:
                self.velocity.x = tile.rect.right - self.rect.left
            if direction == Direction.RIGHT:
                self.velocity.x = tile.rect.left - self.rect.right

    def update(self, dt: float):
        """Update the weapon's position

        Args:
            dt (float): the time since the last frame
        """
        # Apply gravity
        self.rect.y += self.velocity.y * dt
        # Check for collision with terrain
        self.collide()

    def draw(self, surface):
        """Draw the weapon
        
        Args:
            surface (pygame.Surface): the surface to draw the weapon on
        """
        surface.blit(self.image, self.rect)
