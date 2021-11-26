import pygame


class Player:
    def __init__(self, rect: pygame.Rect, color):
        self.rect = rect
        self.color = color

        self.speed = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
