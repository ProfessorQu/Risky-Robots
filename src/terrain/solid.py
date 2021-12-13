import pygame

class Solid:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        self.color = (0, 0, 0)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)