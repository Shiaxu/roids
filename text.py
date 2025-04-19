import pygame

pygame.font.init()
font = pygame.font.SysFont("arial", 24)

class Text(pygame.sprite.Sprite):
    def __init__(self, text):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.text = text
        
        """self.antialias = antialias
        self.color = color
        self.background = background
        self.font = font
        self.size = size"""

        
        self.rendered_str = font.render(self.text, True, "white")

    def render_text(self):
        print(self.text)
        self.rendered_str = font.render(self.text, True, "white")

        

