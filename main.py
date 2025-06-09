import pygame
from constants import *
from player import Player
from asteroid import Asteroids
from AsteroidField import AsteroidField
from circle_shape import *
from shots import Shot
import sys
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    font = pygame.font.Font(None,36)

    asteroids = pygame.sprite.Group() ##bunch of assteroids
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
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
        for ass in asteroids:
            if ass.collision(player):
                print("over!")
                sys.exit()
            for shot in shots:
                if ass.collision(shot):
                    shot.kill()
                    score += int(100 / ass.radius)
                    ass.split()
        screen.fill("black")            
        player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        pygame.display.flip()
        dt = clock.tick(60)/1000  #fps

if __name__ == "__main__":
    main()