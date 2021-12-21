import pygame

from dataclasses import dataclass
from typing import Callable, Tuple

@dataclass
class BulletData:
    """Data class for a bullet
    """
    image: pygame.Surface
    size: Tuple[int, int]
    speed: int
    damage: int
    knockback: int
    lifetime: int
    hit: Callable