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

        self.collisionRect = pygame.Rect(
            self.rect.x + 5,
            self.rect.y + 5,
            self.rect.width - 10,
            self.rect.height - 10
        )

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

    def checkCollisions(self, terrain: list):
        for tile in terrain:
            if self.rect.colliderect(tile.rect):
                if self.rect.right > tile.rect.left and self.rect.left < tile.rect.right:
                    if self.rect.bottom + self.velocity.y > tile.rect.top:
                        self.velocity.y = 0
                        self.rect.bottom = tile.rect.top
                    elif self.rect.top + self.velocity.y < tile.rect.bottom:
                        self.velocity.y = 0
                        self.rect.top = tile.rect.bottom

                # if self.rect.bottom > tile.rect.top and self.rect.top < tile.rect.bottom:
                #     if self.rect.right + self.velocity.x > tile.rect.left:
                #         self.velocity.x = 0
                #         self.rect.right = tile.rect.left
                #     elif self.rect.left + self.velocity.x < tile.rect.right:
                #         self.velocity.x = 0
                #         self.rect.left = tile.rect.right

    def draw(self, surface):
        image = pygame.transform.flip(self.image, not self.facingRight, False)
        surface.blit(image, self.rect)
