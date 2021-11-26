import pygame


class Object:
    def __init__(self, rect: pygame.Rect, color, isStatic=False):
        self.rect = rect
        self.color = color

        self.static = isStatic
        self.gravity = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        if (not self.static):
            self.rect.y += self.gravity
