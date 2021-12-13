import pygame
from src.constants import Direction


class Inputs:
    def __init__(self, left: int, right: int, jump: int, shoot: int):
        self.left = left
        self.right = right
        self.jump = jump
        self.shoot = shoot

    def get_inputs(self):
        inputs = []

        keys = pygame.key.get_pressed()

        if keys[self.left]:
            inputs.append(Direction.LEFT)
        if keys[self.right]:
            inputs.append(Direction.RIGHT)
        if keys[self.jump]:
            inputs.append(Direction.UP)
        if keys[self.shoot]:
            inputs.append(Direction.DOWN)

        return inputs
