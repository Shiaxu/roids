import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):

    

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def coordinate_reset(self, width, height):
        x = width
        y = height
        if width >= SCREEN_WIDTH:
            x = 0
        if width <= 0:
            x = SCREEN_WIDTH
        if height >= SCREEN_HEIGHT:
            y = 0
        if height <= 0:
            y = SCREEN_HEIGHT
        self.position = pygame.Vector2(x, y)
        

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, other):
        
        return self.position.distance_to(other.position) <= self.radius + other.radius
    
