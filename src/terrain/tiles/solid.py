import pygame

from src.terrain.mode import ScaleMode
from src.terrain.tiles.tile import Tile


class Solid(Tile):
    def __init__(self, rect: pygame.Rect):
        """Initialize the solid object

        Args:
            x (int): the x position of the solid
            y (int): the y position of the solid
            width (int): the width of the solid
            height (int): the height of the solid
        """
        image = pygame.image.load("src/assets/terrain/solid.png")
        super().__init__(image, rect, ScaleMode.Tile)
