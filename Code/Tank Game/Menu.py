"""
Tutorials Used:
https://www.makeuseof.com/start-menu-and-game-over-screen-with-pygame/#:~:text=Creating%20the%20Start%20Menu&text=Next%2C%20you%20will%20add%20a,other%20elements%20on%20the%20screen.&text=You%20can%20then%20add%20the,to%20the%20main%20game%20loop.&text=Now%2C%20the%20start%20menu%20will%20be%20drawn%20to%20the%20screen.

ChatGPT4 used to generate artwork, then edited with PowerPoint
"""
import pygame


def draw_start_menu(screen, width, height):
    background_image = pygame.image.load('../Assets/ScrummyTankersStartMenu.png')
    background_image = pygame.transform.scale(background_image, (width, height))

    screen.blit(background_image, (0, 0))

    pygame.display.update()


def draw_game_over(screen, width, height):
    background_image = pygame.image.load('../Assets/GameOver.png')
    background_image = pygame.transform.scale(background_image, (width, height))

    screen.blit(background_image, (0, 0))

    pygame.display.update()


def draw_instructions_menu(screen, width, height):
    background_image = pygame.image.load('../Assets/instructions.png')
    background_image = pygame.transform.scale(background_image, (width, height))

    screen.blit(background_image, (0, 0))

    pygame.display.update()

