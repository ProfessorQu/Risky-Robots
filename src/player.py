import pygame

from src.constants import *


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, jump_height, max_jumps):
        super().__init__()

        self.x = x
        self.y = y

        self.speed = speed

        self.jumps = max_jumps
        self.max_jumps = max_jumps
        self.jump_height = jump_height

        self.velocity = pygame.math.Vector2(0, 0)

        self.facing_right = True

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

    def update(self, dt, terrain):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.velocity.x = -self.speed * dt
            self.facing_right = False
        if key[pygame.K_d]:
            self.velocity.x = self.speed * dt
            self.facing_right = True
        if key[pygame.K_w] and self.jumps > 0 and self.velocity.y > 0:
            self.velocity.y = -self.jump_height * dt
            self.jumps -= 1

        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.velocity.x = 0

        self.velocity.y += GRAVITY * dt

        self.handleCollisions(terrain)

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def handleCollisions(self, terrain):
        """ A collision system for a 2D platformer"""
        tile, direction = terrain.collide(self)
        if tile is not None:
            if direction == Direction.UP:
                self.velocity.y = tile.rect.bottom - self.rect.top
            elif direction == Direction.DOWN:
                self.velocity.y = tile.rect.top - self.rect.bottom
                self.jumps = self.max_jumps

            if direction == Direction.LEFT:
                self.velocity.x = tile.rect.right - self.rect.left
            elif direction == Direction.RIGHT:
                self.velocity.x = tile.rect.left - self.rect.right

    def draw(self, surface):
        image = pygame.transform.flip(self.image, not self.facing_right, False)
        surface.blit(image, self.rect)
