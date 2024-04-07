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

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bullet")

WHITE = (255, 255, 255)

bullet = Bullet(200, 200, 3, -3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    bullet.move()
    bullet.draw(screen)
    
    pygame.display.flip()

pygame.quit()

