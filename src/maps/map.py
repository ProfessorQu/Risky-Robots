import pygame

from src.terrain import Terrain, Solid, Spring, Mirror
from src.constants import Direction

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Map:
    """A map of the game.
    """
    terrain: Terrain
    bounds: pygame.Rect
    players_pos: list


def get_map_from_file(filename: str) -> Map:
    """Get a map from a file.

    Args:
        filename (str): the filename of the map

    Returns:
        Map: the map
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

        terrain = Terrain()
        bounds = pygame.Rect(0, 0, 0, 0)
        players_pos = []

        mode = "none"

        for line in lines:
            line = line.lower().strip()
            mode, skip = get_mode(mode, line)
            if skip:
                continue

            if mode == "terrain" and "terrain" not in line:
                add_terrain(line, terrain)
            elif mode == "bounds" and "bounds" not in line:
                bounds = pygame.Rect(tuple(map(int, line.split(","))))
            elif mode == "players" and "players" not in line:
                players_pos.append(tuple(map(int, line.split(","))))

        return Map(terrain, bounds, players_pos)

def get_mode(mode: str, line: str) -> Tuple[str, bool]:
    """Get the mode of the map.

    Args:
        mode (str): the current mode
        line (str): the line to check

    Returns:
        str, bool: the new mode, if the mode has changed
    """
    if line == "" or line[0] == "#":
        return mode, True
    elif line.startswith("terrain"):
        return "terrain", False
    elif line.startswith("bounds"):
        return "bounds", False
    elif line.startswith("players"):
        return "players", False
    else:
        return mode, False

def add_terrain(line, terrain):
    """Add a tile to the terrain.

    Args:
        line (str): the line to parse
        terrain (Terrain): the terrain to add to
    """
    if line.startswith("solid"):
        rect = pygame.Rect(tuple(map(int, line[6:].split(","))))
        terrain.append(Solid(rect))
    elif line.startswith("mirror"):
        rect = pygame.Rect(tuple(map(int, line[7:].split(","))))
        terrain.append(Mirror(rect))
    elif line.startswith("spring"):
        vars = line[6:].split(",")
        rect = pygame.Rect(tuple(map(int, vars[:4])))
        vars[4] = vars[4].strip()
        direction = direction_from_string(vars[4])
        terrain.append(Spring(rect, direction))

def direction_from_string(direction: str) -> Direction:
    """Get a direction from a string.
    """
    if direction == "up":
        return Direction.UP
    elif direction == "right":
        return Direction.RIGHT
    elif direction == "down":
        return Direction.DOWN
    elif direction == "left":
        return Direction.LEFT
    else:
        return Direction.NONE