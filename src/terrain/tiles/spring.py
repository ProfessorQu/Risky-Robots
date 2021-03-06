import pygame

from src.terrain.mode import ScaleMode
from src.terrain.tiles.tile import Tile
from src.constants.direction import Direction


class Spring(Tile):
    def __init__(self, rect: pygame.Rect, direction: Direction, scale_mode: ScaleMode = ScaleMode.Stretch):
        """Initialize the solid object

        Args:
            x (int): the x position of the solid
            y (int): the y position of the solid
            width (int): the width of the solid
            height (int): the height of the solid
        """
        image = pygame.image.load("src/assets/terrain/spring.png")

        # Rotate the image according to the direction
        if direction == Direction.LEFT:
            image = pygame.transform.rotate(image, 90)
        elif direction == Direction.RIGHT:
            image = pygame.transform.rotate(image, -90)
        elif direction == Direction.DOWN:
            image = pygame.transform.rotate(image, 180)
            
        super().__init__(image, rect, scale_mode)
        self.direction = direction
