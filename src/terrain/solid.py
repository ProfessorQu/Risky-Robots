import pygame

class Solid:
    def __init__(self, rect: pygame.Rect, color: pygame.Color):
        """Initialize the solid object

        Args:
            x (int): the x position of the solid
            y (int): the y position of the solid
            width (int): the width of the solid
            height (int): the height of the solid
        """
        self.rect = pygame.Rect(rect)
        self.color = color

    def draw(self, surface: pygame.Surface):
        """Draw the solid object

        Args:
            surface (pygame.Surface): the surface to draw the solid on
        """        """"""
        pygame.draw.rect(surface, self.color, self.rect)