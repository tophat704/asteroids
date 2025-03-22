# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    start_x = SCREEN_WIDTH / 2
    start_y = SCREEN_HEIGHT / 2
    player = Player(start_x, start_y)
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BACKGROUND_COLOR)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()