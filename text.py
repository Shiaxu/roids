import pygame

pygame.font.init()
font = pygame.font.SysFont("arial", 24)

class Text:
    def __init__(self, text):
        self.text = text
        
        """self.antialias = antialias
        self.color = color
        self.background = background
        self.font = font
        self.size = size"""

        self.rendered = False
        self.rendered_str = font.render(self.text, True, "white")

    def render_text(self):
        self.rendered_str = font.render(self.text, True, "white")
        self.rendered = True


        