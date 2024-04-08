import pygame


class Bullet:
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = 5
        self.color = (0, 0, 0)

    def move(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)