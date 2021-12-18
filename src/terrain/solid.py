import pygame

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
        
        self.image = pygame.transform.scale(self.image, (scale, scale))

        self.tiles = []
        for x in range(self.rect.x, self.rect.x + self.rect.width, scale):
            for y in range(self.rect.y, self.rect.y + self.rect.height, scale):
                if x + scale > self.rect.x + self.rect.width or y + scale > self.rect.y + self.rect.height:
                    rect = pygame.Rect(x, y, scale, scale)
                    rect.right = self.rect.right
                    rect.bottom = self.rect.bottom
                    rect.left = self.rect.x
                    rect.top = self.rect.y
                    self.tiles.append(rect)
                else:
                    self.tiles.append(pygame.Rect((x, y), (scale, scale)))

    def draw(self, surface: pygame.Surface):
        """Draw the solid object

        Args:
            surface (pygame.Surface): the surface to draw the solid on
        """
        for tile in self.tiles:
            image = pygame.transform.scale(self.image, (tile.width, tile.height))
            surface.blit(image, tile)