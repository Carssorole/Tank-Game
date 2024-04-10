import pygame


class Bullet:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = 3
        self.color = (0, 0, 0)
        self.speed_x = 2
        self.speed_y = 2

    def move(self, screen):
        self.x_pos += self.speed_x

    def shoot(self, screen):
        time = 10
        if time > 0:
            pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)
            self.x_pos += self.speed_x
            self.x_pos += self.speed_y
            time -= 1
