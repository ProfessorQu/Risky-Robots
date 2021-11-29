import pygame

from src.constants import *


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, jumpHeight, jumpTime):
        super().__init__()

        self.x = x
        self.y = y

        self.speed = speed
        self.jumpHeight = jumpHeight

        self.velocity = pygame.math.Vector2(0, 0)

        self.facingRight = True

        self.image = pygame.image.load("src/assets/player.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * scale,
                self.image.get_height() * scale
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, terrain: list):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.velocity.x = -self.speed
            self.facingRight = False
        if key[pygame.K_d]:
            self.velocity.x = self.speed
            self.facingRight = True
        if key[pygame.K_w]:
            self.velocity.y = -self.jumpHeight
        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.velocity.x = 0

        self.velocity.y += GRAVITY

        self.checkCollisions(terrain)

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        print(self.rect.x, self.rect.y)

    def checkCollisions(self, terrain: list):
        """ A collision system for a 2D platformer"""
        for tile in terrain:
            if tile.rect.colliderect(self.rect.x, self.rect.y + self.velocity.y, self.rect.width, self.rect.height):
                if self.velocity.y < 0:
                    self.velocity.y = tile.rect.bottom - self.rect.top
                elif self.velocity.y > 0:
                    self.velocity.y = tile.rect.top - self.rect.bottom
            elif tile.rect.colliderect(self.rect.x + self.velocity.x, self.rect.y, self.rect.width, self.rect.height):
                if self.velocity.x < 0:
                    self.velocity.x = tile.rect.right - self.rect.left
                elif self.velocity.x > 0:
                    self.velocity.x = tile.rect.left - self.rect.right

    def draw(self, surface):
        image = pygame.transform.flip(self.image, not self.facingRight, False)
        surface.blit(image, self.rect)
