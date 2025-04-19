from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new1 = self.velocity.rotate(random_angle)
        new2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius )
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius )
        asteroid1.velocity = new1 * 1.2
        asteroid2.velocity = new2 * 1.2
    
            

    def point_calculation(self, other):
        points = 0
        if self.radius == ASTEROID_MAX_RADIUS:
            points = ASTEROID_POINTS_LARGE  
        if ASTEROID_MIN_RADIUS > self.radius < ASTEROID_MAX_RADIUS:
            points = ASTEROID_POINTS_MEDIUM      
        if self.radius == ASTEROID_MIN_RADIUS:
            points = ASTEROID_POINTS_SMALL
        other.points += points