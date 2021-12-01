from enum import Enum


WIDTH = 800
HEIGHT = 600
FPS = 60

GRAVITY = 10
FLOOR = HEIGHT - 10


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
