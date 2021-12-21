import pygame

from src.terrain.mode import CollideMode
from src.constants import Direction
from src.terrain.tiles.tile import Tile

from typing import List, Tuple


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

    def collide(self, other: pygame.sprite.Sprite, mode: CollideMode) -> List[Tuple[Direction, Tile]]:
        """Get all the tiles that collide with the other sprite

        Args:
            other (pygame.sprite.Sprite): the other sprite
            mode (CollideMode): the mode to check collisions with

        Returns:
            List[Tuple[Direction, Tile]]: a list of tuples containing the direction and tile that collided
        """
        collisions = []
        for tile in self:
            collision, direction = tile.collide(other, mode)
            if collision:
                collisions.append((direction, tile))

        return collisions
                

    def draw(self, surface: pygame.Surface):
        """Draw each tile in the terrain

        Args:
            surface (pygame.Surface): the surface to draw the terrain on
        """
        for tile in self:
            tile.draw(surface)