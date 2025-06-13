import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    #initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    #create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() # asteroid group
    bullets = pygame.sprite.Group()

    # add all player instances into two groups (NOTE: need to do before initialize player)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (updatable, drawable)


    #initialize 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroids_field = AsteroidField()

    #start game loop
    while(True):
        #set quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # draw object
        for object in drawable:
            object.draw(screen)
        
        #update position
        updatable.update(dt)

        #detect collision between player and asteroids
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                return

        #Update the full display surface to the screen, be sure to call it last
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()