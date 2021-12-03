import pygame

from src.constants import *
from src.bullet import Bullet


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, dir, bullet, fireRate):
        self.offset = pygame.math.Vector2(x, y)

        self.image = pygame.image.load("src/assets/weapon.png")

        self.bullet = bullet
        self.fireRate = fireRate

    def draw(self, screen, ):
        pass
