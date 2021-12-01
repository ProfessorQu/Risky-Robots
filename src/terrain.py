import pygame

from src.constants import *


class Terrain(list):
    def __init__(self, *args):
        list.__init__(self, args)

    def draw(self, screen):
        for tile in self:
            screen.blit(tile.image, (tile.x, tile.y))

    def collide(self, other):
        for tile in self:
            if tile.rect.colliderect(other.rect.x, other.rect.y + other.velocity.y, other.rect.width, other.rect.height):
                if other.velocity.y < 0:
                    return tile, Direction.UP
                elif other.velocity.y > 0:
                    return tile, Direction.DOWN

            if tile.rect.colliderect(other.rect.x + other.velocity.x, other.rect.y, other.rect.width, other.rect.height):
                if other.velocity.x < 0:
                    return tile, Direction.LEFT
                elif other.velocity.x > 0:
                    return tile, Direction.RIGHT

        return None, None


class Solid:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
