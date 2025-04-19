from text import *
from constants import *

class Score(Text):
    def __init__(self, points):
        
    
        self.points = points
        self.points_str = f"{self.points}"
        super().__init__(self.points_str)
