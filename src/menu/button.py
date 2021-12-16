import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, id_, rect, color, highlight_color, press_color, text, text_color):
        super().__init__()
        self.id = id_

        self.rect = pygame.Rect(rect)

        self.color = color
        self.highlight_color = highlight_color
        self.press_color = press_color

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
        if self.pressed:
            color = self.press_color
        elif self.hover:
            color = self.highlight_color
        else:
            color = self.color

        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.font.render(self.text, True, self.text_color), self.text_pos)