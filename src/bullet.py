import pygame

from src.constants import bullet, game
from src.terrain.terrain import Terrain

from typing import Tuple, List


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int, int], direction: int, terrain: Terrain):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("src/assets/bullet.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * bullet.SCALE,
                self.image.get_height() * bullet.SCALE,
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.dir = direction

        self.velocity = pygame.math.Vector2(
            direction * bullet.SPEED, 0
        )

        self.terrain = terrain

    def update(self, dt: float, players: List[pygame.sprite.Sprite]):
        self.rect.x += self.velocity.x * dt

        for player in players:
            if self.rect.colliderect(player.rect):
                player.hit(bullet.DAMAGE)

                return True
            

        if (self.rect.x < 0 or self.rect.x > game.WIDTH):
            return True
        if self.rect.y < 0 or self.rect.y > game.HEIGHT:
            return True
        if self.terrain.collide(self, "Current"):
            return True
        
        return False

    def draw(self, screen: pygame.Surface):
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)
