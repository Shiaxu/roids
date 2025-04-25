from asteroidfield import *

class GameInit:
    def __init__(self, score_label, score_value, screen_width, screen_heigth):
        self.score_label = score_label
        self.score_value = score_value
        self.screen_width = screen_width
        self.screen_heigth = screen_heigth
        
    
    def get_score_label(self):
        return self.score_label
    def get_score_value(self):
        return self.score_value
    def get_screen_width(self):
        return self.screen_width
    def get_screen_heigth(self):
        return self.screen_heigth
    def get_asteroid_field(self):
        return AsteroidField()