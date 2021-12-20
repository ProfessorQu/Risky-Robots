import pygame

from src.weapons.data.bullet import BulletData

from typing import Tuple, Callable
from dataclasses import dataclass


@dataclass
class WeaponData:
    image: pygame.Surface
    size: Tuple[int, int]
    cooldown: int
    bullet: BulletData
    shoot: Callable