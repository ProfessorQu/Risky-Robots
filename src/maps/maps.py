import pygame

from src.terrain import Terrain, Solid, Spring
from src.constants import Direction
from src.maps.map import Map
from src.game import *

# Map 1
MAP1 = Map(
    Terrain(
        Solid((50, 250, 200, 40)), # Left platform
        Solid((260, 400, 280, 40)), # Middle platform
        Solid((550, 250, 200, 40)), # Right platform

        Solid((0, 560, WIDTH, 40)), # Floor
    ),
    pygame.Rect(-100, -100, WIDTH + 100, HEIGHT + 100),
    ((100, 500), (700, 500))
)

# Map 2
MAP2 = Map(
    Terrain(
        Solid((-150, 200, 400, 40)), # Left platform
        Solid((550, 200, 400, 40)), # Right platform

        Spring((260, 400, 280, 100), Direction.UP), # Spring in the middle
        Solid((260, 500, 280, 40))
    ),
    pygame.Rect(-100, -100, WIDTH + 100, HEIGHT + 100),
    ((100, 150), (700, 150))
)

# Map 3
MAP3 = Map(
    Terrain(
        Solid((0, 560, WIDTH, 40)), # Floor

        Solid((0, 400, 200, 200)), # Left column
        Solid((600, 400, 200, 200)), # Right column
    ),
    pygame.Rect(-100, -100, WIDTH + 100, HEIGHT + 100),
    ((200, 350), (700, 350))
)