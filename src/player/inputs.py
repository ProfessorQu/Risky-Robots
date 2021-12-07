import pygame


class Inputs:
    def __init__(self, left, right, jump, shoot):
        self.left = left
        self.right = right
        self.jump = jump
        self.shoot = shoot

    def get_inputs(self):
        inputs = []

        keys = pygame.key.get_pressed()

        if keys[self.left]:
            inputs.append("left")
        if keys[self.right]:
            inputs.append("right")
        if keys[self.jump]:
            inputs.append("jump")
        if keys[self.shoot]:
            inputs.append("shoot")

        return inputs
