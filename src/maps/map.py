import pygame

from src.terrain import Terrain

from dataclasses import dataclass

@dataclass
class Map:
    """A map of the game.
    """
    terrain: Terrain
    players_pos: list

