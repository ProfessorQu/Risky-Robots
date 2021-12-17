import pygame
from src.constants import Direction


class Inputs:
    def __init__(self, left: int, right: int, jump: int, shoot: int):
        """Initialize the inputs

        Args:
            left (int): the keycode to move left
            right (int): the keycode to move right
            jump (int): the keycode to jump
            shoot (int): the keycode to shoot
        """
        self.left = left
        self.right = right
        self.jump = jump
        self.shoot = shoot

    def get_inputs(self):
        """Get the inputs from the keyboard
        
        Returns:
            List: a list of the pressed keys
        """
        inputs = []

        # Get the inputs
        keys = pygame.key.get_pressed()

        # Add the inputs
        if keys[self.left]:
            inputs.append(Direction.LEFT)
        if keys[self.right]:
            inputs.append(Direction.RIGHT)
        if keys[self.jump]:
            inputs.append(Direction.UP)
        if keys[self.shoot]:
            inputs.append(Direction.DOWN)

        return inputs
