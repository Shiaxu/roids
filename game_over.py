import pygame

pygame.font.init()
font = pygame.font.SysFont("arial", 69)

class GameOver:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        #self.text_rect_width = 0
        #self.text_rect_height = 0

    #def border(self):

    def game_over_screen(self):
        
        rendered_txt = font.render("Game Over!", True, "white")
        text_rect = rendered_txt.get_rect()
        #self.text_rect_height = text_rect.height
        #self.text_rect_width = text_rect.width
        self.screen.blit(rendered_txt, ((self.width - text_rect.width)/ 2, (self.height - text_rect.height) / 2))
        Rect = pygame.Rect
        r = Rect(self.width/2 - text_rect.width, self.height/2 - text_rect.height , text_rect.width*2 , text_rect.height*2)
        pygame.draw.rect(self.screen, "green", r, 3)

 

