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

    def move(self, screen):
        self.x_pos += self.speed_x
        self.y_pos += self.speed_y

    def shootRight(self, screen):

        while self.time < 500:
            self.x_pos += self.speed_x

            pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1
            pygame.display.update()

    def shootLeft(self, screen):

        while self.time < 500:
            self.x_pos -= self.speed_x

            pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1
            pygame.display.update()

    def shootUp(self, screen):

        while self.time < 500:
            self.y_pos -= self.speed_y

            pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1

    def shootDown(self, screen):

        while self.time < 500:
            self.y_pos += self.speed_y

            pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)
            self.time = self.time + 1
