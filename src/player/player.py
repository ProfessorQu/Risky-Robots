import pygame

from src.constants import player, Direction
from src.player.weapon import Weapon
from src.weapons.data.weapon_pickup import WeaponPickUp
from src.terrain import CollideMode
from src.player.healthbar import HealthBar
from src.player.inputs import Inputs
from src.terrain import Terrain, Solid, Spring, Mirror
from src.player.bullet import Bullet
from src.weapons import revolver

from typing import List, Tuple
import os
import random


class Player(pygame.sprite.Sprite):
    def __init__(
        self, player_id: int,
        pos: Tuple[int, int], facing_right: bool,
        inputs: Inputs,
        bounds: pygame.Rect, terrain: Terrain
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

        self.hurt_image_time = 0

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

        # Load jump sound
        self.jump_sound = pygame.mixer.Sound("src/assets/sounds/jump.wav")
        self.jump_sound.set_volume(0.2)
        
        self.jump_sound_time = 0

        # Load hurt sound
        self.hurt_sound = pygame.mixer.Sound("src/assets/sounds/hurt.wav")
        self.hurt_sound.set_volume(0.1)

        # Load pickup sound
        self.pickup_sound = pygame.mixer.Sound("src/assets/sounds/pickup.wav")
        self.pickup_sound.set_volume(0.2)

        # Load landing sound
        self.landing_sound = pygame.mixer.Sound("src/assets/sounds/landing.wav")
        self.landing_sound.set_volume(0.2)

        # Load spring sound
        self.spring_sound = pygame.mixer.Sound("src/assets/sounds/spring.wav")
        self.spring_sound.set_volume(0.2)

        # Terrain and bounds
        self.terrain = terrain
        self.bounds = bounds

        # Movement
        self.velocity = pygame.math.Vector2(0, 0)
        self.facing_right = facing_right
        self.grounded_timer = 0

        # Jumping
        self.jump_time_counter = 0
        self.is_jumping = False

        # Inputs
        self.inputs = inputs

        # Knockback direction
        self.knockback_force = pygame.math.Vector2(0, 0)

        # Create the weapon
        self.weapon = Weapon(revolver.WEAPON, pos, bounds, terrain)

        # Create the healthbar
        self.healthbar = HealthBar(self.rect)
        self.health = player.MAX_HEALTH


    def hit(self, damage: int, knockback_force: pygame.math.Vector2):
        """Hit the player for damage

        Args:
            damage (int): the amount of damage to deal
        """
        self.health -= damage
        
        # Set the hurt time
        self.hurt_image_time = player.HURT_TIME
        
        # Copy knockback force
        self.knockback_force = knockback_force

        # Play hurt sound
        self.hurt_sound.play()


    def update_inputs(self, weapon_pickups: List[WeaponPickUp], dt: float) -> Bullet:
        """Update the inputs of the player

        Args:
            dt (float): the time since the last frame

        Returns:
            Bullet: the bullet that was shot
        """
        # Get inputs
        inputs = self.inputs.get_inputs()

        # Horizontal movement
        self.horizontal_move(dt, inputs)

        # Jump
        self.jump(dt, inputs)

        # Limit the velocity
        self.limit_speed()

        # Bound the player
        self.out_of_bounds()

        # Check if the player picked up a weapon
        self.check_pickup(inputs, weapon_pickups)

        # Check if the player shot a bullet
        return self.check_shot(inputs)


    def horizontal_move(self, dt: float, inputs: List[bool]):
        """Move the player horizontally

        Args:
            dt (float): the time since the last frame
            inputs (List): the inputs of the player
        """
        left_input = inputs[0]
        right_input = inputs[1]
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
            
        # If no movement, decelerate
        if not left_input and not right_input and self.knockback_force == pygame.math.Vector2(0, 0):
            self.velocity.x -= self.velocity.x * player.FRICTION * dt

            if abs(self.velocity.x) < 1:
                self.velocity.x = 0

            self.state = "idle"


    def jump(self, dt: float, inputs: List[Direction]):
        """Check if the player should jump

        Args:
            dt (float): the time since the last frame
            inputs (List): the inputs of the player
        """
        # Get the jump input
        jump_input = inputs[2]
        # Check if player can jump
        if jump_input and self.grounded_timer > 0:
            self.is_jumping = True
            self.jump_time_counter = player.JUMP_TIME
            self.velocity.y = player.JUMP_HEIGHT * dt

            if self.jump_sound_time <= 0:
                self.jump_sound.play()
                self.jump_sound_time = player.JUMP_SOUND_TIME

        # Check if the player is jumping
        if jump_input and self.is_jumping:
            if self.jump_time_counter > 0:
                self.velocity.y = player.JUMP_HEIGHT * dt
                self.jump_time_counter -= dt
            else:
                self.is_jumping = False

        # Check if the player is not jumping
        if not jump_input:
            self.is_jumping = False
        
        # Decrease the grounded timer
        self.grounded_timer -= dt
        self.jump_sound_time -= dt


    def limit_speed(self):
        """Limit the speed of the player
        """
        # Limit the speed
        if abs(self.velocity.x) > player.MAX_SPEED:
            self.velocity.x = player.MAX_SPEED * self.velocity.x / abs(self.velocity.x)

        # Check if the player is on the ground
        if self.velocity.y >= 1:
            self.state = "falling"
        elif self.velocity.y < 0:
            self.state = "jumping"


    def out_of_bounds(self):
        """Check if the player is out of bounds
        """
        if self.rect.x < self.bounds.left or self.rect.x > self.bounds.right:
            self.health = 0
        if self.rect.y < self.bounds.top or self.rect.y > self.bounds.bottom:
            self.health = 0
    

    def check_pickup(self, inputs: List[Direction], weapon_pickups: List[WeaponPickUp]) -> bool:
        """Check if the player picked up a weapon

        Args:
            inputs (List[Direction]): the inputs of the player
            weapon_pickups (List[WeaponPickUp]): the weapon pickups

        Returns:
            bool: if the player picked up a weapon
        """
        # Pick up weapon if colliding with a weapon pickup and inputting shoot
        if inputs[3]:
            for pickup in weapon_pickups:
                if self.rect.colliderect(pickup.rect):
                    pickup.pickup(self)

                    self.pickup_sound.play()

                    return True
        
        return False


    def check_shot(self, inputs: List[Direction]) -> Bullet:
        """Check if the player shot a bullet

        Args:
            inputs (List): the inputs of the player

        Returns:
            Bullet: the bullet that was shot
        """
        if inputs[3]:
            return self.weapon.shoot()


    def knockback(self, dt: float):
        """Apply knockback to the player over time

        Args:
            dt (float): the time since the last frame
        """
        # Apply the knockback force
        self.velocity += self.knockback_force * dt

        # Reset the knockback force
        self.knockback_force -= self.knockback_force * player.KNOCKBACK_FRICTION * dt
        
        # Limit the knockback force
        if abs(self.knockback_force.x) < 1:
            self.knockback_force.x = 0
        if abs(self.knockback_force.y) < 1:
            self.knockback_force.y = 0
    

    def gravity(self, dt: float):
        """Apply gravity to the player

        Args:
            dt (float): the time since the last frame
        """
        # Gravity
        gravity = player.GRAVITY * dt if self.velocity.y < 0 else player.GRAVITY_FALL * dt
        self.velocity.y += gravity
    

    def collide(self):
        """Check if the player collided with the terrain
        """
        # Check if grounded
        grounded = False
        is_spring = False

        collisions = self.terrain.collide(self, CollideMode.Predict)

        for (direction, tile) in collisions:
            # Collision for solid tiles
            if type(tile) in [Solid, Mirror]:
                if direction in [Direction.RIGHT, Direction.LEFT]:
                    self.velocity.x = 0
                elif direction == Direction.UP:
                    self.rect.top = tile.rect.bottom
                    self.velocity.y = tile.rect.bottom - self.rect.top
                elif direction == Direction.DOWN:
                    self.rect.bottom = tile.rect.top
                    self.velocity.y = tile.rect.top - self.rect.bottom

                    grounded = True

            # Collision for spring tiles
            if type(tile) == Spring:
                if direction == Direction.RIGHT and tile.direction == Direction.LEFT:
                    self.velocity.x *= -player.SPRING_BOUNCINESS
                    is_spring = True
                elif direction == Direction.LEFT and tile.direction == Direction.RIGHT:
                    self.velocity.x *= -player.SPRING_BOUNCINESS
                    is_spring = True
                elif direction == Direction.UP and tile.direction == Direction.DOWN:
                    self.velocity.y *= -player.SPRING_BOUNCINESS
                    is_spring = True
                elif direction == Direction.DOWN and tile.direction == Direction.UP:
                    self.velocity.y *= -player.SPRING_BOUNCINESS
                    is_spring = True

                    grounded = True

        # Set the grounded timer if the player is grounded
        if grounded:
            if is_spring:
                self.spring_sound.play()
            elif self.grounded_timer < 0:
                self.landing_sound.play()

            self.grounded_timer = player.HANG_TIME


    def update_other(self):
        """Update the weapon and the healthbar
        """
        # Update the weapon
        direction = 1 if self.facing_right else -1
        weapon_x = self.rect.centerx + (direction * self.image.get_width() * 0.5)

        self.weapon.update(
            (weapon_x, self.rect.centery),
            direction
        )

        # Update the healthbar
        self.healthbar.update(self.rect.center)


    def update_animation(self, dt: float):
        """Update the animation of the player

        Args:
            dt (float): the time since the last frame
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
        
        # Set image if falling or jumping
        if self.state == "falling":
            self.image = self.falling
        elif self.state == "jumping":
            self.image = self.jumping
        
        # Set image if hurt
        if self.hurt_image_time > 0:
            self.image = self.hurt
            self.hurt_image_time -= dt


    def check_health(self):
        """Check if the player is dead
        """
        if self.health <= 0:
            self.kill()


    def update(self, weapon_pickups: List[WeaponPickUp], dt: float) -> Bullet:
        """Update the player

        Args:
            dt (float): the time since the last update

        Returns:
            Bullet: the new bullet
        """
        new_bullets = self.update_inputs(weapon_pickups, dt)
        
        # Apply knockback
        self.knockback(dt)

        # Apply gravity
        self.gravity(dt)

        # Handle collisions
        self.collide()

        # Update animation
        self.update_animation(dt)

        # Check health
        self.check_health()

        # Update the player's position
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        
        # Update weapon and healthbar
        self.update_other()

        return new_bullets


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