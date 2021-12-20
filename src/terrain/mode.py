from enum import Enum

class CollideMode(Enum):
    Predict = 0
    Current = 1

class ScaleMode(Enum):
    Tile = 0
    Stretch = 1