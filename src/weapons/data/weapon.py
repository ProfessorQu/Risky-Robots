import pygame

from dataclasses import dataclass
from src.weapons.data import BulletData
from typing import Tuple

@dataclass
class WeaponData:
    image: pygame.Surface
    size: Tuple[int, int]
    cooldown: int
    bullet: BulletData