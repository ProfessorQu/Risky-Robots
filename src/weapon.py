import pygame

from src.constants import *
from src.bullet import Bullet


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, terrain):
        self.image = pygame.image.load("src/assets/weapon.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * WeaponVars.SCALE,
                self.image.get_height() * WeaponVars.SCALE
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.bullets = []
        self.fireRate = 0

        self.dir = direction

        self.terrain = terrain

    def shoot(self):
        if self.fireRate <= 0:
            self.bullets.append(
                Bullet(self.rect.centerx, self.rect.centery, self.dir, self.terrain))
            self.fireRate = WeaponVars.FIRE_RATE

    def update(self, dt, pos, direction):
        self.rect.center = pos
        self.dir = direction

        self.fireRate -= 1
        for bullet in self.bullets:
            remove = bullet.update(dt)
            if remove:
                self.bullets.remove(bullet)

    def draw(self, screen):
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)

        for bullet in self.bullets:
            bullet.draw(screen)
