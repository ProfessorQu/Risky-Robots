import pygame

from src.constants import Direction


class Terrain(list):
    def __init__(self, *args):
        """Initialize the terrain object
        """
        list.__init__(self, args)

    def convert(self):
        """Convert each tile in the terrain to a surface
        """
        for tile in self:
            tile.convert()

    def collide(self, other: pygame.sprite.Sprite):
        for tile in self:
            if tile.rect.colliderect(other.rect):
                tile.collide(other)
                

    def draw(self, surface: pygame.Surface):
        """Draw each tile in the terrain

        Args:
            surface (pygame.Surface): the surface to draw the terrain on
        """
        for tile in self:
            tile.draw(surface)