from enum import Enum


WIDTH = 800
HEIGHT = 600
FPS = 60

GRAVITY = 15
GRAVITY_FALL = 20

FLOOR_HEIGHT = 10
FLOOR = HEIGHT - FLOOR_HEIGHT


class WeaponVars:
    FIRE_RATE = 20
    SCALE = 0.05


class BulletVars:
    SPEED = 300
    SCALE = 0.02


class PlayerVars:
    SPEED = 200
    JUMP_HEIGHT = -450
    MAX_JUMPS = 2
    SCALE = 0.02


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
