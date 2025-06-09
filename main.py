import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill("black")            
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000  #fps

if __name__ == "__main__":
    main()