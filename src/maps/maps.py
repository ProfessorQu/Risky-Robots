import pygame

from src.terrain import Terrain, Solid, Spring, Mirror
from src.constants import Direction, game
from src.maps.map import Map
from src.terrain.mode import ScaleMode

# Map 1
MAP1 = Map(
    Terrain(
        Solid((0, game.HEIGHT - 50, game.WIDTH, 50)), # Floor
        Solid((0, 0, game.WIDTH, 50)), # Ceiling

        Solid((0, 0, 50, game.HEIGHT)), # Left wall
        Solid((game.WIDTH - 50, 0, 50, game.HEIGHT)), # Right wall

        Solid((200, 400, 150, 50)), # Left platform
        Solid((0, 250, 200, 50)), # High left platform
        Solid((game.WIDTH - 350, 400, 150, 50)), # Right platform
        Solid((game.WIDTH - 200, 250, 200, 50)), # High right platform

        Solid((350, 250, 100, game.HEIGHT - 400)), # Pillar
    ),
    pygame.Rect(-100, -100, game.WIDTH + 100, game.HEIGHT + 100),
    ((100, 500), (700, 500))
)

# Map 2
MAP2 = Map(
    Terrain(
        Solid((0, game.HEIGHT - 50, game.WIDTH, 50)), # Floor
        Solid((0, 0, game.WIDTH, 50)), # Ceiling

        Solid((0, 0, 50, 600)), # Left wall
        Solid((game.WIDTH - 50, 0, 50, game.HEIGHT)), # Right wall

        # The bottom of the pillar
        Spring((350, 350, 50, 50), Direction.LEFT, ScaleMode.Tile), # Left of this spring pillar
        Spring((400, 350, 50, 50), Direction.RIGHT, ScaleMode.Tile), # Right of this spring pillar
        Spring((350, 330, 100, 50), Direction.UP, ScaleMode.Tile), # Top of this spring pillar
        Solid((375, 350, 50, 50)), # Middle of this pillar

        Spring((350, 500, 50, 50), Direction.LEFT, ScaleMode.Tile), # Left of this spring pillar
        Spring((400, 500, 50, 50), Direction.RIGHT, ScaleMode.Tile), # Right of this spring pillar
        Solid((375, 500, 50, 50)), # Middle of this pillar

        # The top of the pillar
        Spring((350, 50, 50, 100), Direction.LEFT, ScaleMode.Tile), # Left of this spring pillar
        Spring((400, 50, 50, 100), Direction.RIGHT, ScaleMode.Tile), # Right of this spring pillar
        Spring((350, 120, 100, 50), Direction.DOWN, ScaleMode.Tile), # Bottom of this spring pillar
        Solid((375, 50, 50, 100)), # Middle of this pillar

        Solid((50, 300, 150, 50)), # Left platform
        Solid((600, 300, 150, 50)), # Right platform

        Spring((250, 500, 100, 50), Direction.UP), # Left spring
        Spring((450, 500, 100, 50), Direction.UP), # Right spring
    ),
    pygame.Rect(-100, -100, game.WIDTH + 100, game.HEIGHT + 100),
    ((100, 150), (700, 150))
)

# Map 3
MAP3 = Map(
    Terrain(
        Mirror((0, game.HEIGHT - 50, game.WIDTH, 50)), # Floor
        Mirror((0, 0, game.WIDTH, 50)), # Ceiling

        Mirror((0, 0, 50, game.HEIGHT)), # Left wall
        Mirror((game.WIDTH - 50, 0, 50, game.HEIGHT)), # Right wall

        Mirror((200, 400, 150, 50)), # Left platform
        Mirror((0, 250, 200, 50)), # High left platform
        Mirror((game.WIDTH - 350, 400, 150, 50)), # Right platform
        Mirror((game.WIDTH - 200, 250, 200, 50)), # High right platform

        Mirror((350, 250, 100, game.HEIGHT - 400)), # Pillar
    ),
    pygame.Rect(-100, -100, game.WIDTH + 100, game.HEIGHT + 100),
    ((200, 350), (700, 350))
)