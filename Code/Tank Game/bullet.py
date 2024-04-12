import pygame


class Bullet:
    def __init__(self, x_pos, y_pos, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = 4
        self.time = 0
        self.color = color
        self.speed_x = 1
        self.speed_y = 1
        self.cooldown = False
        self.direction = 0