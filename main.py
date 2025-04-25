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
from game_init import *

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

    game_init = GameInit("Score:", 0, SCREEN_WIDTH, SCREEN_HEIGHT)                    
    
    score_label = Text(game_init.get_score_label())
    score_value = Score(game_init.get_score_value())
    player = Player(game_init.get_screen_width()/ 2, game_init.get_screen_heigth() / 2)
    asteroid_field = game_init.get_asteroid_field()
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
                match event.key:
                    case pygame.K_p|pygame.K_ESCAPE:
                        if state == GameState.PLAYING:
                            state = GameState.PAUSED
                        elif state == GameState.PAUSED:
                            state = GameState.PLAYING
                        
                    case pygame.K_SPACE:
                        if state == GameState.GAME_OVER:
                            player.timer = 1
                            state = GameState.PLAYING
                            
                            loopable.empty()
                            renderable.empty()
                            updatable.empty()
                            drawable.empty()
                            enemies.empty()
                            weapons.empty()
                            renderable.empty()
                            game_init2 = GameInit("Score:", 0, SCREEN_WIDTH, SCREEN_HEIGHT)
                            game_init = game_init2 

        pygame.Surface.fill(screen, ("#000000"))
        
        if state == GameState.GAME_OVER:
            updatable.update(dt)
            
        if state == GameState.PLAYING:
            player.update(dt)
            updatable.update(dt)
            screen.blit(score_value.rendered_txt, (80,10))
            screen.blit(score_label.rendered_txt, (10,10))
            
            try:
                if player.collision_check(enemies):
                    if player.check_hp(-1) < 1:
                        state = GameState.GAME_OVER 
                if state == GameState.PLAYING:
                    if player.collision_check(weapons):
                        if player.check_hp(-1) < 1:
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
            score_v = score_value.get_rect()
            score_l = score_label.get_rect()
            screen.blit(score_value.rendered_txt, (((SCREEN_WIDTH - score_v.width) / 2, (SCREEN_HEIGHT / 4) + score_v.height / 2)))
            screen.blit(score_label.rendered_txt, (((SCREEN_WIDTH - score_l.width) / 2, (SCREEN_HEIGHT / 4) - score_l.height)))

        pygame.display.flip()
        

        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()