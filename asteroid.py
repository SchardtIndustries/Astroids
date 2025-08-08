import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = (255, 255, 255)
              
    def draw(self, surface):
        center_x = int(self.position.x)
        center_y = int(self.position.y)
        draw_radius = int(self.radius)

        pygame.draw.circle(surface, self.color, (center_x, center_y), draw_radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
