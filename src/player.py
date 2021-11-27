import pygame


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, rect, color):
        super().__init__()

        self.image = pygame.Surface(rect.size)
        self.image.fill(color)

        self.rect = rect

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Platform(pygame.sprite.Sprite):
    def __init__(self, rect, color):
        super().__init__()

        self.image = pygame.Surface(rect.size)
        self.image.fill(color)

        self.rect = rect

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
