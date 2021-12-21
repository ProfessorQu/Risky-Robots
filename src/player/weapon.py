import pygame

from src.weapons.data.weapon import WeaponData
from src.terrain import Terrain

from typing import Tuple



class Weapon(pygame.sprite.Sprite):
    def __init__(
        self, weapon_type: WeaponData,
        pos: Tuple[int, int],
        bounds: pygame.Rect, terrain: Terrain
        ):
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

        # Set the cooldown
        self.cooldown = 0

        # Set the terrain
        self.terrain = terrain
        self.bounds = bounds

    def shoot(self):
        """Shoot a bullet

        Returns:
            Bullet: the bullet that was shot
        """
        # Check if the player can shoot
        if self.cooldown <= 0:
            return self.weapon_type.shoot(self)

    def update(self, pos: Tuple[int, int], direction: int):
        """Update the weapon's position

        Args:
            pos (Tuple[int, int]): the new position of the weapon
            direction (int): the direction of the weapon
        """
        # Update the position of the weapon
        self.rect.center = pos
        self.dir = direction

        # Update the cooldown
        self.cooldown -= 1

    def draw(self, screen: pygame.Surface):
        """Draw the weapon

        Args:
            screen (pygame.Surface): the screen to draw the weapon on
        """
        # Set the image
        self.image = self.weapon_type.image
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        # Draw the weapon
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)
