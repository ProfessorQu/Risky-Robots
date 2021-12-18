import pygame

from src.terrain import Terrain, Solid
from src.maps.map import Map
from src.game import *

# Map 1
MAP1 = Map(
    Terrain(
        Solid((50, 250, 200, 40), PLATFORM_COLOR), # Left platform
        Solid((275, 400, 250, 40), PLATFORM_COLOR), # Middle platform
        Solid((550, 250, 200, 40), PLATFORM_COLOR), # Right platform

        Solid((50, 580, WIDTH - 100, 20), WALL_COLOR), # Floor
    ),
    pygame.Rect(-100, -100, WIDTH + 100, HEIGHT + 100),
    ((100, 540), (700, 540))
)

# Map 2
MAP2 = Map(
    Terrain(
        Solid((-150, 200, 400, 40), PLATFORM_COLOR), # Left platform
        Solid((275, 400, 250, 40), PLATFORM_COLOR), # Middle platform
        Solid((550, 200, 400, 40), PLATFORM_COLOR), # Right platform
    ),
    pygame.Rect(-100, -100, WIDTH + 100, HEIGHT + 100),
    ((100, 35), (700, 35))
)

# Map 3
MAP3 = Map(
    Terrain(
        Solid((0, 580, WIDTH, 20), WALL_COLOR), # Floor

        Solid((0, 400, 200, 200), WALL_COLOR), # Left column
        Solid((600, 400, 200, 200), WALL_COLOR), # Right column
    ),
    pygame.Rect(-100, -100, WIDTH + 100, HEIGHT + 100),
    ((100, 100), (100, 100))
)