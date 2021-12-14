import pygame
from src.bullet import Bullet

from src.constants import player, Direction
from src.player.weapon import Weapon
from src.player.healthbar import HealthBar
from src.player.inputs import Inputs
from src.terrain.terrain import Terrain

from typing import Tuple
import os
import random

class Player(pygame.sprite.Sprite):
    def __init__(
        self, player_id: int,
        pos: Tuple[int, int], facing_right: bool,
        inputs: Inputs, terrain: Terrain
    ):
        """Initialize the player

        Args:
            player_id (int): the id of the player
            pos (Tuple[int, int]): the position of the player
            facing_right (bool): whether the player is facing right
            inputs (Inputs): the inputs of the player
            terrain (Terrain): the terrain of the map
        """
        pygame.sprite.Sprite.__init__(self)
        self.player_id = player_id

        self.idle_frames = []
        self.walking_frames = []
        
        # Get idle frames
        for image in os.listdir(f"src/assets/player{player_id}/idle"):
            image = pygame.image.load(f"src/assets/player{player_id}/idle/{image}")
            image = pygame.transform.scale(image, (image.get_width() * player.SCALE, image.get_height() * player.SCALE))

            self.idle_frames.append(image)
        
        # Get walking frames
        for image in os.listdir(f"src/assets/player{player_id}/walking"):
            image = pygame.image.load(f"src/assets/player{player_id}/walking/{image}")
            image = pygame.transform.scale(image, (image.get_width() * player.SCALE, image.get_height() * player.SCALE))

            self.walking_frames.append(image)

        # Get falling frame
        self.falling = pygame.image.load(f"src/assets/player{player_id}/falling.png")
        self.falling = pygame.transform.scale(self.falling, (self.falling.get_width() * player.SCALE, self.falling.get_height() * player.SCALE))

        # Get jumping frame
        self.jumping = pygame.image.load(f"src/assets/player{player_id}/jumping.png")
        self.jumping = pygame.transform.scale(self.jumping, (self.jumping.get_width() * player.SCALE, self.jumping.get_height() * player.SCALE))

        # Animation variables
        self.animation_speed = random.uniform(player.ANIMATION_SPEED_MIN, player.ANIMATION_SPEED_MAX)
        self.update_time = 0
        
        # Set the player's state to idle and the frame to 0
        self.state = "idle"
        self.image = self.idle_frames[0]

        # Set the rect of the player
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Inputs and terrain
        self.inputs = inputs
        self.terrain = terrain

        # Movement
        self.velocity = pygame.math.Vector2(0, 0)
        self.facing_right = facing_right
        self.jumps = 0

        # Create the weapon
        self.weapon = Weapon(pos, terrain)

        # Set a few variables for easier access
        self.speed = player.SPEED
        self.jump_height = player.JUMP_HEIGHT
        self.max_jumps = player.MAX_JUMPS
        self.health = player.MAX_HEALTH

        # Create the healthbar
        self.healthbar = HealthBar(self.rect)

        self.frame = 0

    def hit(self, damage: int):
        """Hit the player for damage

        Args:
            damage (int): the amount of damage to deal
        """
        self.health -= damage
        # Check if the player is dead
        if self.health <= 0:
            print(f"Player {self.player_id} died!")
            print(f"Player {1 if self.player_id == 2 else 2} won!")
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def handle_movement(self, dt: float, inputs: list):
        """Handle the movement of the player

        Args:
            dt (float): the time since the last update
            inputs (list): the inputs of the player
        """
        if Direction.LEFT in inputs:
            self.velocity.x = -self.speed * dt
            self.facing_right = False

            self.state = "walking"
        elif Direction.RIGHT in inputs:
            self.velocity.x = self.speed * dt
            self.facing_right = True

            self.state = "walking"

        jump_input = Direction.UP in inputs
        jumps_left = self.jumps > 0
        falling = self.velocity.y >= 0

        jump = jump_input and jumps_left and falling
        if jump:
            self.velocity.y = self.jump_height * dt
            self.jumps -= 1

        if Direction.LEFT not in inputs and Direction.RIGHT not in inputs:
            self.velocity.x = 0
            self.state = "idle"
        
        if self.velocity.y >= 1:
            self.state = "falling"
        elif self.velocity.y <= -1:
            self.state = "jumping"

    def handle_collisions(self):
        """Handle the collisions of the player and update the velocity"""
        collisions = self.terrain.collide(self)

        on_ground = False

        for (tile, direction) in collisions:
            if direction == Direction.UP:
                self.velocity.y = tile.rect.bottom - self.rect.top
            if direction == Direction.DOWN:
                self.velocity.y = tile.rect.top - self.rect.bottom
                self.jumps = self.max_jumps
                on_ground = True

            if direction == Direction.LEFT:
                self.velocity.x = tile.rect.right - self.rect.left
            if direction == Direction.RIGHT:
                self.velocity.x = tile.rect.left - self.rect.right

    def update_animation(self, dt: float):
        """Update the animation of the player

        Args:
            dt (float): the time since the last update
        """
        self.update_time += dt
        if self.update_time >= self.animation_speed:
            if self.state == "idle":
                self.frame = (self.frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.frame]
            elif self.state == "walking":
                self.frame = (self.frame + 1) % len(self.walking_frames)
                self.image = self.walking_frames[self.frame]

            self.update_time = 0
            self.animation_speed = random.uniform(player.ANIMATION_SPEED_MIN, player.ANIMATION_SPEED_MAX)
        
        if self.state == "falling":
            self.image = self.falling
        elif self.state == "jumping":
            self.image = self.jumping

    def update(self, dt: float) -> Bullet:
        """Update the player

        Args:
            dt (float): the time since the last update

        Returns:
            Bullet: the new bullet
        """
        # Get inputs
        inputs = self.inputs.get_inputs()
        
        # Handle inputs
        self.handle_movement(dt, inputs)
        new_bullet = self.weapon.shoot() if Direction.DOWN in inputs else None

        # Gravity
        gravity = player.GRAVITY * dt if self.velocity.y < 0 else player.GRAVITY_FALL * dt
        self.velocity.y += gravity

        # Handle collisions
        self.handle_collisions()

        # Move the player
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Update the weapon
        direction = 1 if self.facing_right else -1
        weapon_x = self.rect.centerx + ( direction * self.image.get_width() * 0.5)

        self.weapon.update(
            (weapon_x, self.rect.centery),
            direction
        )

        # Update the healthbar
        self.healthbar.update(self.rect.center)
        self.update_animation(dt)

        return new_bullet

    def draw(self, screen: pygame.Surface):
        """Draw the player, weapon and healthbar

        Args:
            screen (pygame.Surface): the screen to draw on
        """
        # Draw the player
        image = pygame.transform.flip(self.image, not self.facing_right, False)
        screen.blit(image, self.rect)

        # Draw the weapon
        self.weapon.draw(screen)

        # Draw the healthbar
        self.healthbar.draw(screen, self.health)




