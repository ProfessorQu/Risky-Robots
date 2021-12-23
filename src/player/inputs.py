import pygame

from src.constants import Direction


class Inputs:
    def __init__(
        self, is_controller: bool, controller_id: int,
        left: int, right: int, jump: int, shoot: int
        ):
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

        self.is_controller = is_controller
        self.controller_id = controller_id

    def get_inputs(self):
        """Get the inputs from the keyboard
        
        Returns:
            List: a list of the pressed keys
        """
        inputs = []

        if self.is_controller:
            joystick = pygame.joystick.Joystick(self.controller_id)
            joystick.init()

            inputs.append(joystick.get_axis(0) < -0.5)
            inputs.append(joystick.get_axis(0) > 0.5)
            inputs.append(joystick.get_button(self.jump))
            inputs.append(joystick.get_button(self.shoot))
        else:
            keys = pygame.key.get_pressed()
            inputs.append(keys[self.left])
            inputs.append(keys[self.right])
            inputs.append(keys[self.jump])
            inputs.append(keys[self.shoot])

        return inputs

    def draw(self, surface: pygame.Surface, x: int):
        if self.is_controller:
            color = (255, 0, 0)
        elif self.jump == pygame.K_w:
            color = (0, 255, 0)
        elif self.jump == pygame.K_UP:
            color = (0, 0, 255)
        else:
            color = (0, 0, 0)

        pygame.draw.rect(surface, color, (x * 50, 550, 50, 50))

