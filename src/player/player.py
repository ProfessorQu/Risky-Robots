import pygame

from src.constants import *
from src.player.weapon import Weapon
from src.player.healthbar import HealthBar


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, player_id, pos, facing_right, inputs, terrain):
        pygame.sprite.Sprite.__init__(self)
        self.player_id = player_id

        self.image = pygame.image.load(f"src/assets/player{player_id}.png")
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
        self.facing_right = facing_right
        self.jumps = 0

        self.weapon = Weapon(pos, terrain)

        self.speed = PlayerVars.SPEED
        self.jump_height = PlayerVars.JUMP_HEIGHT
        self.max_jumps = PlayerVars.MAX_JUMPS
        self.health = PlayerVars.MAX_HEALTH

        color = (255, 0, 0) if player_id == 1 else (0, 0, 255)
        rect = pygame.Rect(self.rect.x - self.rect.width * 5, self.rect.height, self.rect.width * 5, self.rect.height)
        self.healthbar = HealthBar(rect, color)


    def update(self, dt):
        inputs = self.inputs.get_inputs()

        new_bullet = None

        if Direction.LEFT in inputs:
            self.velocity.x = -self.speed * dt
            self.facing_right = False

        if Direction.RIGHT in inputs:
            self.velocity.x = self.speed * dt
            self.facing_right = True

        if Direction.UP in inputs and self.jumps > 0 and self.velocity.y >= 0:
            self.velocity.y = self.jump_height * dt
            self.jumps -= 1

        if not Direction.LEFT in inputs and not Direction.RIGHT in inputs:
            self.velocity.x = 0

        if Direction.DOWN in inputs:
            new_bullet = self.weapon.shoot()

        gravity = GRAVITY * dt if self.velocity.y < 0 else GRAVITY_FALL * dt
        self.velocity.y += gravity

        self.handle_collisions()

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        direction = 1 if self.facing_right else -1
        weapon_x = self.rect.centerx + (
            direction * self.image.get_width() * 0.5
        )

        self.weapon.update(
            (weapon_x, self.rect.centery),
            direction
        )

        return new_bullet

    def draw(self, screen):
        image = pygame.transform.flip(self.image, not self.facing_right, False)
        screen.blit(image, self.rect)

        self.weapon.draw(screen)

        self.healthbar.draw(screen, self.health)


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

