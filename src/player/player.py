import pygame

from src.constants import *
from src.player.weapon import Weapon


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, player_id, pos, inputs, terrain):
        super().__init__()
        self.player_id = player_id

        self.image = pygame.image.load("src/assets/player.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * PlayerVars.SCALE,
                self.image.get_height() * PlayerVars.SCALE
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.inputs = inputs

        self.terrain = terrain

        self.velocity = pygame.math.Vector2(0, 0)
        self.facing_right = True
        self.jumps = 0

        self.weapon = Weapon(pos, terrain)

        self.speed = PlayerVars.SPEED
        self.jump_height = PlayerVars.JUMP_HEIGHT
        self.max_jumps = PlayerVars.MAX_JUMPS

    def update(self, dt, screen):
        inputs = self.inputs.get_inputs()

        if "left" in inputs:
            self.velocity.x = -self.speed * dt
            self.facing_right = False

        if "right" in inputs:
            self.velocity.x = self.speed * dt
            self.facing_right = True

        if "jump" in inputs and self.jumps > 0 and self.velocity.y >= 0:
            self.velocity.y = self.jump_height * dt
            self.jumps -= 1

        if not "left" in inputs and not "right" in inputs:
            self.velocity.x = 0

        if "shoot" in inputs:
            self.weapon.shoot(self.player_id)

        gravity = GRAVITY * dt if self.velocity.y < 0 else GRAVITY_FALL * dt
        self.velocity.y += gravity

        self.handle_collisions()

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        self.draw(screen)

        self.weapon.update(
            0, self.rect.center,
            1 if self.facing_right else -1
        )

    def handle_collisions(self):
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
