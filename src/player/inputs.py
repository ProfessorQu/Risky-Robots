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

        if self.is_controller:
            self.image = pygame.image.load("src/assets/menus/player_select/inputs/controller.png")
        elif self.jump == pygame.K_w:
            self.image = pygame.image.load("src/assets/menus/player_select/inputs/wasd.png")
        elif self.jump == pygame.K_UP:
            self.image = pygame.image.load("src/assets/menus/player_select/inputs/arrows.png")
        
        self.image = pygame.transform.scale(self.image, (150, 150))

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
        """Draw the inputs

        Args:
            surface (pygame.Surface): the surface to draw on
            x (int): the x position to draw the inputs
        """
        surface.blit(self.image, (x * 160 + 10, 450))

