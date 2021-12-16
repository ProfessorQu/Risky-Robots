from src.terrain import Terrain, Solid

WIDTH = 800
HEIGHT = 600

FPS = 60

WALL_COLOR = (0, 0, 0)
PLATFORM_COLOR = (0, 0, 0)

MAP1_TERRAIN = Terrain(
    Solid((0, 200, 250, 40), PLATFORM_COLOR), # Left platform
    Solid((275, 400, 250, 40), PLATFORM_COLOR), # Middle platform
    Solid((550, 200, 250, 40), PLATFORM_COLOR), # Right platform

    Solid((0, 0, WIDTH, 20), WALL_COLOR), # Ceiling
    Solid((0, 580, WIDTH, 20), WALL_COLOR), # Floor

    Solid((0, 0, 20, 600), WALL_COLOR), # Left wall
    Solid((780, 0, 20, 600), WALL_COLOR), # Right wall
)
MAP1_PLAYERS_POS = ((100, 540), (700, 540))

MAP2_TERRAIN = Terrain(
    Solid((0, 200, 250, 40), PLATFORM_COLOR), # Left platform
    Solid((275, 400, 250, 40), PLATFORM_COLOR), # Middle platform
    Solid((550, 200, 250, 40), PLATFORM_COLOR), # Right platform
)
MAP2_PLAYERS_POS = ((100, 35), (700, 35))

MAP3_TERRAIN = Terrain(
    Solid((0, 0, WIDTH, 20), WALL_COLOR), # Ceiling
    Solid((0, 580, WIDTH, 20), WALL_COLOR), # Floor

    Solid((0, 0, 20, 600), WALL_COLOR), # Left wall
    Solid((780, 0, 20, 600), WALL_COLOR), # Right wall

    Solid((0, 400, 200, 200), WALL_COLOR), # Left column
    Solid((600, 400, 200, 200), WALL_COLOR), # Right column
)
MAP3_PLAYERS_POS = ((100, 100), (100, 100))