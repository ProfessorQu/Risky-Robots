import pygame
from pygame.locals import *

from src.constants.game import *
from src.menu.button import Button
from src.player.inputs import Inputs
import src.menus.level_select as level_select


# Initialize sound mixer
pygame.mixer.pre_init(44100, -16, 2, 2048)

# Initialize the game
pygame.init()
pygame.display.set_caption("Game")

# Initialize joysticks
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

for joystick in joysticks:
    joystick.init()

# Create the screen and the clock
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# Create the buttons
buttons = []
button_pos = [
    (100, 400),
    (300, 400),
    (500, 400),
    (700, 400)
]

# Get buttons
button_names = [
    "Remove",
    "Add WASD",
    "Add Arrows",
    "Add Controller",
]

inputs = []

rect = pygame.Rect(0, 0, 175, 50)
path = 'src/assets/menus/player_select/buttons/button.png'

for i in range(4):
    rect.center = button_pos[i]
    name = button_names[i]

    buttons.append(Button(i, path, rect, (150, 150, 150), (100, 100, 100), name, 25, (255, 255, 255)))

rect = pygame.Rect(0, 0, 200, 150)
rect.center = (WIDTH / 2, HEIGHT / 3)

buttons.append(
    Button(4, path, rect, (150, 150, 150), (100, 100, 100), "Play", 75, (255, 255, 255))
)

click = False

wasd_added = False
arrows_added = False

controller_id = 0

running = True

# Main loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            click = True

    # Draw the screen
    SCREEN.fill((0, 128, 128))

    for button in buttons:
        # Draw the buttons
        button.draw(SCREEN)

        if button.pressed and click:
            # Remove button
            if inputs and button.id == 0:
                removed = inputs.pop()
                if removed.is_controller:
                    controller_id -= 1
                if removed.jump == pygame.K_w:
                    wasd_added = False
                if removed.jump == pygame.K_UP:
                    arrows_added = False

            # Set a limit of at most 4 inputs
            if len(inputs) < 4:
                # Add WASD
                if button.id == 1:
                    if not wasd_added:
                        inputs.append(
                            Inputs(False, 0, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
                        )
                        wasd_added = True
                # Add Arrows
                elif button.id == 2:
                    if not arrows_added:
                        inputs.append(
                            Inputs(False, 0, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
                        )
                        arrows_added = True
                # Add Controller
                elif button.id == 3 and controller_id < pygame.joystick.get_count():
                    inputs.append(
                        Inputs(True, controller_id, 0, 0, 0, 2)
                    )
                    controller_id += 1

            # Play button
            if len(inputs) >= 2 and button.id == 4:
                level_select.level_select(SCREEN, CLOCK, inputs)

    # Draw the inputs
    for x, input in enumerate(inputs):
        input.draw(SCREEN, x)

    click = False

    # Update the screen
    pygame.display.update()

print("Exiting...")
pygame.quit()