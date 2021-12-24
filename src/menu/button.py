import pygame

class Button(pygame.sprite.Sprite):
    def __init__(
        self, id_: int, image_path: str, rect: pygame.Rect, color: pygame.Color, highlight_color: pygame.Color,
        text: str, font_size: int, text_color: pygame.Color, highlight_text_color: pygame.Color = None
        ):
        """Initialize the button

        Args:
            id_ (int): the id of the button
            rect (pygame.Rect): the rect of the button
            color (pygame.Color): the color of the button
            highlight_color (pygame.Color): the color of the button when hovered
            text (str): the text of the button
            text_color (pygame.Color): the color of the text
        """
        super().__init__()
        self.id = id_

        self.rect = pygame.Rect(rect)

        # Set the colors
        self.color = color
        self.highlight_color = highlight_color

        # Create the image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

        # Set the text
        self.text = text
        self.text_color = text_color
        self.highlight_text_color = highlight_text_color

        # Set the font
        self.font = pygame.font.SysFont("Bauhaus 93", font_size)

        # Set the text position
        self.text_pos = (self.rect.centerx - self.font.size(self.text)[0] / 2, self.rect.centery - self.font.size(self.text)[1] / 2)
    
    @property
    def hover(self) -> bool:
        """Check if the mouse is hovering over the button

        Returns:
            bool: True if the mouse is hovering over the button, False otherwise
        """
        return self.rect.collidepoint(pygame.mouse.get_pos())

    @property
    def pressed(self) -> bool:
        """Check if the button is pressed

        Returns:
            bool: True if the button is pressed, False otherwise
        """
        return pygame.mouse.get_pressed()[0] and self.hover

    def draw(self, surface: pygame.Surface):
        """Draw the button

        Args:
            surface (pygame.Surface): the surface to draw the button on
        """
        # Copy the image
        image = self.image.copy()
        text_color = self.text_color
        # If the mouse is hovering over the button, change the color
        if self.hover:
            image.fill(self.highlight_color, special_flags=pygame.BLEND_RGBA_MULT)
            if self.highlight_text_color is not None:
                text_color = self.highlight_text_color
        else:
            image.fill(self.color, special_flags=pygame.BLEND_RGBA_MULT)

        # Draw the image and text
        surface.blit(image, self.rect)
        surface.blit(self.font.render(self.text, True, text_color), self.text_pos)
