import pygame

import sys

from constants import *

from player import Player

from asteroid import Asteroid

from asteroidfield import AsteroidField

from shot import Shot

clock = pygame.time.Clock()

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player_object = Player(player_x, player_y)
    AsteroidField_object = AsteroidField()

    while running:
        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        updatable.update(dt)

        for sprite in asteroids:
            if sprite.check_collision(player_object) is True:
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)  
      
        pygame.display.flip()

if __name__ == "__main__":
    main()
