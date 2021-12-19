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
        grounded = False
        for tile in self:
            if tile.rect.colliderect(other.rect.x + other.velocity.x, other.rect.y, other.rect.width, other.rect.height):
                tile.collide(other, horizontal=True)
            if tile.rect.colliderect(other.rect.x, other.rect.y + other.velocity.y, other.rect.width, other.rect.height):
                new = tile.collide(other, horizontal=False)

                if new:
                    grounded = True
        
        return grounded
                

    def draw(self, surface: pygame.Surface):
        """Draw each tile in the terrain

        Args:
            surface (pygame.Surface): the surface to draw the terrain on
        """
        for tile in self:
            tile.draw(surface)