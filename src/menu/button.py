import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, rect, color, highlight_color, press_color, text, text_color):
        super().__init__()
        self.rect = pygame.Rect(rect)

        self.color = color
        self.highlight_color = highlight_color
        self.press_color = press_color

        self.text = text
        self.text_color = text_color

        self.font = pygame.font.SysFont("Bauhaus 93", 50)

        self.text_pos = (self.rect.centerx - self.font.size(self.text)[0] / 2, self.rect.centery - self.font.size(self.text)[1] / 2)
        
    def draw(self, surface):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        surface.blit(self.font.render(self.text, True, self.text_color), self.text_pos)