from circleshape import *
from bullets import *
from game_state import *

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.timer = 0
        self.lives = 1

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self , dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if self.timer <= 0 and keys[pygame.K_SPACE]:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN 

    def move(self, dt):
        
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        a = self.position + forward * self.radius

        shot = Bullets(a.x, a.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def lives_upd(self, number):
        self.lives += number
    
    def check_hp(self, hp):
        if self.lives > 1:
            self.lives_upd(hp)
            return self.lives
        else:
            self.lives_upd(hp)
            self.kill()
            return self.lives
        
    def collision_check(self, group):
        for obj in group:
            if obj.collision(self):
                obj.kill()
                return True
        return False
