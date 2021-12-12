import pygame

from src.constants import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, terrain):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("src/assets/bullet.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * BulletVars.SCALE,
                self.image.get_height() * BulletVars.SCALE,
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.dir = direction

        self.velocity = pygame.math.Vector2(
            direction * BulletVars.SPEED, 0
        )

        self.terrain = terrain

    def update(self, dt, players):
        self.rect.x += self.velocity.x * dt

        for player in players:
            if self.rect.colliderect(player.rect):
                player.hit(10)

                return True
            

        if (self.rect.x < 0 or self.rect.x > WIDTH):
            return True
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            return True
        if self.terrain.collide(self, "Current"):
            return True
        
        return False

    def draw(self, screen):
        image = pygame.transform.flip(self.image, self.dir != 1, False)
        screen.blit(image, self.rect)
