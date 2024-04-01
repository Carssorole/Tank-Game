#the main file for the Atari: Combat remake
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    #main running clock, all realtime computation will be done in here including collisions, player movement, and such
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("green")

    #render game here

    #game tests here(colission and such)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()

