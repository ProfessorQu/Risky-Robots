import pygame
from src.constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/assets/bullet.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * BULLET_SCALE,
                self.image.get_height() * BULLET_SCALE
            )
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = pygame.math.Vector2(BULLET_SPEED, 0)

    def update(self, dt, terrain):
        # self.rect.x += self.velocity.x * dt

        if terrain.collide(self):
            return True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
