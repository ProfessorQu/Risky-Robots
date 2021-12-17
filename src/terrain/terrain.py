import pygame

from src.constants import Direction


class Terrain(list):
    def __init__(self, *args):
        """Initialize the terrain object
        """
        list.__init__(self, args)

    def draw(self, surface: pygame.Surface):
        """Draw each tile in the terrain

        Args:
            surface (pygame.Surface): the surface to draw the terrain on
        """
        for tile in self:
            tile.draw(surface)

    def collide(self, other: pygame.sprite.Sprite, mode: str="Predict") -> dict:
        """Check if the sprite collides with any of the tiles in the terrain

        Args:
            other (pygame.sprite.Sprite): the sprite to check for collisions
            mode (str, optional): the mode to use for checking collisions. Defaults to "Predict".

        Returns:
            dict: a dictionary containing the collision information
        """
        collisions = []
        for tile in self:
            # Check for collisions with the current x and y
            if mode == "Current":
                if tile.rect.colliderect(other.rect.x, other.rect.y, other.rect.width, other.rect.height):
                    if other.velocity.y < 0:
                        collisions.append((tile, Direction.UP))
                    if other.velocity.y > 1:
                        collisions.append((tile, Direction.DOWN))

                    if other.velocity.x < 0:
                        collisions.append((tile, Direction.LEFT))
                    if other.velocity.x > 0:
                        collisions.append((tile, Direction.RIGHT))

            # Check for collisions with the predicted x and y
            elif mode == "Predict":
                if tile.rect.colliderect(other.rect.x, other.rect.y + other.velocity.y, other.rect.width, other.rect.height):
                    if other.velocity.y < 0:
                        collisions.append((tile, Direction.UP))
                    if other.velocity.y > 1:
                        collisions.append((tile, Direction.DOWN))

                if tile.rect.colliderect(other.rect.x + other.velocity.x, other.rect.y, other.rect.width, other.rect.height):
                    if other.velocity.x < 0:
                        collisions.append((tile, Direction.LEFT))
                    if other.velocity.x > 0:
                        collisions.append((tile, Direction.RIGHT))
                        
        return collisions
