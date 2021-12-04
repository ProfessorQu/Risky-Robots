import pygame

from src.constants import *
from src.weapon import Weapon


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, terrain):
        super().__init__()

        self.jumps = 0

        self.speed = PlayerVars.SPEED
        self.jump_height = PlayerVars.JUMP_HEIGHT
        self.max_jumps = PlayerVars.MAX_JUMPS

        self.velocity = pygame.math.Vector2(0, 0)

        self.facing_right = True

        self.terrain = terrain

        self.image = pygame.image.load("src/assets/player.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * PlayerVars.SCALE,
                self.image.get_height() * PlayerVars.SCALE
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.weapon = Weapon(x, y, 1, self.terrain)

    def update(self, dt):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.velocity.x = -self.speed * dt
            self.facing_right = False

        if key[pygame.K_d]:
            self.velocity.x = self.speed * dt
            self.facing_right = True

        if key[pygame.K_w] and self.jumps > 0 and self.velocity.y >= 0:
            self.velocity.y = self.jump_height * dt
            self.jumps -= 1

        if not key[pygame.K_a] and not key[pygame.K_d]:
            self.velocity.x = 0

        if key[pygame.K_s]:
            self.weapon.shoot()

        gravity = GRAVITY * dt if self.velocity.y < 0 else GRAVITY_FALL * dt
        self.velocity.y += gravity

        self.handleCollisions()

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.weapon.update(dt, self.rect.center,
                           1 if self.facing_right else -1)

    def handleCollisions(self):
        """ A collision system for a 2D platformer"""
        collisions = self.terrain.collide(self)
        for (tile, direction) in collisions:
            if direction == Direction.UP:
                self.velocity.y = tile.rect.bottom - self.rect.top
            if direction == Direction.DOWN:
                self.velocity.y = tile.rect.top - self.rect.bottom
                self.jumps = self.max_jumps

            if direction == Direction.LEFT:
                self.velocity.x = tile.rect.right - self.rect.left
            if direction == Direction.RIGHT:
                self.velocity.x = tile.rect.left - self.rect.right

    def draw(self, screen):
        image = pygame.transform.flip(self.image, not self.facing_right, False)
        screen.blit(image, self.rect)

        self.weapon.draw(screen)
