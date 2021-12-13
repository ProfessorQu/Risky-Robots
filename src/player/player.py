import pygame

from src.constants import player, Direction
from src.player.weapon import Weapon
from src.player.healthbar import HealthBar
from src.player.inputs import Inputs
from src.terrain.terrain import Terrain

from typing import Tuple

# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, player_id: int, pos: Tuple[int, int], facing_right: bool, inputs: Inputs, terrain: Terrain):
        pygame.sprite.Sprite.__init__(self)
        self.player_id = player_id

        self.image = pygame.image.load(f"src/assets/player{player_id}.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * player.SCALE,
                self.image.get_height() * player.SCALE
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

        self.speed = player.SPEED
        self.jump_height = player.JUMP_HEIGHT
        self.max_jumps = player.MAX_JUMPS
        self.health = player.MAX_HEALTH

        self.healthbar = HealthBar(self.rect)

    def hit(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print(f"Player {self.player_id} died!")
            print(f"Player {1 if self.player_id == 2 else 2} won!")
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def handle_collisions(self):
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

    def update(self, dt: float):
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

        gravity = player.GRAVITY * dt if self.velocity.y < 0 else player.GRAVITY_FALL * dt
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

        self.healthbar.update(self.rect)

        return new_bullet

    def draw(self, screen: pygame.Surface):
        image = pygame.transform.flip(self.image, not self.facing_right, False)
        screen.blit(image, self.rect)

        self.weapon.draw(screen)

        self.healthbar.draw(screen, self.health)


