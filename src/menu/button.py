import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, id_, rect, color, highlight_color, text, text_color):
        super().__init__()
        self.id = id_

        self.rect = pygame.Rect(rect)

        self.color = color
        self.highlight_color = highlight_color

        self.image = pygame.image.load(f"src/assets/maps/map{self.id + 1}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        self.text = text
        self.text_color = text_color

        self.font = pygame.font.SysFont("Bauhaus 93", 50)

        self.text_pos = (self.rect.centerx - self.font.size(self.text)[0] / 2, self.rect.centery - self.font.size(self.text)[1] / 2)
    
    @property
    def hover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    @property
    def pressed(self):
        return self.hover and pygame.mouse.get_pressed()[0]

    def draw(self, surface):
        image = self.image.copy()
        if self.hover:
            image.fill(self.highlight_color, special_flags=pygame.BLEND_RGBA_MULT)
        else:
            image.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)

        surface.blit(image, self.rect)

        surface.blit(self.font.render(self.text, True, self.text_color), self.text_pos)
