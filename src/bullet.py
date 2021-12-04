import pygame

from src.constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, terrain):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/assets/bullet.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * BulletVars.SCALE,
                self.image.get_height() * BulletVars.SCALE,
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.dir = direction

        self.velocity = pygame.math.Vector2(
            direction * BulletVars.SPEED, 0
        )

        self.terrain = terrain

    def update(self, dt):
        self.rect.x += self.velocity.x * dt

        if self.rect.x < 0 or self.rect.x > WIDTH:
            return True
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            return True

        return self.terrain.collide(self, "Current")

    def draw(self, screen):
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)
