from enum import Enum


WIDTH = 800
HEIGHT = 600
FPS = 60

GRAVITY = 15
GRAVITY_FALL = 20

FLOOR_HEIGHT = 10
FLOOR = HEIGHT - FLOOR_HEIGHT


class WeaponVars:
    FIRE_RATE = 75
    SCALE = 4


class BulletVars:
    SPEED = 300
    SCALE = 1.5


class PlayerVars:
    SPEED = 200
    JUMP_HEIGHT = -450
    MAX_HEALTH = 100
    MAX_JUMPS = 2
    SCALE = 5

class HealthBarVars:
    WIDTH = 50
    HEIGHT = 10

    HOVER = 50

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
