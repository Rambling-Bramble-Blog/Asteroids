import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

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