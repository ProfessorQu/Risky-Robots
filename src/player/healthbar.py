import pygame

from src.constants import healthbar, player

from typing import Tuple


class HealthBar:
    def __init__(self, player_pos: Tuple[int, int]):
        """Initialize the health bar

        Args:
            player_rect (pygame.Rect): the player's rectangle
        """
        # Copy the player's rectangle
        self.rect = pygame.Rect(
            player_pos[0], player_pos[1],
            healthbar.WIDTH, healthbar.HEIGHT
        )

        # Set the health bar's position
        self.update(player_pos)

    def update(self, player_pos: Tuple[int, int]):
        """Update the health bar's position

        Args:
            player_pos (Tuple[int, int]): the player's position
        """
        self.rect.x = player_pos[0] - healthbar.WIDTH // 2
        self.rect.y = player_pos[1] - healthbar.HEIGHT - healthbar.HOVER
    
    def draw(self, surface: pygame.Surface, health: int):
        """Draw the health bar

        Args:
            surface (pygame.Surface): the surface to draw the health bar on
            health (int): the player's health
        """
        # Set the color of the health bar
        percent = health / player.MAX_HEALTH
        if percent > 0.5:
            color = (0, 255, 0)
        elif percent > 0.25:
            color = (255, 255, 0)
        else:
            color = (255, 0, 0)

        # Update the health bar
        rect = self.rect.copy()
        rect.width = rect.width * percent

        # Draw the health bar
        pygame.draw.rect(surface, color, rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)