from circleshape import CircleShape
import pygame
import constants
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            split1_velocity = self.velocity.rotate(angle)
            split2_velocity = self.velocity.rotate(angle * (-1))
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = split1_velocity * 1.2
            split2.velocity = split2_velocity * 1.2