import pygame

from src.constants import *


class Terrain(list):
    def __init__(self, *args):
        list.__init__(self, args)

    def draw(self, screen):
        for tile in self:
            screen.blit(tile.image, (tile.x, tile.y))

    def collide(self, other, mode="Predict") -> dict:
        collisions = {}
        if mode == "Predict":
            for tile in self:
                if tile.rect.colliderect(other.rect.x, other.rect.y + other.velocity.y, other.rect.width, other.rect.height):
                    if other.velocity.y < 0:
                        collisions[Direction.UP] = tile
                    if other.velocity.y > 1:
                        collisions[Direction.DOWN] = tile

                if tile.rect.colliderect(other.rect.x + other.velocity.x, other.rect.y, other.rect.width, other.rect.height):
                    if other.velocity.x < 0:
                        collisions[Direction.LEFT] = tile
                    if other.velocity.x > 0:
                        collisions[Direction.RIGHT] = tile
        elif mode == "Current":
            for tile in self:
                if tile.rect.colliderect(other.rect.x, other.rect.y, other.rect.width, other.rect.height):
                    if other.velocity.y < 0:
                        collisions[Direction.UP] = tile
                    if other.velocity.y > 1:
                        collisions[Direction.DOWN] = tile

                if tile.rect.colliderect(other.rect.x, other.rect.y, other.rect.width, other.rect.height):
                    if other.velocity.x < 0:
                        collisions[Direction.LEFT] = tile
                    if other.velocity.x > 0:
                        collisions[Direction.RIGHT] = tile

        return collisions


class Solid:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.color = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
