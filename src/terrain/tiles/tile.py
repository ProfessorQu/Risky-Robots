import pygame

from src.constants import Direction
from src.terrain.mode import CollideMode, ScaleMode

from typing import List, Tuple


class Tile:
    def __init__(self, image: pygame.Surface, rect: pygame.Rect, scale_mode: ScaleMode):
        """Initialize the solid object

        Args:
            x (int): the x position of the solid
            y (int): the y position of the solid
            width (int): the width of the solid
            height (int): the height of the solid
        """
        self.image = image

        self.rect = pygame.Rect(rect)
        scale = min(self.rect.width, self.rect.height)

        if scale_mode == ScaleMode.Tile:
            self.tiles = []
            for x in range(self.rect.x, self.rect.x + self.rect.width, scale):
                for y in range(self.rect.y, self.rect.y + self.rect.height, scale):
                    if x + scale > self.rect.x + self.rect.width or y + scale > self.rect.y + self.rect.height:
                        rect = pygame.Rect(x, y, (self.rect.x + self.rect.width) - x, (self.rect.y + self.rect.height) - y)
                    else:
                        rect = pygame.Rect((x, y), (scale, scale))
                    
                    self.tiles.append(rect)
        elif scale_mode == ScaleMode.Stretch:
            self.tiles = [self.rect]
    
    def convert(self):
        """Convert the tile's image
        """
        self.image = self.image.convert_alpha()

    def collide(self, other: pygame.sprite.Sprite, mode: CollideMode) -> Tuple[bool, List[Direction]]:
        """Check if the other sprite collides with this tile

        Args:
            other (pygame.sprite.Sprite): the other sprite
            mode (CollideMode): the mode to check collisions with

        Returns:
            Tuple[bool, Direction]: a tuple containing if the other sprite collided and the direction of the collision
        """
        if type(other) == pygame.Rect:
            rect = other
            velocity = pygame.Vector2(0, 0)
        else:
            rect = other.rect
            velocity = other.velocity

        if mode == CollideMode.Predict:
            if self.rect.colliderect(rect.x + velocity.x, rect.y, rect.width, rect.height):
                return True, Direction.RIGHT if velocity.x > 0 else Direction.LEFT
            if self.rect.colliderect(rect.x, rect.y + velocity.y, rect.width, rect.height):
                return True, Direction.DOWN if velocity.y > 0 else Direction.UP
            
            return False, Direction.NONE
        elif mode == CollideMode.Current:
            if self.rect.colliderect(rect):
                directions = []
                if velocity.x > 0:
                    directions.append(Direction.RIGHT)
                if velocity.x < 0:
                    directions.append(Direction.LEFT)
                if velocity.y > 0 and rect.bottom - rect.height / 2 < self.rect.top:
                    directions.append(Direction.DOWN)
                if velocity.y < 0 and rect.top + rect.height / 2 > self.rect.bottom:
                    directions.append(Direction.UP)
                
                return True, directions
                    
            return False, Direction.NONE

    def draw(self, surface: pygame.Surface):
        """Draw the solid object

        Args:
            surface (pygame.Surface): the surface to draw the solid on
        """
        for tile in self.tiles:
            image = pygame.transform.scale(self.image, (tile.width, tile.height))
            surface.blit(image, tile)