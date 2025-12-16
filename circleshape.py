import pygame
import constants
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def check_bounds(self):
        margin = 100
        if (self.position.x < -margin or
            self.position.x > constants.SCREEN_WIDTH + margin or
            self.position.y < -margin or
            self.position.y > constants.SCREEN_HEIGHT + margin):
            self.kill()

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius + other.radius):
            return True
        return False