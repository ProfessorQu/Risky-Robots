import pygame

from src.terrain import Terrain, Solid
from src.maps.map import Map
from src.game import *

MAP1 = Map(
    Terrain(
        Solid((0, 200, 250, 40), PLATFORM_COLOR), # Left platform
        Solid((275, 400, 250, 40), PLATFORM_COLOR), # Middle platform
        Solid((550, 200, 250, 40), PLATFORM_COLOR), # Right platform

        Solid((0, 0, WIDTH, 20), WALL_COLOR), # Ceiling
        Solid((0, 580, WIDTH, 20), WALL_COLOR), # Floor

        Solid((0, 0, 20, 600), WALL_COLOR), # Left wall
        Solid((780, 0, 20, 600), WALL_COLOR), # Right wall
    ),
    ((100, 540), (700, 540))
)

MAP2 = Map(
    Terrain(
        Solid((-150, 200, 400, 40), PLATFORM_COLOR), # Left platform
        Solid((275, 400, 250, 40), PLATFORM_COLOR), # Middle platform
        Solid((550, 200, 400, 40), PLATFORM_COLOR), # Right platform
    ),
    ((100, 35), (700, 35))
)

MAP3 = Map(
    Terrain(
        Solid((0, 0, WIDTH, 20), WALL_COLOR), # Ceiling
        Solid((0, 580, WIDTH, 20), WALL_COLOR), # Floor

        Solid((0, 0, 20, 600), WALL_COLOR), # Left wall
        Solid((780, 0, 20, 600), WALL_COLOR), # Right wall

        Solid((0, 400, 200, 200), WALL_COLOR), # Left column
        Solid((600, 400, 200, 200), WALL_COLOR), # Right column
    ),
    ((100, 100), (100, 100))
)