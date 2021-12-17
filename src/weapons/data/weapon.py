import pygame

from dataclasses import dataclass

@dataclass
class WeaponData:
    image: pygame.Surface
    rect: pygame.Rect
    cooldown: int