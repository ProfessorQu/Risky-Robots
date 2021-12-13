import pygame

from src.constants import Direction


class Terrain(list):
    def __init__(self, *args):
        list.__init__(self, args)

    def draw(self, screen: pygame.Surface):
        for tile in self:
            tile.draw(screen)

    def collide(self, other: pygame.sprite.Sprite, mode: str="Predict") -> dict:
        collisions = []
        for tile in self:
            if mode == "Current":
                if tile.rect.colliderect(other.rect.x, other.rect.y, other.rect.width, other.rect.height):
                    if other.velocity.y < 0:
                        collisions.append((tile, Direction.UP))
                    if other.velocity.y > 1:
                        collisions.append((tile, Direction.DOWN))

                    if other.velocity.x < 0:
                        collisions.append((tile, Direction.LEFT))
                    if other.velocity.x > 0:
                        collisions.append((tile, Direction.RIGHT))

            elif mode == "Predict":
                if tile.rect.colliderect(other.rect.x, other.rect.y + other.velocity.y, other.rect.width, other.rect.height):
                    if other.velocity.y < 0:
                        collisions.append((tile, Direction.UP))
                    if other.velocity.y > 1:
                        collisions.append((tile, Direction.DOWN))

                if tile.rect.colliderect(other.rect.x + other.velocity.x, other.rect.y, other.rect.width, other.rect.height):
                    if other.velocity.x < 0:
                        collisions.append((tile, Direction.LEFT))
                    if other.velocity.x > 0:
                        collisions.append((tile, Direction.RIGHT))
        return collisions
