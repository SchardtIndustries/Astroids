import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        left = self.position.x - self.radius
        top = self.position.y - self.radius
        width = 2 * self.radius
        height = 2 * self.radius
        self.rect = pygame.Rect(left, top, width, height)

    def draw(self, screen):
        pass

    def update(self, dt):
        self.rect.center = self.position

    def check_collision(self, other_circle):
        distance = self.position.distance_to(other_circle.position)

        if distance < (self.radius + other_circle.radius):
            return True
        else:
            return False
