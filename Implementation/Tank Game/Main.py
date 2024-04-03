#the main file for the Atari: Combat remake
import pygame
from pygame.locals import *
from Tank import Tank
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
tank1 = Tank("sprites/tank1.png", 100, 100, 70, 70)
tank2 = Tank("sprites/tank2.png", 1000, 600, 80, 50)

while running:
    #main running clock, all realtime computation will be done in here including collisions, player movement, and such
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                tank1.x -= 10
            elif event.key == K_RIGHT:
                tank1.x += 10
            elif event.key == K_UP:
                tank1.y -= 10
            elif event.key == K_DOWN:
                tank1.y += 10
            if event.key == K_a:
                tank2.x -= 10
            elif event.key == K_d:
                tank2.x += 10
            elif event.key == K_w:
                tank2.y -= 10
            elif event.key == K_s:
                tank2.y += 10

    screen.fill("green")
    tank1.draw(screen)
    tank2.draw(screen)
    pygame.display.update()

    #render game here


    pygame.display.flip()

    clock.tick(60)

pygame.quit()

