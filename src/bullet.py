import pygame

from src.constants import bullet, game
from src.terrain.terrain import Terrain

from typing import Tuple, List


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int, int], direction: int, terrain: Terrain):
        """Initialize the bullet

        Args:
            pos (Tuple[int, int]): the position of the bullet
            direction (int): the direction of the bullet
            terrain (Terrain): the terrain of the map
        """        """"""
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("src/assets/bullet.png").convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * bullet.SCALE,
                self.image.get_height() * bullet.SCALE,
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.dir = direction

        self.velocity = pygame.math.Vector2(direction * bullet.SPEED, 0)

        self.terrain = terrain

    def update(self, dt: float, players: List[pygame.sprite.Sprite]) -> bool:
        """Update the bullet's position

        Args:
            dt (float): the time since the last frame
            players (List[pygame.sprite.Sprite]): the list of players

        Returns:
            bool: True if the bullet is still alive, False otherwise
        """
        self.rect.x += self.velocity.x * dt

        for player in players:
            if self.rect.colliderect(player.rect):
                player.hit(bullet.DAMAGE, self.dir)

                return True
            

        if (self.rect.x < 0 or self.rect.x > game.WIDTH):
            return True
        if self.rect.y < 0 or self.rect.y > game.HEIGHT:
            return True
        if self.terrain.collide(self, "Current"):
            return True
        
        return False

    def draw(self, surface: pygame.Surface):
        """Draw the bullet

        Args:
            surface (pygame.Surface): the surface to draw the bullet on
        """
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        surface.blit(image, self.rect)
