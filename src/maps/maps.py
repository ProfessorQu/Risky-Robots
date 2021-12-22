import pygame

from src.terrain import Terrain, Solid, Spring
from src.constants import Direction, game
from src.maps.map import Map
from src.terrain.mode import ScaleMode

# Map 1
MAP1 = Map(
    Terrain(
        Solid((0, game.HEIGHT - 50, game.WIDTH, 50)),
        Solid((0, 0, 50, game.HEIGHT)),
        Solid((game.WIDTH - 50, 0, 50, game.HEIGHT)),
        Solid((0, 0, game.WIDTH, 50)),
    ),
    pygame.Rect(-100, -100, game.WIDTH + 100, game.HEIGHT + 100),
    ((100, 500), (700, 500))
)

# Map 2
MAP2 = Map(
    Terrain(
        Spring((50, game.HEIGHT - 50, game.WIDTH - 100, 50), Direction.UP, ScaleMode.Tile), # Floor
        Spring((50, 0, game.WIDTH - 100, 50), Direction.DOWN, ScaleMode.Tile), # Ceiling

        Spring((0, 50, 50, game.HEIGHT - 100), Direction.RIGHT, ScaleMode.Tile), # Left wall
        Spring((game.WIDTH - 50, 50, 50, game.HEIGHT - 100), Direction.LEFT, ScaleMode.Tile), # Right wall

        Solid((0, 0, 50, 50)), # Top left corner
        Solid((game.WIDTH - 50, 0, 50, 50)), # Top right corner
        Solid((0, game.HEIGHT - 50, 50, 50)), # Bottom left corner
        Solid((game.WIDTH - 50, game.HEIGHT - 50, 50, 50)), # Bottom right corner

        Solid((300, 300, 200, 50))
    ),
    pygame.Rect(-100, -100, game.WIDTH + 100, game.HEIGHT + 100),
    ((100, 150), (700, 150))
)

# Map 3
MAP3 = Map(
    Terrain(
        Solid((0, 560, game.WIDTH, 40)), # Floor

        Solid((0, 400, 200, 200)), # Left column
        Solid((600, 400, 200, 200)), # Right column
    ),
    pygame.Rect(-100, -100, game.WIDTH + 100, game.HEIGHT + 100),
    ((200, 350), (700, 350))
)