import pygame

from src.constants import Direction

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

    def handle_collision(self, player: pygame.Rect, direction: Direction):
        return True

    def draw(self, surface: pygame.Surface):
        """Draw the solid object

        Args:
            surface (pygame.Surface): the surface to draw the solid on
        """
        for tile in self.tiles:
            image = pygame.transform.scale(self.image, (tile.width, tile.height))
            surface.blit(image, tile)