from os import umask
import pygame

from dataclasses import dataclass

@dataclass
class BulletData:
    image: pygame.Surface
    rect: pygame.Rect
    speed: int
    damage: int