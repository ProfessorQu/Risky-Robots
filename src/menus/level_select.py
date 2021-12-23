import pygame
from pygame.locals import *

from src.constants.game import *
from src.menu.button import Button
from src.player.inputs import Inputs
import src.menus.game as game
from src.maps import MAP1, MAP2, MAP3

from typing import List


def level_select(SCREEN: pygame.Surface, CLOCK: pygame.time.Clock, inputs: List[Inputs]):
    # Initialize the game
    pygame.init()
    pygame.display.set_caption("Game")

    # Create the screen and the clock
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    # Create the buttons
    buttons = []
    button_pos = [
        (200, 150),
        (600, 150),
        (200, 450),
        (600, 450),
    ]

    rect = pygame.Rect(0, 0, WIDTH / 3, HEIGHT / 3)
    for i in range(4):
        rect.center = button_pos[i]
        
        path = f"src/assets/menu/level_select/buttons/button{i + 1}.png"
        buttons.append(Button(i, path, rect, (200, 200, 200), (100, 100, 100), f"Map {i + 1}", 50, (255, 255, 255)))

    running = True

    # Main loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        # Tick
        CLOCK.tick(FPS)

        # Draw the screen
        SCREEN.fill((0, 128, 128))

        # Draw the buttons
        for button in buttons:
            button.draw(SCREEN)

            if button.pressed:
                if button.id == 0:
                    game.game(MAP1, SCREEN, CLOCK, inputs)
                elif button.id == 1:
                    game.game(MAP2, SCREEN, CLOCK, inputs)
                elif button.id == 2:
                    game.game(MAP3, SCREEN, CLOCK, inputs)

        # Update the screen
        pygame.display.update()

    print("Exiting...")
    pygame.quit()
