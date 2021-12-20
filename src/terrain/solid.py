import pygame

from src.constants import Direction
from src.terrain import CollideMode


class Solid:
    def __init__(self, rect: pygame.Rect):
        """Initialize the solid object

        Args:
            x (int): the x position of the solid
            y (int): the y position of the solid
            width (int): the width of the solid
            height (int): the height of the solid
        """
        self.image = pygame.image.load("src/assets/terrain/solid.png")

        self.rect = pygame.Rect(rect)
        scale = min(self.rect.width, self.rect.height)

        self.tiles = []
        for x in range(self.rect.x, self.rect.x + self.rect.width, scale):
            for y in range(self.rect.y, self.rect.y + self.rect.height, scale):
                if x + scale > self.rect.x + self.rect.width or y + scale > self.rect.y + self.rect.height:
                    rect = pygame.Rect(x, y, (self.rect.x + self.rect.width) - x, (self.rect.y + self.rect.height) - y)
                else:
                    rect = pygame.Rect((x, y), (scale, scale))
                
                self.tiles.append(rect)
    
    def convert(self):
        self.image = self.image.convert_alpha()

    def collide(self, other: pygame.sprite.Sprite, mode: CollideMode):
        if mode == CollideMode.Predict:
            if self.rect.colliderect(other.rect.x + other.velocity.x, other.rect.y, other.rect.width, other.rect.height):
                return True, Direction.RIGHT if other.velocity.x > 0 else Direction.LEFT
            if self.rect.colliderect(other.rect.x, other.rect.y + other.velocity.y, other.rect.width, other.rect.height):
                return True, Direction.DOWN if other.velocity.y > 0 else Direction.UP
            
            return False, Direction.NONE
        elif mode == CollideMode.Current:
            if self.rect.colliderect(other.rect):
                return True, Direction.NONE
            return False, Direction.NONE

    def draw(self, surface: pygame.Surface):
        """Draw the solid object

        Args:
            surface (pygame.Surface): the surface to draw the solid on
        """
        for tile in self.tiles:
            image = pygame.transform.scale(self.image, (tile.width, tile.height))
            surface.blit(image, tile)