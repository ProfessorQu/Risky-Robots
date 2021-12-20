import pygame

from dataclasses import dataclass
from typing import Callable, Tuple

@dataclass
class BulletData:
    image: pygame.Surface
    size: Tuple[int, int]
    speed: int
    damage: int
    knockback: int
    hit: Callable