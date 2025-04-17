import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from bullets import *


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def main():
    pygame.init

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    enemies = pygame.sprite.Group()
    weapons = pygame.sprite.Group()

    Asteroid.containers = (enemies, updatable, drawable)
    Player.containers = (updatable, drawable)   
    AsteroidField.containers = (updatable)
    Bullets.containers = (weapons, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.Surface.fill(screen, ("#000000"))
        updatable.update(dt)
        try:
            for obj in enemies:
                if obj.collision(player):
                    sys.exit("Game Over!")
        except Exception as e:
            print(e)
        for enemy in enemies:
            for weapon in weapons:
                if enemy.collision(weapon):
                    enemy.split()
                    weapon.kill()

        for obj in drawable:
            
            obj.coordinate_reset(obj.position[0], obj.position[1])
            obj.draw(screen)
            #print(f"PRINTED {obj.position}")
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()