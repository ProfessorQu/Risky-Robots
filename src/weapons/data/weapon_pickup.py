import pygame

from src.terrain import Terrain
from src.weapons.data.weapon import WeaponData
from src.constants.weapon_pickup import *
from src.constants import game
from src.terrain import CollideMode

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

        # Create the velocity
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
        if self.terrain.collide(self, CollideMode.Current):
            self.velocity.y = 0

        if self.rect.x < 0 or self.rect.x > game.WIDTH:
            self.kill()
        if self.rect.y > game.HEIGHT:
            self.kill()

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
