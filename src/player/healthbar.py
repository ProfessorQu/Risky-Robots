import pygame
from src.constants import *


class HealthBar:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

    def draw(self, surface, health):
        rect = self.rect
        rect.width = self.rect.width * health / PlayerVars.MAX_HEALTH
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 1, 1)