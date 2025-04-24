import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from bullets import *
from score import *
from UI import *
from game_state import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




def main():
    pygame.init

    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    enemies = pygame.sprite.Group()
    weapons = pygame.sprite.Group()
    renderable = pygame.sprite.Group()
    loopable = pygame.sprite.Group()

    Asteroid.containers = (enemies, updatable, drawable)
    Player.containers = (drawable, loopable)   
    AsteroidField.containers = (updatable)
    Bullets.containers = (weapons, updatable, drawable, loopable)
    Score.containers = (renderable)
    #Text.containers = (renderable)
                        
    score_label = Text("Score:")
    score_value = Score(0)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    UI_ = UI(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    score_label.render_text()

    # Game State
    state = GameState.PLAYING
    # Game Loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print(f"PRINTED {event.key == pygame.K_p}")
                if event.key == pygame.K_p and state == GameState.PLAYING:
                   state = GameState.PAUSED
                elif event.key == pygame.K_p and state == GameState.PAUSED:
                   state = GameState.PLAYING
            
                elif event.key == pygame.K_SPACE and state == GameState.GAME_OVER:
                    state = GameState.PLAYING
                    score_value.kill()
                    updatable.empty()
                    drawable.empty()
                    enemies.empty()
                    weapons.empty()
                    renderable.empty()
        
        pygame.Surface.fill(screen, ("#000000"))
        
        if state == GameState.GAME_OVER:
            updatable.update(dt)
            
        if state == GameState.PLAYING:
            player.update(dt)
            updatable.update(dt)
            screen.blit(score_value.rendered_txt, (80,10))
            screen.blit(score_label.rendered_txt, (10,10))
            try:
                for enemy in enemies:
                    if enemy.collision(player):
                        enemy.kill()
                        
                        
                        if player.lives > 1:
                            player.lives_upd(-1)
                    
                        else:
                            player.lives_upd(-1)
                            player.kill()
                            state = GameState.GAME_OVER


            except Exception as e:
                print(e)
        #### 
        score_compare = score_value.points
        for enemy in enemies:
            for weapon in weapons:
                if enemy.collision(weapon):
                    enemy.split()
                    enemy.point_calculation(score_value)
                    weapon.kill()
                    

        for obj in drawable:
            if obj in loopable:
                obj.coordinate_reset(obj.position[0], obj.position[1])
            obj.draw(screen)
            
        for obj in renderable:
            
            if obj.points != score_compare:
                obj.render_text()
                
        if state == GameState.PAUSED:
            UI_.pause_screen()
            screen.blit(score_value.rendered_txt, (((SCREEN_WIDTH - score_value.width) / 2, (SCREEN_HEIGHT / 4) + score_value.height / 2)))
            screen.blit(score_label.rendered_txt, (((SCREEN_WIDTH - score_label.width) / 2, (SCREEN_HEIGHT / 4) - score_label.height)))
        
        if state == GameState.GAME_OVER:
            UI_.game_over_screen()
            screen.blit(score_value.rendered_txt, (((SCREEN_WIDTH - score_value.width) / 2, (SCREEN_HEIGHT / 4) + score_value.height / 2)))
            screen.blit(score_label.rendered_txt, (((SCREEN_WIDTH - score_label.width) / 2, (SCREEN_HEIGHT / 4) - score_label.height)))

        pygame.display.flip()
        

        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()