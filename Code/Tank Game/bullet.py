import pygame


class Bullet:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = 3
        self.time = 0
        self.color = (0, 0, 0)
        self.speed_x = 2
        self.speed_y = 2

    def move(self, screen):
        self.x_pos += self.speed_x
        self.y_pos += self.speed_y

    def shootRight(self, screen):

        while self.time < 3000:
            self.x_pos += self.speed_x

            pygame.draw.circle(screen, (0, 0, 255), (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1

    def shootLeft(self, screen):

        while self.time < 3000:
            self.x_pos -= self.speed_x

            pygame.draw.circle(screen, (0, 0, 255), (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1

    def shootUp(self, screen):

        while self.time < 3000:
            self.y_pos -= self.speed_y

            pygame.draw.circle(screen, (0, 0, 255), (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1

    def shootDown(self, screen):

        while self.time < 3000:
            self.y_pos += self.speed_y

            pygame.draw.circle(screen, (0, 0, 255), (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1
