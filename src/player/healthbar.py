import pygame
from src.constants import *


class HealthBar:
    def __init__(self, player_rect):
        self.rect = player_rect.copy()
        self.rect.width = HealthBarVars.WIDTH
        self.rect.height = HealthBarVars.HEIGHT
        self.rect.y = player_rect.centery - HealthBarVars.HOVER
        self.rect.x = player_rect.centerx - self.rect.width / 2

    def update(self, player_rect):
        self.rect = player_rect.copy()
        self.rect.width = HealthBarVars.WIDTH
        self.rect.height = HealthBarVars.HEIGHT
        self.rect.y = player_rect.centery - HealthBarVars.HOVER
        self.rect.x = player_rect.centerx - self.rect.width / 2

    def draw(self, surface, health):
        percent = health / PlayerVars.MAX_HEALTH
        if percent > 0.5:
            color = (0, 255, 0)
        elif percent > 0.25:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)

        rect = self.rect.copy()
        rect.width = rect.width * percent

        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)