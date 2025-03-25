import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOR, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            random_angle = random.uniform(20, 30)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_roid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_roid1.velocity = velocity1 * 1.2
            new_roid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_roid2.velocity = velocity2 * 1.2
        self.kill()
