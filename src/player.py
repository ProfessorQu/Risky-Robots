import pygame

from src.constants import *
from src.bullet import Bullet


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.jumps = 0

        self.velocity = pygame.math.Vector2(0, 0)

        self.facing_right = True

        self.bullets = []

        self.image = pygame.image.load("src/assets/player.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * PLAYER_SCALE,
                self.image.get_height() * PLAYER_SCALE
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, dt, terrain):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.velocity.x = -PLAYER_SPEED * dt
            self.facing_right = False
        if key[pygame.K_d]:
            self.velocity.x = PLAYER_SPEED * dt
            self.facing_right = True
        if key[pygame.K_w] and self.jumps > 0 and self.velocity.y > 0:
            self.velocity.y = PLAYER_JUMP_HEIGHT * dt
            self.jumps -= 1

        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.velocity.x = 0

        if key[pygame.K_s] and len(self.bullets) < 1:
            bullet = self.fireBullet()
            self.bullets.append(bullet)

        self.velocity.y += GRAVITY * dt

        self.handleCollisions(terrain)

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        for bullet in self.bullets:
            remove = bullet.update(dt, terrain)
            if remove:
                pass

    def handleCollisions(self, terrain):
        """ A collision system for a 2D platformer"""
        collisions = terrain.collide(self)
        for (direction, tile) in collisions.items():
            if direction == Direction.UP:
                self.velocity.y = tile.rect.bottom - self.rect.top
            if direction == Direction.DOWN:
                self.velocity.y = tile.rect.top - self.rect.bottom
                self.jumps = PLAYER_MAX_JUMPS

            if direction == Direction.LEFT:
                self.velocity.x = tile.rect.right - self.rect.left
            if direction == Direction.RIGHT:
                self.velocity.x = tile.rect.left - self.rect.right

    def fireBullet(self):
        return (
            Bullet(self.rect.right, self.rect.centery, 1)
            if self.facing_right
            else Bullet(self.rect.left, self.rect.centery, -1)
        )

    def draw(self, screen):
        image = pygame.transform.flip(self.image, not self.facing_right, False)
        screen.blit(image, self.rect)
