import pygame

from src.constants.particle import *
from src.terrain import Terrain, CollideMode
from src.constants import Direction


class Particle(pygame.sprite.Sprite):
    def __init__(
            self, pos: pygame.Vector2, velocity: pygame.Vector2,
            radius: int, color: pygame.Color, lifetime: int
        ):
        super().__init__()
        
        self.pos = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(velocity)

        self.radius = radius
        self.color = color

        self.rect = pygame.Rect((0, 0), (radius * 2, radius * 2))

        self.lifetime = lifetime
    
    def update(self):
        self.pos += self.velocity
        self.lifetime -= 1

        if self.lifetime <= 0:
            self.kill()
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)