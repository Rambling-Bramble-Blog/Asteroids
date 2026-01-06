import pygame, random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # Initial rotation angle in degrees

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)
        
    def update(self, dt):
        # Example of simple rotation and movement logic for the asteroid
        # self.rotation += 20 * dt  # Rotate at 20 degrees per second
        self.position += self.velocity * dt  # Move according to velocity
        
    def split(self):
        self.kill()  # Remove the current asteroid
        # This method can be called to split the asteroid into smaller pieces
        if self.radius <= ASTEROID_MIN_RADIUS:  # Do not split if the asteroid is too small
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            self. new_asteroid1_velocity = self.velocity.rotate(angle)
            self.new_asteroid2_velocity = self.velocity.rotate(-angle)
            self.new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            self.velocity_scale = 1.2
            
            self.new_asteroid1 = Asteroid(self.position.x, self.position.y, self.new_asteroid_radius)
            self.new_asteroid2 = Asteroid(self.position.x, self.position.y, self.new_asteroid_radius)
            self.new_asteroid1.velocity = self.new_asteroid1_velocity * self.velocity_scale
            self.new_asteroid2.velocity = self.new_asteroid2_velocity * self.velocity_scale