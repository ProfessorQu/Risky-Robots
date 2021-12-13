import pygame

from src.constants import weapon
from src.bullet import Bullet

from typing import Tuple


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int, int], terrain):
        """Initialize the weapon

        Args:
            pos (): [description]
            terrain ([type]): [description]
        """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("src/assets/weapon.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * weapon.SCALE,
                self.image.get_height() * weapon.SCALE
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.dir = 1

        self.fireRate = 0

        self.terrain = terrain

    def shoot(self):
        # Check if the player can shoot
        if self.fireRate <= 0:
            # Create a bullet
            bullet_pos = (
                self.rect.centerx + (self.dir * self.image.get_width() / 2),
                self.rect.centery - self.image.get_height() / 4
            )
            bullet = Bullet(bullet_pos, self.dir, self.terrain)
            # Reset fire rate
            self.fireRate = weapon.FIRE_RATE

            return bullet

    def update(self, pos: Tuple[int, int], direction: int):
        self.rect.center = pos
        self.dir = direction

        self.fireRate -= 1

    def draw(self, screen: pygame.Surface):
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)
