import pygame

pygame.font.init()


class Text(pygame.sprite.Sprite):
    def __init__(self, text, size=24):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.text = text
        self.size = size
        """self.antialias = antialias
        self.color = color
        self.background = background
        self.font = font
        """
        self.font = pygame.font.SysFont("arial", self.size)
        
        self.rendered_txt = self.font.render(self.text, True, "white")
        self.rendered_rect = self.rendered_txt.get_rect()
        self.width = self.rendered_rect.width
        self.height = self.rendered_rect.height

    def render_text(self):
        
        self.rendered_txt = self.font.render(self.text, True, "white")

    def get_rect(self):
        self.rendered_rect = self.rendered_txt.get_rect()
        return self.rendered_txt.get_rect()

