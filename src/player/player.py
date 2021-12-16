import pygame
from src.player.bullet import Bullet

from src.constants import game, player, Direction
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

        # Animation lists
        self.idle_frames = []
        self.walking_frames = []
        
        # Get idle frames
        for image in os.listdir(f"src/assets/player{player_id}/idle"):
            image = pygame.image.load(f"src/assets/player{player_id}/idle/{image}").convert_alpha()
            image = pygame.transform.scale(image, (image.get_width() * player.SCALE, image.get_height() * player.SCALE))

            self.idle_frames.append(image)
        
        # Get walking frames
        for image in os.listdir(f"src/assets/player{player_id}/walking"):
            image = pygame.image.load(f"src/assets/player{player_id}/walking/{image}").convert_alpha()
            image = pygame.transform.scale(image, (image.get_width() * player.SCALE, image.get_height() * player.SCALE))

            self.walking_frames.append(image)

        # Get falling frame
        self.falling = pygame.image.load(f"src/assets/player{player_id}/falling.png").convert_alpha()
        self.falling = pygame.transform.scale(self.falling, (self.falling.get_width() * player.SCALE, self.falling.get_height() * player.SCALE))

        # Get jumping frame
        self.jumping = pygame.image.load(f"src/assets/player{player_id}/jumping.png").convert_alpha()
        self.jumping = pygame.transform.scale(self.jumping, (self.jumping.get_width() * player.SCALE, self.jumping.get_height() * player.SCALE))

        # Get hurt frame
        self.hurt = pygame.image.load(f"src/assets/player{player_id}/hurt.png").convert_alpha()
        self.hurt = pygame.transform.scale(self.hurt, (self.hurt.get_width() * player.SCALE, self.hurt.get_height() * player.SCALE))

        self.hurt_time = 0

        # Animation variables
        self.animation_speed = random.uniform(player.ANIMATION_SPEED_MIN, player.ANIMATION_SPEED_MAX)
        self.update_time = 0
        self.frame = 0
        
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
        self.ground_timer = 0

        self.jump_time_counter = 0
        self.is_jumping = False
        
        # Knockback direction
        self.knockback_dir = 0

        # Create the weapon
        self.weapon = Weapon(pos, terrain)

        # Create the healthbar
        self.healthbar = HealthBar(self.rect)
        self.health = player.MAX_HEALTH



    def hit(self, damage: int, direction: int):
        """Hit the player for damage

        Args:
            damage (int): the amount of damage to deal
        """
        self.health -= damage
        
        # Set the hurt time
        self.hurt_time = player.HURT_TIME

        self.knockback_dir = direction

    def handle_movement(self, dt: float, inputs: list):
        """Handle the movement of the player

        Args:
            dt (float): the time since the last update
            inputs (list): the inputs of the player
        """
        # Set variables
        jump_input = Direction.UP in inputs
        left_input = Direction.LEFT in inputs
        right_input = Direction.RIGHT in inputs

        # Move left
        if left_input:
            self.velocity.x -= player.ACCELERATION * dt
            self.facing_right = False

            self.state = "walking"
        # Move right
        elif right_input:
            self.velocity.x += player.ACCELERATION * dt
            self.facing_right = True

            self.state = "walking"

        # Jump
        if jump_input and self.ground_timer > 0:
            self.is_jumping = True
            self.jump_time_counter = player.JUMP_TIME
            self.velocity.y = player.JUMP_HEIGHT * dt

        if jump_input and self.is_jumping:
            if self.jump_time_counter > 0:
                self.velocity.y = player.JUMP_HEIGHT * dt
                self.jump_time_counter -= dt
            else:
                self.is_jumping = False
        
        if not jump_input:
            self.is_jumping = False

        # If no movement, decelerate
        if not left_input and not right_input:
            self.velocity.x -= self.velocity.x * player.FRICTION * dt

            if abs(self.velocity.x) < 1:
                self.velocity.x = 0
                
            self.state = "idle"
        
        # Limit the speed
        self.velocity.x = min(self.velocity.x, player.MAX_SPEED)
        self.velocity.x = max(self.velocity.x, -player.MAX_SPEED)

        # Check if the player is on the ground
        if self.velocity.y >= 1:
            self.state = "falling"
        elif self.velocity.y < 0:
            self.state = "jumping"
        
        self.ground_timer -= dt

    def handle_collisions(self):
        """Handle the collisions of the player
        """
        # Get all collisions
        collisions = self.terrain.collide(self)

        # Check if grounded
        grounded = False

        for (tile, direction) in collisions:
            if direction == Direction.UP:
                self.velocity.y = tile.rect.bottom - self.rect.top
            if direction == Direction.DOWN:
                self.velocity.y = tile.rect.top - self.rect.bottom
                grounded = True

            if direction == Direction.LEFT:
                self.velocity.x = tile.rect.right - self.rect.left
            if direction == Direction.RIGHT:
                self.velocity.x = tile.rect.left - self.rect.right
        
        if grounded:
            self.ground_timer = player.HANG_TIME

    def update_animation(self, dt: float):
        """Update the animation of the player

        Args:
            dt (float): the time since the last update
        """
        # Update the animation
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
        
        # Set the image
        if self.state == "falling":
            self.image = self.falling
        elif self.state == "jumping":
            self.image = self.jumping
        
        if self.hurt_time > 0:
            self.image = self.hurt
            self.hurt_time -= dt

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

        # Apply knockback
        if self.knockback_dir != 0:
            self.velocity.x = self.knockback_dir * player.HORIZONTAL_KNOCKBACK * dt
            self.velocity.y = player.VERTICAL_KNOCKBACK * dt
            self.knockback_dir = 0

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
        weapon_x = self.rect.centerx + (direction * self.image.get_width() * 0.5)

        self.weapon.update(
            (weapon_x, self.rect.centery),
            direction
        )

        # Update the healthbar
        self.healthbar.update(self.rect.center)
        self.update_animation(dt)

        # Do damage if out of bounds
        if self.rect.x < 0 or self.rect.right > game.WIDTH:
            self.health -= 1
        if self.rect.y < 0 or self.rect.bottom > game.HEIGHT:
            self.health  -= 1

        # Check if the player is dead
        if self.health <= 0:
            print(f"Player {self.player_id} died!")
            print(f"Player {1 if self.player_id == 2 else 2} won!")
            pygame.event.post(pygame.event.Event(pygame.QUIT))

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




