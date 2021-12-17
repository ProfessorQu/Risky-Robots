import pygame

from dataclasses import dataclass
from typing import Tuple

@dataclass
class BulletData:
    image: pygame.Surface
    size: Tuple[int, int]
    speed: int
    damage: int