from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            small_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            small_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            small_asteroid_one.velocity = velocity1 * 1.2
            small_asteroid_two.velocity = velocity2 * 1.2