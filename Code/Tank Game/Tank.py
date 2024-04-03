"""
This is the Tank class.
Tutorials used for this class:
Initial creation: https://reintech.io/blog/how-to-create-a-video-game-character-with-pygame#google_vignette
"""
import pygame
from pygame import *


class Tank(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        loaded_image = pygame.image.load(image)
        self.image = pygame.transform.scale(loaded_image, (width, height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))