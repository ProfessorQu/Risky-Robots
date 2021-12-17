import pygame

from src.terrain import Terrain

from dataclasses import dataclass

@dataclass
class Map:
    terrain: Terrain
    players_pos: list

