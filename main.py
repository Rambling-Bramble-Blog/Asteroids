import pygame, sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time between frames
    
    updatable =  pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)
        
        for element in drawable:
            element.draw(screen)
            
        for asteroid in asteroids:
            if player.collide_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
        
        pygame.display.flip()
        dt = clock.tick (60)/1000  # Limit to 60 frames per second
        # print(dt)
    
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
