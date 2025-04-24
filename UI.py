import pygame
from text import *

pygame.font.init()
font = pygame.font.SysFont("arial", 69)

class UI:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        #self.text_rect_width = 0
        #self.text_rect_height = 0

    #def border(self):

    def game_over_screen(self):
        g_o_text = Text("Game Over!", 69)
        game_over_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        game_over_surface.fill((0, 0, 0, 155))
        self.screen.blit(game_over_surface, (0,0))
        

        self.screen.blit(g_o_text.rendered_txt, ((self.width - g_o_text.width)/ 2, (self.height - g_o_text.height) / 2))
        Rect = pygame.Rect
        r = Rect(self.width/2 - g_o_text.width, self.height/2 - g_o_text.height , g_o_text.width*2 , g_o_text.height*2)
        pygame.draw.rect(self.screen, "red", r, 3)

    def pause_screen(self):
        pass


