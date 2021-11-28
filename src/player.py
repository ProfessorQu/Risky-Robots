import pygame


# The 2D platformer player class.
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        super().__init__()

        self.x = x
        self.y = y

        self.speed = speed
        self.velocity = pygame.math.Vector2(0, 0)

        self.facingRight = True

        self.image = pygame.image.load("src/assets/player.png")
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width() * scale,
                self.image.get_height() * scale
            )
        )

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.velocity.x = -self.speed
            self.facingRight = False
        elif key[pygame.K_d]:
            self.velocity.x = self.speed
            self.facingRight = True
        else:
            self.velocity.x = 0

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def draw(self, surface):
        image = pygame.transform.flip(self.image, not self.facingRight, False)
        surface.blit(image, self.rect)
