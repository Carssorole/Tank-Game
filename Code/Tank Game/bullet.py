import pygame
import sys

pygame.init()

width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Black Circle")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    radius = 5
    circle_center = (width // 2, height // 2)
    pygame.draw.circle(screen, BLACK, circle_center, radius)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
