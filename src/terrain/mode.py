from enum import Enum

class CollideMode(Enum):
    """The mode to check collisions with
    """
    Predict = 0
    Current = 1

class ScaleMode(Enum):
    """The mode to scale the tile
    """
    Tile = 0
    Stretch = 1