import pygame

from src.constants import *
from src.bullet import Bullet


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, terrain):
        self.image = pygame.image.load("src/assets/weapon.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * WeaponVars.SCALE,
                self.image.get_height() * WeaponVars.SCALE
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.fireRate = 0

        self.dir = 1

        self.terrain = terrain

    def shoot(self, player_id):
        if self.fireRate <= 0:
            bullet_pos = (
                self.rect.centerx + (self.dir * self.image.get_width() / 2),
                self.rect.centery - self.image.get_height() / 4
            )
            bullet = Bullet(player_id, bullet_pos, self.dir, self.terrain)
            self.fireRate = WeaponVars.FIRE_RATE

            return bullet

    def update(self, pos, direction, screen):
        self.rect.center = pos
        self.dir = direction

        self.fireRate -= 1

        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)
