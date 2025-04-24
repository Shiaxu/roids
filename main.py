import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from bullets import *
from score import *
from game_over import *
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

    Asteroid.containers = (enemies, updatable, drawable)
    Player.containers = (drawable)   
    AsteroidField.containers = (updatable)
    Bullets.containers = (weapons, updatable, drawable)
    Score.containers = (renderable)
    #Text.containers = (renderable)
                        
    score_label = Text("Score:")
    score_value = Score(0)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    game_over = GameOver(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
    
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
                if event.key == pygame.K_p and state == GameState.PLAYING:
                   state = GameState.PAUSED
                if event.key == pygame.K_p and state == GameState.PAUSED:
                   state = GameState.PLAYING

        pygame.Surface.fill(screen, ("#000000"))
        
        if state == GameState.GAME_OVER:
            updatable.update(dt)

        if state == GameState.PLAYING:
            player.update(dt)
            updatable.update(dt)
            screen.blit(score_value.rendered_str, (80,10))
            screen.blit(score_label.rendered_str, (10,10))
            try:
                for enemy in enemies:
                    if enemy.collision(player):
                        enemy.kill()
                        
                        
                        if player.lives > 0:
                            player.lives_upd(-1)
                    
                        else:
                            player.kill()
                            state = GameState.GAME_OVER


            except Exception as e:
                print(e)

        score_compare = score_value.points


        for enemy in enemies:
            for weapon in weapons:
                if enemy.collision(weapon):
                    enemy.split()
                    enemy.point_calculation(score_value)
                    weapon.kill()
                    

        for obj in drawable:
            obj.coordinate_reset(obj.position[0], obj.position[1])
            obj.draw(screen)
            
        for obj in renderable:
            
            if obj.points != score_compare:
                obj.render_text()
                

        if state == GameState.GAME_OVER:
            game_over.game_over_screen()
            score_value_rect = score_value.rendered_str.get_rect()
            score_label_rect = score_label.rendered_str.get_rect()
            #print(f"PRINTED {game_over.text_rect_width} and {game_over.text_rect_height}")
            screen.blit(score_value.rendered_str, (((SCREEN_WIDTH - score_value_rect.width) / 2, (SCREEN_HEIGHT / 4) + score_value_rect.height / 2)))
            screen.blit(score_label.rendered_str, (((SCREEN_WIDTH - score_label_rect.width) / 2, (SCREEN_HEIGHT / 4) - score_label_rect.height)))

        #screen.blit(score_value.rendered_str, (80,10))
        #screen.blit(score_label.rendered_str, (10,10))
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

if __name__ == "__main__":
    main()