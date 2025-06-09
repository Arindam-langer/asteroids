import pygame
from constants import *
from player import Player
from asteroid import Asteroids
from AsteroidField import AsteroidField

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()


    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2) #triangle
    dt = 0

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        player.update(dt)
        screen.fill("black")            
        player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000  #fps

if __name__ == "__main__":
    main()