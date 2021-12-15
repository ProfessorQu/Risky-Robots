import pygame

from src.constants import weapon
from src.player.bullet import Bullet

from typing import Tuple


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int, int], terrain):
        """Initialize the weapon

        Args:
            pos (Tuple[int, int]): the position of the weapon
            terrain ([type]): the terrain of the map
        """
        pygame.sprite.Sprite.__init__(self)

        # Get the image of the weapon
        self.image = pygame.image.load("src/assets/weapon.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * weapon.SCALE,
                self.image.get_height() * weapon.SCALE
            )
        )

        # Set the position of the weapon
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.dir = 1

        self.cooldown = 0

        self.terrain = terrain

    def shoot(self):
        """Shoot a bullet

        Returns:
            Bullet: the bullet that was shot
        """
        # Check if the player can shoot
        if self.cooldown <= 0:
            # Create a bullet
            bullet_pos = (
                self.rect.centerx + (self.dir * self.image.get_width() / 2),
                self.rect.centery - self.image.get_height() / 4
            )
            bullet = Bullet(bullet_pos, self.dir, self.terrain)
            # Reset fire rate
            self.cooldown = weapon.COOLDOWN

            return bullet

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
        # Draw the weapon
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)
