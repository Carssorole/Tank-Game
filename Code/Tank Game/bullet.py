import pygame


class Bullet:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = 5
        self.color = (0, 0, 0)

    def move(self):
        self.x_pos += 2
        self.y_pos += 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)
