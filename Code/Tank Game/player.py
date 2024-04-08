import pygame

SCOREBOARD_HEIGHT = 66

class Player(pygame.sprite.Sprite):
    def __init__(self, images, x, y):
        super().__init__()
        self.elapsed = 0
        self.sprites = images
        self.index = 0
        self.image = self.sprites[self.index]
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y + SCOREBOARD_HEIGHT

    # Update is used to change sprite images upon key inputs
    def update(self, index):
        self.index = index

        if self.index >= len(self.sprites):
            self.index = 0

        self.image = self.sprites[self.index]

    def updateJumbotron(self):
        self.elapsed = self.elapsed + 1
        if self.elapsed > 10:
            self.update(self.index + 1)
            self.elapsed = 0
            self.image = pygame.transform.rotate(self.image, 90)

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, pixels):
        self.rect.y -= pixels

    def moveBack(self, pixels):
        self.rect.y += pixels
